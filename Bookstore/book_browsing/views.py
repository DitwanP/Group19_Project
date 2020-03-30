from django.db.models import Q
from django.shortcuts import render, get_object_or_404


# Create your views here.
from django.template import RequestContext

from book_details.models import BookInfo


def home(request):
    return render(request, 'index.html')


def account(request):
    template = "account.html",
    return render(request, template)


def checkout(request):
    template = "checkout.html",
    return render(request, template)


def login(request):
    template = "login.html",
    return render(request, template)


def book(request):
    template = "book.html",
    return render(request, template)


def about(request):
    template = "about.html",
    return render(request, template)


def contact(request):
    template = "contact.html",
    return render(request, template)


def blog(request):
    template = "blog.html",
    return render(request, template)


def salesOff(request):
    template = "sales_off.html",
    return render(request, template)


def blogDetails(request):
    template = "blog_details.html",
    return render(request, template)


def order(request):
    template = "order.html",
    return render(request, template)


def newBook(request):
    template = 'new_book.html',
    return render(request, template)


def cart(request):
    template = 'cart.html',
    return render(request, template)


def search(request):
    query = request.GET.get('q')
    results = None
    try:
        query = str(query)
    except ValueError:
        query = None

    if query:
        results = BookInfo.objects.filter(Q(bookName=query) | Q(genre=query))
    context = RequestContext(request)
    return render(request, 'search.html', {"results": results})

