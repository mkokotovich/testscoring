from rest_framework import permissions

class IsOwnerPermission(permissions.BasePermission):
    """
    Object-level permission to only allow updating objects the user is owner for
    """
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user or request.user.is_superuser


class IsTestOwnerPermission(permissions.BasePermission):
    """
    Object-level permission to only allow updating Items for which the user
    is the owner of the Item's test
    """
    def has_object_permission(self, request, view, obj):
        return obj.test.owner == request.user or request.user.is_superuser
