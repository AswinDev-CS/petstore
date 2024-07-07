"""
URL configuration for EcomProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from petstoreapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name="home"),
    path('signup',views.SignUpView.as_view(),name="signup"),
    path('signin',views.SignInView.as_view(),name="signin"),
    path('signout',views.SignOutView.as_view(),name="signout"),
    path('detail/<int:id>',views.PetDetailView.as_view(),name="detail"),
    path('cart/<int:id>',views.CartCreateView.as_view(),name="cartcreate"),
    path('delete/<int:id>',views.CartDelete.as_view(),name="delete"),
    path('list',views.CartListView.as_view(),name="list"),
    path('order/<int:id>',views.PlaceOrderView.as_view(),name="order"),
    path('address',views.AdrressView.as_view(),name="address"),
    path('addelete/<int:id>',views.DeleteAdrressView.as_view(),name="addelete"),
    path('cat/<int:id>',views.CategoryView.as_view(),name="cat"),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

