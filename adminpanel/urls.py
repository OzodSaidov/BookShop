from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import IndexRedirectView, \
    IndexView, ProfileView, DashboardView, TablesView

app_name = 'adminpanel'
urlpatterns = [
    path('', IndexRedirectView.as_view(), name='index_redirect'),
    path('index/', IndexView.as_view(), name='index'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('tables/', TablesView.as_view(), name='tables'),
    path('login/', LoginView.as_view(template_name='admin/login.html',
                                     redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
