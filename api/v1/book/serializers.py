# from django.contrib.auth.models import User
# from rest_framework import serializers
# # from .models import Book, Author, UserProfile
#
#
# # Book's Serializers
#
# class BookCreateSerializer(serializers.ModelSerializer):
#     user = serializers.HiddenField(default=serializers.CurrentUserDefault())
#
#     class Meta:
#         model = Book
#         fields = '__all__'
#         # exclude = ('user',)
#
#     def to_representation(self, instance):
#         data = super(BookCreateSerializer, self).to_representation(instance)
#         data['author'] = instance.author.name
#         return data
#
#
# class BookDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = '__all__'
#
#     """front ga author_id va user_id ni emas author_name va user_name ni return qiladi"""
#
#     def to_representation(self, instance):
#         data = super(BookDetailSerializer, self).to_representation(instance)
#         data['author'] = instance.author.name
#         data['user'] = instance.user.username
#         return data
#
#
# class BookUpdateSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Book
#         fields = (
#             'id',
#             'title',
#             'genre',
#             'language',
#             'author',
#             'publisher',
#         )
#
#     """front ga author_id va user_id ni emas author_name va user_name ni return qiladi"""
#
#     def to_representation(self, instance):
#         data = super(BookUpdateSerializer, self).to_representation(instance)
#         data['author'] = instance.author.name
#         data['user'] = instance.user.username
#         return data
#
#
# class BookListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = (
#             'id',
#             'title',
#             'genre',
#             'author',
#         )
#
#     """front ga author_id ni emas author_name ni return qiladi"""
#
#     def to_representation(self, instance):
#         data = super(BookListSerializer, self).to_representation(instance)
#         data['author'] = instance.author.name
#         return data
#
#
# # Author's Serializers
#
# class AuthorCreateSerializer(serializers.ModelSerializer):
#     user = serializers.HiddenField(default=serializers.CurrentUserDefault())
#
#     class Meta:
#         model = Author
#         fields = '__all__'
#         # exclude = ('user',)
#
#
# class AuthorDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = '__all__'
#
#     def to_representation(self, instance):
#         data = super(AuthorDetailSerializer, self).to_representation(instance)
#         data['user'] = instance.user.username
#         return data
#
#
# class AuthorUpdateSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Author
#         fields = (
#             'id',
#             'name',
#             'email',
#             'address',
#             'phone',
#         )
#
#     def to_representation(self, instance):
#         data = super(AuthorUpdateSerializer, self).to_representation(instance)
#         data['user'] = instance.user.username
#         return data
#
#
# class AuthorListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = (
#             'id',
#             'name',
#             'address',
#         )
#
#
# class UserProfileSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(source='user.username')
#     password = serializers.CharField(source='user.password',
#                                      style={'input_type': 'password', 'placeholder': 'Password'}, write_only=True)
#
#     class Meta:
#         model = UserProfile
#         fields = (
#             'username',
#             'password',
#             'status',
#             'first_name',
#             'last_name',
#             'email',
#         )
#
#     def create(self, validated_data):
#         # User create qilish
#         user = User(username=validated_data['user']['username'])
#         user.set_password(validated_data['user']['password'])
#         user.save()
#
#         profile = UserProfile(user=user)
#         profile.first_name = validated_data['first_name']
#         profile.last_name = validated_data['last_name']
#         profile.email = validated_data['email']
#         profile.status = validated_data['status']
#         profile.save()
#         return profile

