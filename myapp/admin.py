from django.contrib import admin
from .models import contacts , SERVICES , Technicians,Testimonial,car_rent,BOOK_CAR,OurServices,Datels,accessories,accessories_book,singup

# Register your models here.


admin.site.register(SERVICES)
admin.site.register(contacts)
admin.site.register(Technicians)
admin.site.register(Testimonial)
admin.site.register(car_rent)
admin.site.register(BOOK_CAR)
admin.site.register(OurServices)
admin.site.register(Datels)
admin.site.register(accessories)
admin.site.register(accessories_book)
admin.site.register(singup)



