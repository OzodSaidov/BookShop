from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from .views import IndexView, AdminPanelView

app_name = 'adminpanel'
urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('adminpanel/', AdminPanelView.as_view(), name='cpanel'),
    path('login/', LoginView.as_view(template_name='admin-panel/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
