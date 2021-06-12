from django.urls import path, include
from .views import IndexView, BooksView, AuthorsView

app_name = 'book'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('books/', BooksView.as_view(), name='books'),
]
