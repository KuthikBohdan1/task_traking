from django.core.exceptions import PermissionDenied

class UserIsOwnerMixin(object):
    def dispatch(self, request, *args, **kwargs):
        isinstance = self.get_object()
        if isinstance.author != self.request.user:
            raise PermissionDenied
        
        return super().dispatch(request, *args, **kwargs)