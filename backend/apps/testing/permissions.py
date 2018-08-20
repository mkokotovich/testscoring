from rest_framework import permissions

class IsOwnerPermission(permissions.BasePermission):
    """
    Object-level permission to only allow updating objects the user is owner for
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user or request.user.is_admin
