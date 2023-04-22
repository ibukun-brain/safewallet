from django.contrib.auth.mixins import AccessMixin
from django.contrib import messages

from django.shortcuts import redirect

class IsUserVerifiedMixin(AccessMixin):
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.verified:
            messages.error(request, "Your account hasn't been verified")
            return redirect('account_wallet:verify_user')
        return super(IsSelfandLoginRequiredMixin, self).dispatch(request, *args, **kwargs)