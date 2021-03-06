"""groupup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path,include
from django.conf.urls import url,include
from . import views,settings
from accounts import views as accviews
from groups import views as grviews
from posts import views as poviews
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage.as_view(),name="home"),
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name="login"),
    path('logout/',auth_views.LogoutView.as_view(),name="logout"),
    path('signup/',accviews.SignUp.as_view(),name="signup"),
    path("test/",views.TestPage.as_view(),name="test"),
    path("thanks/",views.ThanksPage.as_view(),name="thanks"),
    url(r"^posts/", include("posts.urls", namespace="posts")),
    url(r"^groups/",include("groups.urls", namespace="groups")),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),


]
