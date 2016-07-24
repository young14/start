# Create your views here.
from blog.models import Auther, Book
from django.shortcuts import render_to_response


def show_authers(request):
    authers = Auther.objects.all()
    books = Book.objects.all()
    return render_to_response('index.html',{'authers':authers, 'books':books})
