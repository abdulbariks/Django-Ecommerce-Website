from .carts import Card

def cart(request):
    return {"cart": Card(request)}