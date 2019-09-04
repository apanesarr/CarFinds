from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class IsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        message = "You must be authenticated"
        is_it = bool(request.user)
        if is_it:
            return is_it
        else:
            raise PermissionDenied(detail=message)