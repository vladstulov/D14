
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),


    path('', include('newsapp.urls')),
    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),
    path('news/', include('newsapp.urls')),

    path('i18n/', include('django.conf.urls.i18n')),
]

# urlpatterns +=  i18n_patterns(
#     path('', include('newsapp.urls')),
# )
