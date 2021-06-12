from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .services.permissions import AdminAccess


class IndexView(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('adminpanel:cpanel')


class AdminPanelView(AdminAccess, generic.TemplateView):
    template_name = 'admin-panel/index.html'
