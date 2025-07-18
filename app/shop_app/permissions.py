from datetime import datetime
from rest_framework.permissions import BasePermission

# Разрешения на уровне объектов в DRF
# Разрешение на изменение объекта только для его владельца:
# has_object_permission: Позволяет всем пользователям просматривать объект,
# но изменять его может только владелец (obj.owner == request.user).


class IsOwnerOrReadOnly(BasePermission):
    """
    Разрешает редактирование объектов только их владельцам, остальным - только чтение.
    """

    def has_object_permission(self, request, view, obj):    # Разрешения
        # Все пользователи могут просматривать
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Только владелец может изменять объект
        return obj.owner == request.user


class IsAdminOrOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Все пользователи могут просматривать
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Только администратор или владелец может изменять объект
        return request.user.is_staff or obj.owner == request.user


class IsWorkHour(BasePermission):

    def has_object_permission(self, request, view, obj):
        current_hour = datetime.now().hour
        return 9 <= current_hour < 18   # basa dannyh dostupno tol'ko do 18 chasow
