from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import Profile
from products.models import books

from shopping_cart.extras import generate_order_id,  generate_save_id, transact, generate_client_token
from shopping_cart.models import OrderItem, Order, Transaction, SaveItem, Saved

import datetime
import stripe

stripe.api_key = "sk_test_4PDwRmxMmJFYdUbQHGMJz3zn003JF5ugKA"


def get_user_pending_order(request):
    # get order for the correct user
    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0

@login_required()
def increase_item_quantity(request, **kwargs):
    # get the user profile
    user_profile = get_object_or_404(Profile, user=request.user)

    # filter books by id
    book = books.objects.filter(id=kwargs.get('item_id', "")).first()

    # create orderItem of the selected book
    order_item, status = OrderItem.objects.get_or_create(book=book)
    order_item.quantity = order_item.quantity + 1
    order_item.price_in_cart = order_item.book.price * order_item.quantity
    order_item.save()

    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()

    books_for_order = OrderItem.objects.all().order_by('-book')
    sbooks = SaveItem.objects.all()

    context = {'user_order': user_order, 'books_for_order': books_for_order, 'sbooks': sbooks}

    return render(request,'shopping_cart/order_summary.html', context)

@login_required()
def decrease_item_quantity(request, **kwargs):
    # get the user profile
    user_profile = get_object_or_404(Profile, user=request.user)

    # filter books by id
    book = books.objects.filter(id=kwargs.get('item_id', "")).first()

    # create orderItem of the selected book
    order_item, status = OrderItem.objects.get_or_create(book=book)
    if order_item.quantity > 1:
        order_item.quantity = order_item.quantity - 1
        order_item.price_in_cart = order_item.book.price * order_item.quantity
        order_item.save()

    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()

    books_for_order = OrderItem.objects.all().order_by('-book')
    sbooks = SaveItem.objects.all()

    context = {'user_order': user_order, 'books_for_order': books_for_order, 'sbooks': sbooks}

    return render(request,'shopping_cart/order_summary.html', context)

@login_required()
def add_to_cart(request, **kwargs):
    # get the user profile
    user_profile = get_object_or_404(Profile, user=request.user)

    # filter books by id
    book = books.objects.filter(id=kwargs.get('item_id', "")).first()

    # create orderItem of the selected book
    order_item, status = OrderItem.objects.get_or_create(book=book, price_in_cart=book.price)

    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()

    books_for_order = OrderItem.objects.all().order_by('-book')
    sbooks = SaveItem.objects.all()

    context = {'user_order': user_order, 'books_for_order': books_for_order, 'sbooks': sbooks}

    # show confirmation message and redirect back to the same page
    messages.info(request, "Item has been added to cart")
    return redirect(request.META['HTTP_REFERER'])

@login_required()
def add_to_cart_from_detail(request, **kwargs):
    # get the user profile
    user_profile = get_object_or_404(Profile, user=request.user)

    # filter books by id
    book = books.objects.filter(id=kwargs.get('item_id', "")).first()

    book_id = kwargs.get('item_id')

    # create orderItem of the selected book
    order_item, status = OrderItem.objects.get_or_create(book=book, price_in_cart=book.price)

    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()

    books_for_order = OrderItem.objects.all().order_by('-book')
    sbooks = SaveItem.objects.all()

    context = {'user_order': user_order, 'books_for_order': books_for_order, 'sbooks': sbooks}

    # show confirmation message and redirect back to the same page
    messages.info(request, "Item has been added to cart")
    return redirect(reverse('book_details', args=(book_id,)))

@login_required()
def add_to_cart_from_saved(request, **kwargs):
    # get the user profile
    user_profile = get_object_or_404(Profile, user=request.user)

    # filter books by id
    book = books.objects.filter(id=kwargs.get('item_id', "")).first()

    # create orderItem of the selected book
    saved_to_cart, status = OrderItem.objects.get_or_create(book_id=kwargs.get('item_id'))
    saved_to_cart.is_saved_for_later = False
    saved_to_cart.save()

    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(saved_to_cart)
    if status:
        # generate a reference code
        user_order.ref_code = generate_save_id()
        user_order.save()

    sbooks = SaveItem.objects.all()

    books_for_order = OrderItem.objects.exclude(is_saved_for_later=True).order_by('-book')

    context = {'user_order': user_order, 'books_for_order': books_for_order, 'sbooks': sbooks}
    return render(request,'shopping_cart/order_summary.html', context)

