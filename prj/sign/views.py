from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm

from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

#from django.http import HttpResponse
#API для объектов HttpRequest и HttpResponse, которые определены в модуле django.http.
import logging
logger = logging.getLogger(__name__)

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'

@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        premium_group.user_set.add(user)
    return redirect('/')

# def leo(request):
#     #HTTPResponse- Каждое представление отвечает за возврат объекта HttpResponse.
#     return HttpResponse("Знак зодиака Левв!")
#
# def scoppio(request):
#     return HttpResponse("Знак зодиака Скорпион!")

# def zzzz(request, zzz):
#     if zzz == 'фыва':
#         return HttpResponse("Щляпа!")
#     elif zzz == '2':
#         return HttpResponse("Щляпа2!")
#     elif zzz == '3':
#         return HttpResponse("Щляпа3!")
    #else:
        #return HttpResponse("Щляпа1!")

