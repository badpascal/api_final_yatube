from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS
)


class IsOwnerOrReadOnly(BasePermission):
    """Пермишен разрешающий автору всё, безопасные методы остальным."""

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or obj.author == request.user
