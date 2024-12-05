from .carts import Card

def cart(request):
    cart = Card(request)
    if len(list(cart.cart.keys())) < 1:
        try:
            del cart.session[cart.coupon_id]
        except:
            ...
    return {"cart": Card(request)}