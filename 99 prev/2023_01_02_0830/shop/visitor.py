class Visitor:
    def __init__(self, request):
        # when Visitor is init, it receives a request obj
        # though this obj, it has access to the 'Session' data
        self.request = request

        if "visitor" not in request.session:
            request.session["visitor"] = {
                "shoppingcart": []  # list of product id's
            }

        self.shopping_cart_product_ids = request.session["visitor"]["shoppingcart"]

    def get_shopping_cart_item_count(self):
        return len(self.shopping_cart_product_ids)

    def add_product_to_shopping_cart(self, product_id):
        self.shopping_cart_product_ids.append(product_id)
        self.request.session.modified = True
