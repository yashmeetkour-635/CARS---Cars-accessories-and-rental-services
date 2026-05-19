"""
URL configuration for webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from myapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index),
    path('booking', views.booking),
    path('ser/<int:id>', views.ser),
    path('team', views.team),
    path('testimonial', views.testimonial),
    path('contact', views.contact),
    path('about', views.about),
    path('error', views.error),
    path('rental', views.rental),
    path('car_book/<int:id>', views.car_book),
    path('sign_up', views.sign_up),
    path('', views.login),
    path('Service', views.Service),
    path('cart_page', views.cart_page),
    path('Accessories_book/<int:id>', views.Accessories_book),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('increase_quantity/<int:cart_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:cart_id>/', views.decrease_quantity, name='decrease_quantity'),
    path("checkout/", views.checkout_page, name="checkout_page"),
    path("process_checkout/", views.process_checkout, name="process_checkout"),
    path('payment_process', views.payment_process),
    path('success', views.success),
    path('order_list/', views.order_list, name='order_list'),
    path('logout', views.logout),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

