"""
With Jet Smart Cart the more items you buy, the more you save. The algorithm behind how this works is a bit complicated, and since it's your first day at Jet you decide to ask one of your co-workers for more information. In return, you offer to implement a new cart update algorithm for them. The update algorithm works like this:

Whenever a new customer visits jet.com, their shopping cart is initially empty. Once the customer starts shopping, the cart can receive any of the following requests:

add : <item_name>: the <item_name> item was added to the cart;
remove : <item_name>: all <item_name> items were removed from the cart;
quantity_upd : <item_name> : <value>: the <item_name> quantity in the cart was changed by <value>, which is an integer in the format +a or -a;
checkout: the customer has paid and the cart is now empty.
Given a list of requests in the formats described above, return the state of the cart after they have been processed. Elements in the cart should be returned in the order they were received.

Example

For

requests = ["add : milk",
            "add : pickles",
            "remove : milk",
            "add : milk",
            "quantity_upd : pickles : +4"]
the output should be
shoppingCart(requests) = ["pickles : 5", "milk : 1"];

For

requests = ["add : rock",
            "add : paper",
            "add : scissors",
            "checkout",
            "add : golden medal"]
the output should be
shoppingCart(requests) = ["golden medal : 1"].
"""


from collections import OrderedDict, defaultdict

class OrderedDefaultDict(OrderedDict, defaultdict):
    def __init__(self, default_factory=None, *args, **kwargs):
        #in python3 you can omit the args to super
        super(OrderedDefaultDict, self).__init__(*args, **kwargs)
        self.default_factory = default_factory

def parse_request(request):
    parts = request.split(' : ')
    if len(parts) == 1:
        return None
    elif len(parts) == 2:
        if parts[0] == 'add':
            return [parts[1], 1]
        else:
            return [parts[1], 0]
    else:
        if '+' in parts[2]:
            return [parts[1], int(parts[2][1:])]
        else:
            return [parts[1], -int(parts[2][1:])]

def shoppingCart(requests):
    cart = OrderedDefaultDict(int)
    for request in requests:
        parsed = parse_request(request)
        if parsed:
            if parsed[1] == 0:
                cart[parsed[0]] = 0
            else:
                cart[parsed[0]] += parsed[1]
            if cart[parsed[0]] == 0:
                cart.pop(parsed[0])
        else:
            cart = OrderedDefaultDict(int)
    return [" : ".join([key, str(value)]) for key, value in cart.iteritems()]

