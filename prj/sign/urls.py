from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView, upgrade_me
#, #leo

#from sign import views # Такой вариант лучше чем первый, тогда не надо их всех указывать:
# from sign.views import leo, scorpio, fish и т.п.
# from приложение.файл import def1, def2 ...

#если внутри приложения импорт, то можно так:
# from .views import def1, def2 ...

urlpatterns = [

    #path('horoscope/leo/', leo),
    #path('zz', views.scoppio),
    #path('<zzz>/', views.zzzz),

    path('login/',
         LoginView.as_view(template_name = 'sign/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name = 'sign/logout.html'),
         name='logout'),
    path('signup/',
         BaseRegisterView.as_view(template_name = 'sign/signup.html'),
         name='signup'),
    path('upgrade/', upgrade_me, name = 'upgrade'),
]