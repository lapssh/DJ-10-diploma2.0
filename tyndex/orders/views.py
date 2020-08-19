from django.contrib import messages
from django.shortcuts import render, redirect

from accounts.models import Customer
from orders.models import Order, ProductsInOrder
from shop.models import Product


def show_cart_view(request):
    next_page = request.GET.get('next')
    context = {
        'next': next_page,
    }
    cart = request.session.get('cart', None)
    if cart:
        products = {}
        product_list = Product.objects.filter(
            pk__in=cart.keys()).values(
            'id', 'name', 'img', 'price', )
        for product in product_list:
            products[str(product['id'])] = product
            print(products, '\n')
        for key in cart.keys():
            cart[key]['product'] = products[key]
            print(cart[key]['product'], '\n')
        context['cart'] = cart
        context['products_count'] = len(cart)
        print(80 * '=')
        print(len(cart))
    return render(request, 'cart.html', context)


def add_to_cart(request):
    next_page = request.GET.get('next')
    if request.method == 'POST':
        product_pk = request.GET.get('product_id')
        if 'cart' not in request.session:
            request.session['cart'] = {}
        cart = request.session.get('cart')
        if product_pk in cart:
            cart[product_pk]['quantity'] += 1
        else:
            cart[product_pk] = {
                'quantity': 1,
            }
    request.session.modified = True
    return redirect(next_page)


def order_view(request):
    if request.method == 'POST':
        cart = request.session['cart']
        print('items: ', request.session.__dict__)
        customer_id_ = request.session['_auth_user_id']
        print('ID пользователя: ', request.session['_auth_user_id'])
        customer_pk = request.session['_auth_user_id']
        print(cart)
        customer_ = Customer.objects.get(user_id=customer_id_)
        print(customer_)

        cart = request.session['cart']

        if len(cart) > 0:
            order = Order.objects.create(customer=customer_)

            for key, value in cart.items():
                product = Product.objects.get(pk=key)
                quantity = value['quantity']
                ProductsInOrder.objects.create(order=order,
                                               product=product,
                                               quantity=quantity,
                                               )
            request.session['cart'] = {}
            request.session.modified = True

            messages.success(request,
                             f"Спасибо, {customer_}! Ваш заказ оформлен."
                             f"\nОжидайте доставку, наш курьер скоро с вами свяжется.")

    return redirect('show_cart')
