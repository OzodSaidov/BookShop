from django_filters import FilterSet, CharFilter
from book_rest.models import Book, Author


class BookFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    genre = CharFilter(field_name='genre', lookup_expr='icontains')
    author = CharFilter(field_name='author__name', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['title', 'genre', 'author']


class AuthorFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Author
        fields = ['name']