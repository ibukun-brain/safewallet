import random

from allauth.account.adapter import DefaultAccountAdapter

from accounts.models import CustomUser 


class CustomAccountAdapter(DefaultAccountAdapter):

    # def populate_username(self, request, user):
    #     custom_user = CustomUser.objects.get(email=user)
    #     first_name = custom_user.first_name
    #     last_name = custom_user.last_name
    #     print(self.generate_unique_username(
    #         [first_name, last_name, user, "user"]
    #     ))
    #     return self.generate_unique_username(
    #         [first_name, last_name, user, "user"]
    #     )

    

    def generate_unique_username(self, txts, regex=None):
        user = self.user
        random_name = f"{user}{random.random(1, 100)}"
        return super().generate_unique_username(random_name, regex)
