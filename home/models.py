import uuid
from decimal import Decimal

import auto_prefetch

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from wallet.utils.models import TimeBasedModel

User = get_user_model()


class Wallet(TimeBasedModel):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    user = auto_prefetch.OneToOneField(
        "accounts.CustomUser",
        on_delete=models.CASCADE
    )
    account_name = models.CharField(max_length=250)
    account_number = models.CharField(max_length=10)
    account_preference = models.CharField(max_length=50)
    balance = models.DecimalField(
        decimal_places=2,
        max_digits=11,
        default=0.00,
        validators=[MinValueValidator(Decimal('0.00'))]
    )
    bank = models.CharField(max_length=20)
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}'s wallet"
