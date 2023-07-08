import uuid
import auto_prefetch

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from wallet.utils.choices import Gender
from wallet.utils.media import image_upload_path, default_profile_image
from wallet.utils.managers import CustomUserManager
from wallet.utils.models import TimeBasedModel


class CustomUser(TimeBasedModel, AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "mobile_no"]

    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    uid = models.UUIDField(default=uuid.uuid4)
    email = models.EmailField(verbose_name="email address", unique=True)
    mobile_no = models.CharField(
        max_length=11,
        unique=True,
        error_messages={
            "unique": ("A user with that Mobile Number already exists."),
        }
    )
    date_joined = models.DateTimeField(default=timezone.now)
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
    is_active = models.BooleanField(default=True)
    verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = CustomUserManager()

    class Meta(auto_prefetch.Model.Meta):
        verbose_name = "User"
        verbose_name_plural = "Users"

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    @property
    def image_url(self):

        if self.profile_pic:
            return self.profile_pic.url

        return f"{settings.MEDIA_URL}/default/user-default.png"
