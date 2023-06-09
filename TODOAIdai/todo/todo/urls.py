"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from main.views import *
from homework.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage, name="home"),
    path("test/", test, name="test"),
    path("test2/", second),
    path("dom", dom, name="dom"),
    path("test3/", test, name="test3"),
    path("meet/", meet, name="meet"),
    path("meet1/", meet1, name="meet1"),
    path("add-todo/", add_todo, name="add-todo"),
    path("add-tome/", add_tome, name="add-tome"),
    path("delete-todo/<id>/", delete_todo, name="delete-todo"),
    path("mark-todo/<id>/", mark_todo, name="mark-todo"),
    path("unmark-todo/<id>/", unmark_todo, name="unmark-todo"),
    path("delt-todo/<id>/",delete_to_meet,name="delt-todo"),
    path("mark-todos/<id>/", mark_to_meet,name="mark-todos"),
    path("clos-todo/<id>/",closed_todo, name="clos-todo"),
    path("close-todo/<id>", close_todo, name="close-todo"),
    path("habits/", habits, name="habits"),
    path("add-habits/", add_habits, name="add-habits"),
    path("del-habits/<id>/", del_habits, name="del-habits"),
    path("mark-habits/<id>/", mark_habits, name="mark-habits"),
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

