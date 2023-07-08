from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

# from allauth.account.signals import user_signed_up

from home.tasks import create_user_wallet_after_signup_task

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_wallet_after_signup(sender, instance, created, **kwargs):
    if created:
        account_name = instance.get_full_name()
        email = instance.email
        mobile_no = instance.mobile_no
        create_user_wallet_after_signup_task.delay(
            account_name,
            email=email,
            mobile_no=mobile_no
        )

# @receiver(user_signed_up, sender=CustomUser)
# def create_user_wallet_after_signup(request, user, **kwargs):
#     create_user_wallet_after_signup_task.delay(request, user, **kwargs)
    # print(user)
    # print(kwargs)
    # created_user = CustomUser.objects.get(email=user)
    # print('user sucessfully created')
    # wallet = WalletAPI()
    # new_user_wallet = wallet.create_user_wallet(
    #     account_name=created_user.get_full_name(),
    #     email=created_user.email,
    #     mobilenumber=created_user.mobile_no,
    #     country="NG",
    #     bank_code="035",
    # )
    # new_user_wallet = create_user_wallet_after_signup_task.delay()
    # if new_user_wallet["status"] == "success":
    #     Wallet.objects.create(
    #         user=created_user,
    #         account_preference=new_user_wallet["data"]["account_reference"],
    #         account_name=created_user.get_full_name(),
    #         account_number=new_user_wallet["data"]["nuban"],
    #         bank=new_user_wallet["data"]["bank_name"],
    #     )
