from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.db.models import Avg, Min, Max
from .models import Book

# Create your views here.
def index(request):
    doge = Book.objects.all().order_by("-rating")
    number_book = doge.count()
    avg_rating = doge.aggregate(Avg("rating"))
    return render(request, "book_outlet/index.html", {
        "books":doge,
        "number_book":number_book,
        "average_rating":avg_rating
    })

def book_detail(request, slug):
    # try:
    #     doge = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    doge = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html", {
        "title": doge.title,
        "rating": doge.rating,
        "author": doge.author,
        "trending": doge.isTrending
    })