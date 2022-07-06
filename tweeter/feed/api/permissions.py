
from rest_framework import permissions


class CreateOnlyAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            if request.user.is_authenticated:
                return True
            else:
                return False
        else:
            return True
