from .permissions import IsStaffPermission
from rest_framework import permissions

class StaffEditorPermissionsMixins():
    
    permission_classes = [permissions.IsAuthenticated, IsStaffPermission]

#requette personaliser
class UserQuerySetMixin():
    user_field = 'user'
    def get_queryset(self, *args, **kwargs):
        
        qs = super().get_queryset(*args, **kwargs)
        query_data = {}
        query_data[self.user_field] = self.request.user
        return qs.filter(**query_data) #les deux etoile consiste a decompacter le dictionner au lieu d'avoir {'user':'donfack'} on a plus tot qs.filter(user=donfack)