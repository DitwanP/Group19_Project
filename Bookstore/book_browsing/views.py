import books as books
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template import RequestContext
from products.models import books


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


def order(request):
    template = "order.html",
    return render(request, template)


def newBook(request):
    template = 'new_book.html',
    return render(request, template)


def cart(request):
    template = 'order_summary.html',
    return render(request, template)


def search(request):
    query = request.GET.get('q')
    bookResult = None
    results = None
    count = None
    try:
        query = str(query)
    except ValueError:
        query = None

    if query:
        results = books.objects.filter(Q(name=query) | Q(genre=query))
        count = results.count()

    if results:
        page = request.GET.get('page', 1)
        paginator = Paginator(results, 8)
        try:
            bookResult = paginator.page(page)
        except PageNotAnInteger:
            bookResult = paginator.page(1)
        except EmptyPage:
            bookResult = paginator.page(paginator.num_pages)

    return render(request, 'search.html', {"books": bookResult, "count": count})


def viewPage(request):
    queryString = request.path
    pageName = queryString.replace('/', '').title()
    results = books.objects.filter(Q(genre=pageName)).order_by('name')
    page = request.GET.get('page', 1)
    paginator = Paginator(results, 8)
    try:
        bookResult = paginator.page(page)
    except PageNotAnInteger:
        bookResult = paginator.page(1)
    except EmptyPage:
        bookResult = paginator.page(paginator.num_pages)
    return render(request, 'book.html', {'books': bookResult, "title": pageName, "count": results.count()})


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
    results = books.objects.order_by('releasedDate').reverse()[:10]
    page = request.GET.get('page', 1)
    paginator = Paginator(results, 8)
    try:
        bookResult = paginator.page(page)
    except PageNotAnInteger:
        bookResult = paginator.page(1)
    except EmptyPage:
        bookResult = paginator.page(paginator.num_pages)
    return render(request, 'new_release.html', {'books': bookResult, "title": "New Release", "count": results.count()})


def topSeller(request):
    template = 'top_sellers.html',
    return render(request, template)


def filterData(request):
    sortType = request.GET.get("sort_type")
    queryString = request.GET.get("page_url")

    pageName = queryString.replace('/', '').title()
    if sortType == 'releasedDate':
        results = books.objects.filter(Q(genre=pageName)).order_by('releasedDate').reverse()
    elif sortType == 'price':
        results = books.objects.filter(Q(genre=pageName)).order_by('price').reverse()
    elif sortType == 'pricelowtohigh':
        results = books.objects.filter(Q(genre=pageName)).order_by('price')
    elif sortType == 'atoz':
        results = books.objects.filter(Q(genre=pageName)).order_by('name')
    else:
        results = books.objects.filter(Q(genre=pageName)).order_by(sortType)

    page = request.GET.get('page', 1)
    paginator = Paginator(results, 8)
    try:
        bookResult = paginator.page(page)
    except PageNotAnInteger:
        bookResult = paginator.page(1)
    except EmptyPage:
        bookResult = paginator.page(paginator.num_pages)

    return render(request, 'ajax/book.html', {'books': bookResult})


def filterReleasedData(request):
    sortType = request.GET.get("sort_type")
    if sortType == 'releasedDate':
        results = books.objects.all().order_by('releasedDate').reverse()
    elif sortType == 'price':
        results = books.objects.all().order_by('price', 'releasedDate').reverse()
    elif sortType == 'pricelowtohigh':
        results = books.objects.all().order_by('price', 'releasedDate')
    elif sortType == 'atoz':
        results = books.objects.all().order_by('name', 'releasedDate')
    else:
        results = books.objects.all().order_by(sortType, 'releasedDate')

    page = request.GET.get('page', 1)
    paginator = Paginator(results, 8)
    try:
        bookResult = paginator.page(page)
    except PageNotAnInteger:
        bookResult = paginator.page(1)
    except EmptyPage:
        bookResult = paginator.page(paginator.num_pages)

    return render(request, 'ajax/book.html', {'books': bookResult})
