from django.dispatch import receiver
from allauth.account.signals import user_signed_up

from accounts.models import CustomUser
from home.models import Wallet

from wallet.utils.api import WalletAPI


@receiver(user_signed_up, sender=CustomUser)
def create_user_wallet_after_signup(request, user, **kwargs):
    print(user)
    print(kwargs)
    created_user = CustomUser.objects.get(email=user)
    print('user sucessfully created')
    wallet = WalletAPI()
    new_user_wallet = wallet.create_user_wallet(
        account_name=created_user.get_full_name(),
        email=created_user.email,
        mobilenumber=created_user.mobile_no,
        country="NG",
        bank_code="035",
    )
    if new_user_wallet["status"] == "success":
        Wallet.objects.create(
            user=created_user,
            account_preference=new_user_wallet["data"]["account_reference"],
            account_name=created_user.get_full_name(),
            account_number=new_user_wallet["data"]["nuban"],
            bank=new_user_wallet["data"]["bank_name"],
        )
