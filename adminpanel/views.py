from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .services.permissions import AdminAccess


class IndexRedirectView(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('adminpanel:index')


class IndexView(AdminAccess, generic.TemplateView):
    template_name = 'adminpanel/index.html'


class ProfileView(AdminAccess, generic.TemplateView):
    template_name = 'adminpanel/profile.html'


class DashboardView(AdminAccess, generic.TemplateView):
    template_name = 'adminpanel/dashboard.html'


class TablesView(AdminAccess, generic.TemplateView):
    template_name = 'adminpanel/tables.html'
