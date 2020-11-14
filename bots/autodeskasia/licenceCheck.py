"""
You are given two tables products and users in a MySQL database. The products table has columns product_name and product_licenses (valid licenses for this product, separated by commas). The users table has columns user_name and product_licenses (licenses that this user has, separated by commas).

Your task is to fetch information from the database and print the following info to the console: For every pair <user, product> you should print true if the user has at least one of the valid licenses for this product, and false otherwise.

Database credentials
Host: localhost
Username: test
Password: empty (no password)
Database name: ri_db
Example

For the following tables products

product_name	product_licenses
Benifema	0h72PQzGzq
Jutafenac	12dBuZZB4N,NHe2NB5ugq,0pd3z81168,pU85XxhyH5
Lipsin	z3orr4T82y,AK1PQYA1Vp,11N9mnOaxT
Raxone	Oi48ZGe5Q7
and users

user_name	product_licenses
Patrick Miller	0pd3z81168,0h72PQzGzq,12dBuZZB4N
Zac Patel	b9jsp75JFj,IbHKpn7732,pU85XxhyH5
The following output should be printed to the standard output stream:

User Patrick Miller:
  Benifema: true
  Jutafenac: true
  Lipsin: false
  Raxone: false
User Zac Patel:
  Benifema: false
  Jutafenac: true
  Lipsin: false
  Raxone: false
"""

from sqlalchemy import Column, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'
    product_name = Column(String, primary_key=True)
    product_licenses = Column(String)

class User(Base):
    __tablename__ = 'users'
    user_name = Column(String, primary_key=True)
    product_licenses = Column(String)

def main():
    engine = create_engine("mysql+mysqlconnector://test:@localhost/ri_db")
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()

    licences = {}
    product_names = []
    for p in s.query(Product):
        product_names.append(p.product_name)
        codes = p.product_licenses.split(',')
        for c in codes:
            licences[c] = p.product_name

    for u in s.query(User):
        print(f"User {u.user_name}:")
        codes = u.product_licenses.split(',')
        user_licences = {}
        for c in codes:
            if c in licences:
                user_licences[licences[c]] = True
        for name in product_names:
            has_licence = 'true' if name in user_licences else 'false'
            print(f"  {name}: {has_licence}")

    s.commit()
    s.close()

if __name__ == '__main__':
    main()
