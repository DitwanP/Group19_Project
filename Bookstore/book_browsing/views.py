import books as books

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template import RequestContext

from accounts.models import Profile
from products.models import books
from shopping_cart.models import OrderItem, Order


def home(request):
    books_for_order = None
    user_order = None
    if request.user.is_active:
        user_profile = get_object_or_404(Profile, user=request.user)
        user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
        books_for_order = OrderItem.objects.all()[0:2]

    # Top Interest
    new_release = books.objects.order_by('releasedDate').reverse()[:15]
    on_sales = books.objects.all().order_by("name")[:15]
    feature_products = books.objects.filter(Q(category='Entertainment')).order_by("name")[:15]

    # Best Selling
    best_sellings = OrderItem.objects.all()

    # Book
    all_books = books.objects.all()

    # Science Fiction
    science_fiction_books = books.objects.filter(Q(genre="Science Fiction")).order_by('name')

    # History Book
    history_books = books.objects.filter(Q(genre="Science Fiction")).order_by('name')

    # Fantasy Book
    fantasy_books = books.objects.filter(Q(genre="Fantacy")).order_by('name')

    context = {'books_for_order': books_for_order, "user_order": user_order, "new_release": new_release, "on_sales": on_sales, "feature_products": feature_products, "best_sellings": best_sellings, "all_books": all_books, "science_fiction_books": science_fiction_books, "history_books": history_books, "fantasy_books": fantasy_books}
    return render(request, 'index.html', context)


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

    if pageName == "Fiction":
        pageName = "Science Fiction"

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


def fantasy(request):
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

    if pageName == "Fiction":
        pageName = "Science Fiction"

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


def getBookDetailsById(request):
    bookId = request.GET.get("book_id")
    bookObject = books.objects.get(pk=int(bookId))

    return render(request, 'ajax/book_details.html', {'book': bookObject})


def ajaxSubmit(request):
    print(request)
    return