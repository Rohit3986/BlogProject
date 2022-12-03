
from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.signals import request_finished,request_started,got_request_exception
from django.db.models.signals import pre_delete,pre_init,pre_save,post_delete,post_init,post_save,pre_migrate,post_migrate
from django.db.backends.signals import connection_created

#reciver's function
def login_sucess(sender, request, user, **kwargs):
    request.session["active"]=True
    print("----------------------------------")
    print("running intro")
    print("request is ",request)
    print("user is ",user)
    print("userpaaswrd is ",user.password)
    print("sender is ",sender)
    print("--------------------------------------------")
user_logged_in.connect(login_sucess,sender=User)

'''@receiver(user_logged_out,sender=User)
def logout_sucess(sender, request, user, **kwargs):
    print("----------------------------------")
    print("running outro logout")
    print("request is ",request)
    print("user is ",user)
    print("userpaaswrd is ",user.password)
    print("sender is ",sender)
    print("--------------------------------------------")
#user_logged_out.connect(logout_sucess,sender=User)

@receiver(user_login_failed)
def login_failed(sender, credentials,request, **kwargs):
    print("----------------------------------")
    print("running logout failed")
    print("request is ",request)
    print("credentials is ",credentials)
    print("sender is ",sender)
    print("--------------------------------------------")

@receiver(pre_save,sender=User)
def save_models(sender, instance, **kwargs):
    print("----------------------------------")
    print("running pre save")
    print("instance is ",instance)
    print(f'kwargs: {kwargs}')
    print("sender is ",sender)
    print("--------------------------------------------")

@receiver(post_save,sender=User)
def save_models_post(sender, instance, created,**kwargs):
    print("----------------------------------")
    print("running post save")
    print("instance is ",instance)
    print(f'kwargs: {kwargs}')
    print("sender is ",sender)
    print("created is ",created)
    print("--------------------------------------------")


@receiver(pre_delete,sender=User)
def delete_models(sender, instance, **kwargs):
    print("----------------------------------")
    print("running pre delete")
    print("instance is ",instance)
    print(f'kwargs: {kwargs}')
    print("sender is ",sender)
    print("--------------------------------------------")

@receiver(post_delete,sender=User)
def delete_models(sender, instance, **kwargs):
    print("----------------------------------")
    print("running post delete")
    print("instance is ",instance)
    print(f'kwargs: {kwargs}')
    print("sender is ",sender)
    print("--------------------------------------------")

@receiver(pre_init,sender=User)
def init_models(sender, *args, **kwargs):
    print("----------------------------------")
    print("running pre init")
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')
    print("sender is ",sender)
    print("--------------------------------------------")

@receiver(post_init,sender=User)
def init_models(sender, *args, **kwargs):
    print("----------------------------------")
    print("running post init")
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')
    print("sender is ",sender)
    print("--------------------------------------------")

@receiver(request_started)
def req_start(sender, environ,**kwargs):
    print("----------------------------------")
    print("running request started")
    print("environ is ",environ)
    print("sender is ",sender)
    print("--------------------------------------------")

@receiver(request_finished)
def req_finshed(sender, **kwargs):
    print("----------------------------------")
    print("running request finshed")

    print("sender is ",sender)
    print("--------------------------------------------")

@receiver(got_request_exception)
def error_h(sender, **kwargs):
    print("----------------------------------")
    print("running got request exception")

    print("sender is ",sender)
    print("--------------------------------------------")


@receiver(pre_migrate)
def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps,**kwargs):
    print("----------------------------------")
    print("running pre migrate")

    print("sender is ",sender)
    print("app_config is ",app_config)
    print("verbosity is ",verbosity)
    print("interactive is ",interactive)
    print("using is ",using)
    print("plan is ",plan)
    print("apps is ",apps)
    print(f'kwargs is {kwargs}')
    print("--------------------------------------------")

@receiver(post_migrate)
def after_install_app(sender, app_config, verbosity, interactive, using, plan, apps,**kwargs):
    print("----------------------------------")
    print("running pre migrate")

    print("sender is ",sender)
    print("app_config is ",app_config)
    print("verbosity is ",verbosity)
    print("interactive is ",interactive)
    print("using is ",using)
    print("plan is ",plan)
    print("apps is ",apps)
    print(f'kwargs is {kwargs}')
    print("--------------------------------------------")

@receiver(connection_created)
def conn_db(sender, connection,**kwargs):
    print("----------------------------------")
    print("running conndb")

    print("sender is ",sender)
    print("connection is ",connection)
    print(f'kwargs is {kwargs}')
    print("--------------------------------------------")'''