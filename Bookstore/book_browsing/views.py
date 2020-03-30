from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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


def viewPage(request):
    queryString = request.path
    pageName = queryString.replace('/', '').title()
    results = BookInfo.objects.filter(Q(genre=pageName)).order_by('bookName')
    page = request.GET.get('page', 1)
    paginator = Paginator(results, 8)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    return render(request, 'book.html', {'books': books, "title": pageName, "count": results.count()})


def fantacy(request):
    return viewPage(request)


def romance(request):
    return viewPage(request)


def fiction(request):
    return viewPage(request)


def history(request):
    return viewPage(request)


def thriller(request):
    return viewPage(request)


def newRelease(request):
    template = 'new_release.html',
    return render(request, template)


def topSeller(request):
    template = 'top_sellers.html',
    return render(request, template)
