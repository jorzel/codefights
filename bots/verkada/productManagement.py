
"""
You work at an electronics shop, and you've just received a shipment containing new models of Verkada security cameras. With these new items, you'll need to make some updates to your product database.

Each product in your database has a unique SKU (id) and a product name (name), and the system accepts several different commands:

The methods that should be supported are listed below:

createProduct(id, name) - creates a record for a new product. Returns false if a product with the specified id already exists, and true otherwise;
updateProduct(id, name) - updates the product with the provided info. Returns false if the product with such id does not exist, and true otherwise.
deleteProduct(id) - deletes the provided product. Returns false if the product with this id does not exist, and true otherwise.
findProductById(id) - finds a product by id. Returns the product (in the form of a JSON) if the product with this id exists, and null otherwise.
findProductByTitle(title) - find a product by title. Returns the product (in the form of a JSON) if the product with this title exists, and null otherwise.
For each command of the first three types, return its result - "true" or "false" and for the last two commands return the product - its result as a stringified JSON (or "null" if no product was found).

Example

For operations = [["createProduct", "10", "Camera_10"], ["createProduct", "10", "Camera_10"], ["updateProduct", "10", "New_Camera_10"], ["deleteProduct", "9"],["findProductById", "9"], ["findProductById", "10"], ["findProductByTitle", "Camera_10"], ["findProductByTitle", "New_Camera_10"]], the output should be
productManagement(operations) = ["true", "false", "true", "false", "null", "{"id":"10","title":"New_Camera_10"}", "null", "{"id":"10","title":"New_Camera_10"}"].
"""


class ProductManager:
    products = []
    def createProduct(self, id, title):
        # TODO: return false if the product id already exists
        if self.findProductById(id):
            return False
        product = {}
        product['id'] = id
        product['title'] = title
        self.products.append(product)
        return True

    def updateProduct(self, id, title):
        # TODO: return false if the product id does not exist
        if not self.findProductById(id):
            return False
        updproduct = {}
        for product in self.products:
            if product['id'] == id:
                updproduct = product
        updproduct['title'] = title
        return True

    def deleteProduct(self, id):
        # TODO: return false if the product does not exist
        if not self.findProductById(id):
            return False
        updproduct = {}
        for product in self.products:
            if product['id'] == id:
                updproduct = product
        del updproduct
        return True

    def findProductById(self, id):
        # product or null
        for product in self.products:
            if product['id'] == id:
                return product
        return None

    def findProductByTitle(self, title):
        # product or null
        for product in self.products:
            if product['title'] == title:
                return product
        return None

productManager = ProductManager()

import json
def productManagement(operations):
    # Calls corresponding methods of productManager based on the input
    ans = []
    for operation in operations:
        if operation[0] == 'createProduct':
            res = productManager.createProduct(operation[1], operation[2])
            ans.append(json.dumps(res))
        if operation[0] == 'updateProduct':
            res = productManager.updateProduct(operation[1], operation[2])
            ans.append(json.dumps(res))
        if operation[0] == 'deleteProduct':
            res = productManager.deleteProduct(operation[1])
            ans.append(json.dumps(res))
        if operation[0] == 'findProductById':
            res = productManager.findProductById(operation[1])
            if res == None:
                ans.append('null')
            else:
                ans.append(json.dumps(res, separators=(',', ':')))
        if operation[0] == 'findProductByTitle':
            res = productManager.findProductByTitle(operation[1])
            if res == None:
                ans.append('null')
            else:
                ans.append(json.dumps(res, separators=(',', ':')))
    return ans
