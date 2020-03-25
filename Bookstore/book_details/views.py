from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo
from .models import BookAuthor
from django.views import generic

from products.models import *
# Create your views here.
#def bookView(request):
    #book = BookInfo.objects.get(bookName = 'Criss Cross')
    #author = BookAuthor.objects.filter(bookinfo__bookName = 'Criss Cross')
    #authorInfo = BookAuthor.objects.get(authorName = str(author[0]))
    #book_list = list()

    #book_list.append(book.bookName + "\n")
    #book_list.append(book.description + "\n")
    #book_list.append("Genre: " + book.genre + "\n")
    #book_list.append("Publisher: " + book.publisher + "\n")
    #book_list.append("Book Rating: " + str(book.averageRating) + "\n")
    #book_list.append("Author: " + authorInfo.authorName + "\n")
    #book_list.append("Bio: " + authorInfo.authorBio + "\n")

    
    #response_html = '<br>'.join(book_list)
    #return HttpResponse(response_html)
class bookDetailsView(generic.DetailView):
    template_name= "book_details.html"
    #model = BookInfo

    def get_context_data(self, **kwargs):
        context = super(bookDetailsView, self).get_context_data(**kwargs)
        book = Books.objects.get(pk=self.kwargs.get('pk'))
        context['book'] = Books.objects.get(pk=self.kwargs.get('pk'))
        context['author'] = book.author
        return context
        
    def get_queryset(self):
        return Books.objects.all()

    
class bookAuthorsView(generic.DetailView):
    template_name= "book_author.html"

    def get_context_data(self, **kwargs):
        context=super(bookAuthorsView, self).get_context_data(**kwargs)
        author = Authors.objects.get(pk=self.kwargs.get('pk'))
        context['author'] = author
        context['books'] = Books.objects.filter(author=author.authorName)
        return context
    
    def get_queryset(self):
        return BookAuthor.objects.all()
