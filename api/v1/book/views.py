# from rest_framework.response import Response
# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from .permissions import IsOwnerBook, IsOwnerAuthor
# from django_filters.rest_framework import DjangoFilterBackend
# # from .models import
# from .serializers import (
#     BookListSerializer,
#     BookCreateSerializer,
#     BookDetailSerializer,
#     BookUpdateSerializer,
#     AuthorListSerializer,
#     AuthorDetailSerializer,
#     AuthorCreateSerializer,
#     AuthorUpdateSerializer,
#     UserProfileSerializer,
# )
# from .services.filters import BookFilter, AuthorFilter
#
#
# # The book's view
#
# # Create
# class BookCreateView(generics.CreateAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Book.objects.all()
#     serializer_class = BookCreateSerializer
#
#     def post(self, request, *args, **kwargs):
#         return super(BookCreateView, self).post(request, *args, **kwargs)
#
#
# # Read
# class BookDetailView(generics.RetrieveAPIView):
#     permission_classes = [IsAuthenticated, IsOwnerBook]
#     queryset = Book.objects.all()
#     serializer_class = BookDetailSerializer
#     lookup_field = 'pk'
#
#
# # Update
# class BookUpdate(generics.UpdateAPIView):
#     permission_classes = [IsAuthenticated, IsOwnerBook]
#     queryset = Book.objects.all()
#     serializer_class = BookUpdateSerializer
#     lookup_field = 'pk'
#
#     def get(self, request, pk):
#         book = Book.objects.get(id=pk)
#         serializer = BookUpdateSerializer(book, many=False)
#         return Response(serializer.data)
#
#
# # Delete
# class BookDelete(generics.DestroyAPIView):
#     permission_classes = [IsAuthenticated, IsOwnerBook, ]
#     queryset = Book.objects.all()
#     lookup_field = 'pk'
#
#
# # The list all books
# class BookListView(generics.ListAPIView):
#     permission_classes = [IsAuthenticated, IsOwnerBook, ]
#     queryset = Book.objects.all()
#     serializer_class = BookListSerializer
#     filter_backends = [DjangoFilterBackend, ]
#     filterset_class = BookFilter
#
#     def get_queryset(self):
#         # after get all products on DB it will be filtered by its owner and return the queryset
#         user_queryset = self.queryset.filter(user=self.request.user)
#         return user_queryset
#
#
# # The author's view
#
# # Create
# class AuthorCreateView(generics.CreateAPIView):
#     permission_classes = [IsAuthenticated, ]
#     queryset = Author.objects.all()
#     serializer_class = AuthorCreateSerializer
#
#     def post(self, request, *args, **kwargs):
#         return super(AuthorCreateView, self).post(request, *args, **kwargs)
#
#
# # Read
# class AuthorDetailView(generics.RetrieveAPIView):
#     permission_classes = [IsAuthenticated, IsOwnerAuthor, ]
#     queryset = Author.objects.all()
#     serializer_class = AuthorDetailSerializer
#     lookup_field = 'pk'
#
#
# # Update
# class AuthorUpdate(generics.UpdateAPIView):
#     permission_classes = [IsAuthenticated, IsOwnerAuthor, ]
#     queryset = Author.objects.all()
#     serializer_class = AuthorUpdateSerializer
#     lookup_field = 'pk'
#
#     def get(self, request, pk):
#         author = Author.objects.get(id=pk)
#         serializer = AuthorUpdateSerializer(author, many=False)
#         return Response(serializer.data)
#
#
# # Delete
# class AuthorDelete(generics.DestroyAPIView):
#     permission_classes = [IsAuthenticated, IsOwnerAuthor, ]
#     queryset = Author.objects.all()
#     lookup_field = 'pk'
#
#
# # The list all authors
# class AuthorListView(generics.ListAPIView):
#     permission_classes = [IsAuthenticated, IsOwnerAuthor, ]
#     queryset = Author.objects.all()
#     serializer_class = AuthorListSerializer
#     filter_backends = [DjangoFilterBackend, ]
#     filterset_class = AuthorFilter
#
#     def get_queryset(self):
#         # after get all products on DB it will be filtered by its owner and return the queryset
#         user_queryset = self.queryset.filter(user=self.request.user)
#         return user_queryset
#
#
# class CreateProfileView(generics.CreateAPIView):
#     permission_classes = [AllowAny, ]
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer
#
#     def post(self, request, *args, **kwargs):
#         return super(CreateProfileView, self).post(request, *args, **kwargs)

