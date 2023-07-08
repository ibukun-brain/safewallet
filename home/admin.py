from django.contrib import admin

from home.models import Wallet


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ['user', 'account_number', 'balance']
    autocomplete_fields = ['user']
    list_select_related = ['user']
    readonly_fields = ['uid']
    search_fields = ['user__email', 'account_number', 'bank']

