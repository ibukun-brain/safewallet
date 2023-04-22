from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin



class HideBalanceView(LoginRequiredMixin, generic.TemplateView):

    def post(self, request, *args, **kwargs):
        user_wallet = self.request.user.wallet
        user_wallet.is_hidden = True
        user_wallet.save()
        if self.request.htmx:
            context = {
               'hide_balance':True
            }
            return render(request, 'partials/_hide_or_show_balance.html', context)
       
        else:
            return redirect(reverse_lazy('home:dashboard'))
           

class ShowBalanceView(LoginRequiredMixin, generic.TemplateView):

    def post(self, request, *args, **kwargs):
        user_wallet = self.request.user.wallet
        user_wallet.is_hidden = False
        user_wallet.save()
        if self.request.htmx:
            context = {
                'hide_balance':False
            }

            return render(request, 'partials/_hide_or_show_balance.html', context)
       
        else:
            return redirect(reverse_lazy('home:dashboard'))


class AddMoneyView(LoginRequiredMixin, generic.TemplateView):
    
    def get(self, request, *args, **kwargs):
        context = {

        }
        if self.request.htmx:

            return render(request, 'partials/_add_money.html')
        
        return render(request, 'home/add_money.html')
    

class WalletView(LoginRequiredMixin, generic.TemplateView):

        
    def get(self, request, *args, **kwargs):
         
        if self.request.htmx:
             return render(request, 'partials/_wallet.html')

        return render(request, 'home/index.html')