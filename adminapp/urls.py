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
from adminapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index1', views.index1),
    path('show_contact', views.show_contact),
    path('view_services', views.view_services),
    path('add_services', views.add_services),
    path('Edit_services/<int:id>', views.Edit_services),
    path('delete/<int:id>', views.delete),
    path('Remove_services', views.Remove_services),
    path('Services_Booing_Show', views.Services_Booing_Show),
    path('view_car', views.view_car),
    path('add_car', views.add_car),
    path('edit_car/<int:id>', views.edit_car),
    path('delete_car/<int:id>', views.delete_car),
    path('view_technicians', views.view_technicians),
    path('add_technicians', views.add_technicians),
    path('edit_technicians/<int:id>', views.edit_technicians),
    path('delete_technicians/<int:id>', views.delete_technicians),
    path('view_testimonial', views.view_testimonial),
    path('add_testimonial', views.add_testimonial),
    path('edit_testimonial/<int:id>', views.edit_testimonial),
    path('delete_testimonial/<int:id>', views.delete_testimonial),
    path('view_accessories', views.view_accessories),
    path('add_accessories', views.add_accessories),
    path('edit_accessories/<int:id>', views.edit_accessories),
    path('delete_accessories/<int:id>', views.delete_accessories),
    path('show_car_booking', views.show_car_booking),
    path('show_access_booking', views.show_access_booking),
    path('view_datels', views.view_datels),
    path('add_datels', views.add_datels),
    path('', views.admin_login),
    path('edit_datels/<int:datels_id>/', views.edit_datels),
    path('delete_datels/<int:datels_id>/', views.delete_datels, ),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
