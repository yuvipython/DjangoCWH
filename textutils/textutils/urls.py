"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name='index'),
#     path('about', views.about, name='about'),
#
# ]

# text utility

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # path('remove_punctuation', views.remove_punctuation, name='remove_punctuation'),
    # path('capitalize_first', views.capitalize_first, name='capitalize_first'),
    # path('remove_newline', views.remove_newline, name='remove_newline'),
    # path('remove_space', views.remove_space, name='remove_space'),
    # path('char_count', views.char_count, name='char_count'),
    path('analyze/', views.analyze, name='analyze'),
    path('e1/', views.e1, name='e1'),

]
