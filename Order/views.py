from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from ShoppingCart.shopping import ShoppingCart
from .models import Order, OrderLine

# Create your views here.


def send_email(**kwargs):
    subject = 'Thanks for your order'
    message = render_to_string('order.html',
                               {'order': kwargs.get('order'),
                                'order_lines': kwargs.get('order_lines'),
                                'name': kwargs.get('name')})
    message_text = strip_tags(message)
    from_email = 'gonzalezreyesadriano@gmail.com'
    recipient_list = 'gonzalezreyesadriano2507@gmail.com'
    send_mail(subject, message_text, from_email, [recipient_list], fail_silently=False, html_message=message)


@login_required(login_url='login/')
def process_order(request):
    order = Order.objects.create(user=request.user)
    cart = ShoppingCart(request)
    order_lines = list()
    for key, value in cart.cart.items():
        order_lines.append(
            OrderLine(
                product_id=key,
                quantity=value['quantity'],
                user=request.user,
                order=order,
            )
        )
    OrderLine.objects.bulk_create(order_lines)

    send_email(
        order=order,
        order_lines=order_lines,
        name=request.user.username,
        email=request.user.email
    )

    messages.success(request, 'Your order has been successfully sent')
    return redirect('Store')
