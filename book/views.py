from django.shortcuts import render
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'index.html'


class BooksView(generic.TemplateView):
    template_name = 'book/books.html'


class AuthorsView(generic.TemplateView):
    template_name = 'book/authors.html'
