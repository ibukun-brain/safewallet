# Create your views here.
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from home.models import Wallet

# Wallet.objects.create(
#     user = user,
#     balance = new_wallet["data"]["availableBalance"],
#     account_name = new_wallet["data"]["accountName"],
#     account_number = new_wallet["data"]["accountNumber"],
#     bank = new_wallet["data"]["bank"],
#     phone_number = new_wallet["data"]["phoneNumber"],
#     password = fernet.encrypt(new_wallet["data"]["password"].encode())
# )
# messages.success(request, "Account verified, wallet successfully created")
# return reverse_lazy("accounts:dashboard")

# else:
            # messages.error(request, new_wallet["response"]["message"])
        