from django.contrib.auth.mixins import LoginRequiredMixin


class AdminAccess(LoginRequiredMixin):
    permission_denied_message = 'Access is denied!'
    raise_exception = False
