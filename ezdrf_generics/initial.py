# This module will makes you to define classbased views only.
# this will check for all view classes in app_name.views and
# add them to DB to check for permissions dynamically.
# wrote by mmzadfalah@gmail.com

def init_permissions():
    import inspect
    from importlib import import_module
    from django.conf import settings
    from ezdrf_generics.models import Permission
    permission_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE',]
    # get all permissions:
    permissions = Permission.objects.all()
    # print("APPS: ", settings.PROJECT_APPS)
    # list values in the db:
    db_classes = list(permissions.values_list(
        'view_name', flat=True).distinct())
    # print("db", db_classes)
    # search for all view classes:
    code_classes = []
    permission_found = []
    for app_name in settings.PROJECT_APPS:
        import_path = "%s.%s" % (app_name, 'views')
        this_module = import_module(import_path)
        for name, obj in inspect.getmembers(this_module):
            if inspect.isclass(obj) and obj.__module__ == import_path and getattr(obj, 'is_view', False):
                for method in obj.allowed_methods:
                    if method in permission_methods:
                        permission_found.append({"view_name":name, "app_name":app_name, "method": method})
                        code_classes.append(name)
    # search for all view classes done.
    # check that view names are unique:
    if not (len(code_classes) == len(set(code_classes))):
        raise ValueError(
            "The view_names in whole [PROJECT_APPS].views is not unique! Try changing the name of one of these classes.")
    # print(code_classes)
    # check for the deleted or renamed views, we can't handle rename here, so the rename is adding one new record and deletes the old one.
    for db_view_name in db_classes:
        print("db_view_name", db_view_name)
        if db_view_name not in code_classes:
            # db_classes is just calculated from the database, so it should exists!
            db_obj = Permission.objects.get(view_name=db_view_name)
            db_obj.delete()
    # renew the list of values!
    db_classes = list(permissions.values_list(
        'view_name', flat=True).distinct())
    # create views that doesn't exists:
    for code_class in code_classes:
        print("code_class", code_class)
        if code_class not in db_classes:
            p = Permission()
            p.view_name = code_class
            p.save()

    return True