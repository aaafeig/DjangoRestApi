from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerOrModerator(BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if request.user.groups.filter(name="moderators").exists():
            if request.method in ["POST", "DELETE"]:
                return False
            return True

        return True

    def has_object_permission(self, request, view, obj):

        if request.user.groups.filter(name="moderators").exists():
            return request.method in SAFE_METHODS or request.method in ["PUT", "PATCH"]

        return obj.owner == request.user
