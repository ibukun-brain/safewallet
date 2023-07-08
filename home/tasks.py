from celery import shared_task

from wallet.utils.api import WalletAPI

from accounts.models import CustomUser

from home.models import Wallet


@shared_task
def create_user_wallet_after_signup_task(account_name, email, mobile_no):
    """Run background task to create a new wallet"""
    print('user sucessfully created')
    wallet = WalletAPI()
    new_user_wallet = wallet.create_user_wallet(
        account_name=account_name,
        email=email,
        mobilenumber=mobile_no,
        country="NG",
        bank_code="232",
    )
    print(new_user_wallet)
    if new_user_wallet["status"] == "success":
        user = CustomUser.objects.get(email=email)
        retrieve_user_va = wallet.retrieve_user_virtual_account_number(
            account_reference=new_user_wallet["data"]["account_reference"]
        )
        print(retrieve_user_va)
        wallet = Wallet.objects.create(
            user=user,
            account_reference=new_user_wallet["data"]["account_reference"],
            account_name=(
                new_user_wallet["data"]["account_name"]
                or user.get_full_name()
            ),
            nuban=new_user_wallet["data"]["nuban"],
            bank=new_user_wallet["data"]["bank_name"],
        )
        wallet.account_number = retrieve_user_va["data"]["static_account"]
        wallet.save()

# @shared_task
# def create_user_wallet_after_signup_task(user, request, **kwargs):
#     """Run background task to create a new wallet"""
#     print(user)
#     print(kwargs)
#     created_user = CustomUser.objects.get(email=user)
#     print('user sucessfully created')
#     wallet = WalletAPI()
#     new_user_wallet = wallet.create_user_wallet(
#         account_name=created_user.get_full_name(),
#         email=created_user.email,
#         mobilenumber=created_user.mobile_no,
#         country="NG",
#         bank_code="035",
#     )
#     new_user_wallet = create_user_wallet_after_signup_task.delay()
#     if new_user_wallet["status"] == "success":
#         Wallet.objects.create(
#             user=created_user,
#             account_preference=new_user_wallet["data"]["account_reference"],
#             account_name=created_user.get_full_name(),
#             account_number=new_user_wallet["data"]["nuban"],
#             bank=new_user_wallet["data"]["bank_name"],
#         )
