from django.shortcuts import render
from .models import Book, Category
from django.db.models import Q

# Create your views here.


def book_list(request):
    query = request.GET.get('q')
    category_filter = request.GET.get('category')

    books = Book.objects.all()

    if query:
        books = books.filter(Q(title__icontains=query) |
                             Q(author__icontains=query))

    if category_filter:
        books = books.filter(category__name__icontains=category_filter)

    categories = Category.objects.all()
    return render(request, 'library/book_list.html', {
        'books': books,
        'categories': categories,
        'query': query,
        'category_filter': category_filter
    })
