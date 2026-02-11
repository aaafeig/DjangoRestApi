from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrModerator(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

        if request.user.groups.filter(name="moderators").exists():
            return request.method in SAFE_METHODS or request.method in ["PUT", "PATCH"]

        return obj.owner == request.user
