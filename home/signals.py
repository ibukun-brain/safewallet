from django.dispatch import receiver
from allauth.account.signals import user_signed_up

from accounts.models import CustomUser
from home.models import Wallet

from wallet.utils.api import WalletAPI


@receiver(user_signed_up, sender=CustomUser)
def create_user_wallet_after_signup(self, request, user, **kwargs):
    print(user)
    print(request)
    print('user sucessfully created')
    wallet = WalletAPI()
    new_user_wallet = wallet.create_user_wallet(
        account_name=request.user.get_full_name(),
        email=request.user.email,
        mobilenumber=request.user.mobile_no,
        country="NG"
    )
    if new_user_wallet["status"] == "success":
        Wallet.objects.create(
            user=request.user,
            account_preference=new_user_wallet["data"]["account_preference"],
            account_name=request.user.get_full_name(),
            account_number=new_user_wallet["data"]["nuban"],
            bank=new_user_wallet["data"]["bank_name"],
        )
