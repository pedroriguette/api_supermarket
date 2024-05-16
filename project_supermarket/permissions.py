from rest_framework import permissions


class GlobalDefaultPermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):
        model_permission = self.get_model(
            request.method,
            view=view,
        )

        if not model_permission:
            return False

        return request.user.has_perm(model_permission)

    def get_model(self, method, view):
        try:
            model_name = view.queryset.model._meta.model_name
            app_label = view.queryset.model._meta.app_label
            actions = self.actions_sufix(method)
            return f'{app_label}.{actions}_{model_name}'
        except AttributeError:
            return False

    def actions_sufix(self, method):
        method_action = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            'HEAD': 'view',
            'OPTIONS': 'view',
        }

        return method_action.get(method, '')
