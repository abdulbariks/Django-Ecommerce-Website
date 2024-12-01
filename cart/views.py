from django.views  import generic
from django.shortcuts import get_list_or_404, redirect

from .carts import Card
from product.models import Product

class AddToCart(generic.View):
    def post(self, request, *args, **kwargs):
        product_id = kwargs['product_id']
        product = Product.objects.get(id=product_id)
        # product = get_list_or_404(Product, id=kwargs.get('product_id'))
        cart = Card(self.request)
        cart.update(product.id, 1)
        return redirect('cart')
    
    
class CartItems(generic.TemplateView):
    template_name = 'cart/cart.html'