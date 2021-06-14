from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from .views import IndexRedirectView, IndexView

app_name = 'adminpanel'
urlpatterns = [
    path('', IndexRedirectView.as_view(), name='index_redirect'),
    path('index/', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(template_name='admin-panel/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
