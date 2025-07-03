from django.shortcuts import render
from .models import Book
# Create your views here.

def book__list(request):
  books = Book.objects.all()
  return render(request, 'library/book_list.html', {'books':books})
