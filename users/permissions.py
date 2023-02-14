from rest_framework import permissions


class UpdateAndDelete(permissions.BasePermission):    
    def has_object_permission(self, request, view, obj):  
        if request.user == obj or request.user.id == obj.user.id:
            return True      

        return False
    