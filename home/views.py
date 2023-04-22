from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from home.models import Wallet

# Create your views here.
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'home/index.html'

