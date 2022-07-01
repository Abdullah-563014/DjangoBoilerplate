from django.urls import path

from AuthApp.controllers import authController
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# from app.controllers.SiteMapController import SITEMAPS
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse


urlpatterns = [


    ################################################################################################
    ################ Authentication ###########################################################
    ################################################################################################
    path('', authController.index, name='index'),
    path('login/', authController.index, name='login'),
    # path('login-action/', authController.loginAction, name='loginAction'),
    # path('signup/', authController.signup, name='signup'),
    # path('signup-action/', authController.signupAction, name='signupAction'),




    ################################################################################################
    ################ DEV Controller ###########################################################
    ################################################################################################
    # path('dev/', devController.dev, name='dev'),

]


urlpatterns += staticfiles_urlpatterns()
# handler404 = devController.pageNotFound
