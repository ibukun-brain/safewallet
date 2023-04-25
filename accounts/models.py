import uuid
import auto_prefetch

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from wallet.utils.choices import Gender
from wallet.utils.media import image_upload_path, default_profile_image
from wallet.utils.managers import CustomUserManager


class CustomUser(AbstractUser):
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]

    uid = models.UUIDField(default=uuid.uuid4)
    email = models.EmailField(verbose_name="email address", unique=True)
    mobile_no = models.CharField(max_length=11, null=True, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=15, choices=Gender.choices, null=True, blank=True
    )
    profile_pic = models.ImageField(
        upload_to=image_upload_path,
        blank=True,
        verbose_name="Profile Picture",
        null=True,
        default=default_profile_image
    )
    verified = models.BooleanField(default=False)
    objects = CustomUserManager()
    prefetch_manager = auto_prefetch.Manager()

    def __str__(self):
        return self.get_full_name() or self.email

    @property
    def image_url(self):

        if self.profile_pic:
            return self.profile_pic.url

        return f"{settings.MEDIA_URL}/default/user-default.png"
