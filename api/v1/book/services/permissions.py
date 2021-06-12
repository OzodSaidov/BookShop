from rest_framework import permissions
from rest_framework.generics import get_object_or_404


class IsOwnerBook(permissions.BasePermission):

    def has_object_permission(self, request, view, book):
        return request.user == book.user


class IsOwnerAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, author):
        return request.user == author.user
