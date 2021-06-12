from django.urls import path, include

app_name = 'api_v1'
urlpatterns = [
    path('book/', include('api.v1.book.urls')),
]
