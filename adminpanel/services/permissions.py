from django.contrib.auth.mixins import LoginRequiredMixin


class AdminAccess(LoginRequiredMixin):
    permission_denied_message = 'Access is denied!'
    raise_exception = False

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, args, kwargs)
