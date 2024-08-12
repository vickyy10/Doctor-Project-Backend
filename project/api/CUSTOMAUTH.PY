from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request,):
        return super().has_permission(request)

