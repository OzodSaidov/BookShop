# from django.urls import path
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
#
# from . import views

# urlpatterns = [
# path('books/', views.BookListView.as_view(), name='books'),
# path('books/create/', views.BookCreateView.as_view(), name='create-book'),
# path('books/<int:pk>/', views.BookDetailView.as_view(), name='detail-book'),
# path('update-book/<int:pk>/', views.BookUpdate.as_view(), name='update-book'),
# path('delete-book/<int:pk>/', views.BookDelete.as_view(), name='delete-book'),
# path('author/', views.AuthorListView.as_view(), name='author'),
# path('create-author/', views.AuthorCreateView.as_view(), name='create-author'),
# path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='detail-author'),
# path('update-author/<int:pk>/', views.AuthorUpdate.as_view(), name='update-author'),
# path('delete-author/<int:pk>/', views.AuthorDelete.as_view(), name='delete-author'),
# path('create-profile/', views.CreateProfileView.as_view(), name='create-profile'),
# ]

from django.urls import path, include

urlpatterns = [
]