@login_required()
def add_to_saved(request, **kwargs):

    # get the user profile
    user_profile = get_object_or_404(Profile, user=request.user)

    # filter books by id
    saved_book = books.objects.filter(id=kwargs.get('item_id', "")).first()

    # create orderItem of the selected book
    saved_item, status = SaveItem.objects.get_or_create(saved_book=saved_book)

    # create saved item that's associated with the user
    user_save, status = Saved.objects.get_or_create(owner=user_profile, is_saved_for_later=False)
    user_save.saved_items.add(saved_item)

    if status:
        # generate a reference code
        user_save.ref_code = generate_save_id()
        user_save.save()

    # show confirmation message and redirect back to the same page
    messages.info(request, "Item saved for later.")
    return redirect(reverse('products:product-list'))

@login_required()
def add_to_saved_from_cart(request, **kwargs):
    # get the user profile
    user_profile = get_object_or_404(Profile, user=request.user)

    # filter books by id
    saved_book = books.objects.filter(id=kwargs.get('item_id', "")).first()

    # create saveItem of the selected book
    saved_item, status = SaveItem.objects.get_or_create(saved_book=saved_book)

    # create saved that's associated with the user
    user_save, status = Saved.objects.get_or_create(owner=user_profile, is_saved_for_later=True)
    user_save.saved_items.add(saved_item)

    sbooks = SaveItem.objects.all()

    cart_to_saved, status = OrderItem.objects.get_or_create(book_id=kwargs.get('item_id'))
    cart_to_saved.is_saved_for_later = True
    cart_to_saved.save()

    books_for_order = OrderItem.objects.exclude(is_saved_for_later=True).order_by('-book')

    if status:
        # generate a reference code
        user_save.ref_code = generate_save_id()
        user_save.save()

    context = {'sbooks': sbooks, 'books_for_order': books_for_order}
    return render(request,'shopping_cart/order_summary.html', context)

@login_required()
def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()

    # get the user profile
    user_profile = get_object_or_404(Profile, user=request.user)

    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    sbooks = SaveItem.objects.all()
    books_for_order = OrderItem.objects.all()

    context = {'sbooks': sbooks, 'books_for_order': books_for_order, 'user_order': user_order}
    return redirect(request.META['HTTP_REFERER'])

@login_required()
def delete_from_saved(request, item_id):
    item_to_delete = SaveItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
    
    # get the user profile
    user_profile = get_object_or_404(Profile, user=request.user)

    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    sbooks = SaveItem.objects.all()
    books_for_order = OrderItem.objects.all()

    context = {'sbooks': sbooks, 'books_for_order': books_for_order, 'user_order': user_order}
    return render(request,'shopping_cart/order_summary.html', context)

@login_required()
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    
    # get the user profile
    user_profile = get_object_or_404(Profile, user=request.user)

    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    sbooks = SaveItem.objects.all()
    books_for_order = OrderItem.objects.all()

    context = {'sbooks': sbooks, 'books_for_order': books_for_order, 'user_order': user_order, 'order': existing_order}
    return render(request,'shopping_cart/order_summary.html', context)


@login_required()
def checkout(request, **kwargs):
    client_token = generate_client_token()
    existing_order = get_user_pending_order(request)
    publishKey = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == 'POST':
        token = request.POST.get('stripeToken', False)
        if token:
            try:
                charge = stripe.Charge.create(
                    amount=100*existing_order.get_cart_total(),
                    currency='usd',
                    description='Example charge',
                    source=token,
                )

                return redirect(reverse('shopping_cart:update_records',
                        kwargs={
                            'token': token
                        })
                    )
            except stripe.CardError as e:
                message.info(request, "Your card has been declined.")
        else:
            result = transact({
                'amount': existing_order.get_cart_total(),
                'payment_method_nonce': request.POST['payment_method_nonce'],
                'options': {
                    "submit_for_settlement": True
                }
            })

            if result.is_success or result.transaction:
                return redirect(reverse('shopping_cart:update_records',
                        kwargs={
                            'token': result.transaction.id
                        })
                    )
            else:
                for x in result.errors.deep_errors:
                    messages.info(request, x)
                return redirect(reverse('shopping_cart:checkout'))
            
    context = {
        'order': existing_order,
        'client_token': client_token,
        'STRIPE_PUBLISHABLE_KEY': publishKey
    }

    return render(request, 'shopping_cart/checkout.html', context)

def success(request, **kwargs):
    # a view signifying the transcation was successful
    return render(request, 'shopping_cart/purchase_success.html', {})
