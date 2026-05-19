from django.shortcuts import render,redirect
from myapp.models import contacts,OurServices,SERVICES,car_rent,Technicians,BOOK_CAR,Testimonial,accessories,Datels,Order,Cart


# Create your views here.

def index1(request):
    return render(request,"index1.html")


def show_contact(request):
    data = contacts.objects.all()
    return render(request,"show_contact.html",{"data":data})

def view_services(request):
    data1 = OurServices.objects.all()
    return render(request, "view_services.html", {"data1": data1})

def add_services(request):
    if request.POST:
        H = request.POST['H_title']
        obj = OurServices(H_title=H)
        obj.save()
        return redirect("/#")
    return render(request,"add_services.html")

def Edit_services(request,id):
    data1 = OurServices.objects.get(id=id)
    if request.POST:
        H = request.POST['H_title']
        obj = OurServices(H_title=H,id=id)
        obj.save()
        return redirect("/view_services")
    return render(request, "Edit_services.html",{"data1":data1})

def Remove_services(request):
    data1 = OurServices.objects.all()
    return render(request, "Remove_services.html", {"data1": data1})

def delete(request,id):
    data = OurServices.objects.get(id=id).delete()
    return redirect("/view_services")

def Services_Booing_Show(request):
    data2 = SERVICES.objects.all()
    return render(request,"Services_Booking_Show.html",{"data2":data2})

def view_car(request):
    data3 = car_rent.objects.all()
    return render(request,"view_car.html",{"data3":data3})

def add_car(request):
    if request.POST:
        c = request.POST['car_name']
        p = request.POST['price']
        i = request.FILES['img']
        obj = car_rent(car_name=c , price = p,img =i)
        obj.save()
        return redirect('/view_car')
    return render(request,"add_car.html")

def edit_car(request,id):
    data4 = car_rent.objects.get(id=id)
    if request.POST:
        c = request.POST['car_name']
        p = request.POST['price']
        i = request.FILES.get('img',None)
        data4.car_name = c
        data4.price = p
        if i:
            data4.img = i
        data4.save()
        return redirect('/view_car')
    return render(request, "edit_car.html", {"data4": data4})

def delete_car(request,id):
    data = car_rent.objects.get(id=id).delete()
    return redirect("/view_car")

def view_technicians(request):
    data5 =  Technicians.objects.all()
    return render(request,"view_technicians.html",{"data5":data5})

def add_technicians(request):
    if request.POST:
        tn = request.POST['tname']
        d = request.POST['Designation']
        f = request.POST['facebook']
        t = request.POST['twitter']
        i = request.POST['instagram']
        img = request.FILES['image']
        obj = Technicians(tname=tn , Designation=d , facebook=f , twitter=t , instagram=i , image=img )
        obj.save()
        return redirect("/view_technicians")
    return render(request,"add_technicians.html")


def edit_technicians(request,id):
    data5 = Technicians.objects.get(id=id)
    if request.POST:
        tn = request.POST['tname']
        d = request.POST['Designation']
        f = request.POST['facebook']
        t = request.POST['twitter']
        i = request.POST['instagram']
        img = request.FILES.get('image', None)
        data5.tname=tn
        data5.Designation=d
        data5.facebook=f
        data5.twitter=t
        data5.instagram=i
        data5.id=id
        if img:
            data5.image =img
        data5.save()
        return redirect('/view_technicians')
    return render(request,"edit_technicians.html",{"data5":data5})


def delete_technicians(request,id):
    data = Technicians.objects.get(id=id).delete()
    return redirect("/view_technicians")



def view_testimonial(request):
    data = Testimonial.objects.all()
    return render(request,"view_testimonial.html",{"data":data})

def add_testimonial(request):
    if request.POST:
        cn = request.POST['cname']
        p = request.POST['profession']
        F = request.POST['feedback']
        img = request.FILES['image']
        obj = Testimonial(cname=cn , profession=p , feedback=F , image=img )
        obj.save()
        return redirect("/view_testimonial")
    return render(request,"add_testimonial.html")

def edit_testimonial(request,id):
    data = Testimonial.objects.get(id=id)
    if request.POST:
        cn = request.POST['cname']
        p = request.POST['profession']
        F = request.POST['feedback']
        i = request.FILES.get('image', None)
        data.cname = cn
        data.profession = p
        data.feedback = F
        data.id=id
        if i:
            data.image = i
        data.save()
        return redirect('/view_testimonial')
    return render(request,"edit_testimonial.html",{"data":data})

def delete_testimonial(request,id):
    data = Testimonial.objects.get(id=id).delete()
    return redirect("/view_testimonial")

def view_accessories(request):
    data = accessories.objects.all()
    return render(request,"view_accessories.html",{"data":data})

def add_accessories(request):
    if request.POST:
        a = request.POST['aname']
        P = request.POST['Price']
        i = request.FILES['img']
        obj = accessories(aname=a , Price = P,img =i)
        obj.save()
        return redirect('/view_accessories')
    return render(request,"add_accessories.html")

def edit_accessories(request,id):
    data5 = accessories.objects.get(id=id)
    if request.POST:
        a = request.POST['aname']
        P = request.POST['Price']
        i = request.FILES.get('img', None)
        data5.aname = a
        data5.Price = P
        if i:
            data5.img = i
        data5.save()
        return redirect('/view_accessories')
    return render(request, "edit_accessories.html", {"data5": data5})

def delete_accessories(request,id):
    data5 = accessories.objects.get(id=id).delete()
    return redirect("/view_accessories")


def show_car_booking(request):
    data = BOOK_CAR.objects.all()
    return render(request,"show_car_booking.html",{"data":data})


def show_access_booking(request):
    data = Order.objects.all()
    data1 = Cart.objects.all()
    return render(request, "show_accessories_booked.html",{"data":data,"data1":data1})



def view_datels(request):
    data = Datels.objects.all()
    return render(request,"view_datels.html",{"data":data})



#
# def add_datels(request):
#     if request.method == "POST":
#         # sid = request.POST.get('sid')
#         title = request.POST.get('title')
#         des = request.POST.get('des')
#         point = request.POST.get('point')
#         image = request.FILES.get('image')
#         datels_id =request.POST.get('datels_id')
#
#         try:
#             data6 = OurServices.objects.get(id=datels_id)
#             obj = datels(
#                 title = title,
#                 des = des,
#                 point = point,
#                 image = image,
#                 sid = data6
#             )
#             obj.save()
#             return HttpResponse("Datels added successfully")
#         except OurServices.DoesNotExist :
#             return HttpResponse("Invlid Datels Selected")
#     else:
#         data = OurServices.objects.all()
#         return render( request,"add_datels.html",{"OurServices":data})
#
#
# from django.shortcuts import render,get_object_or_404,redirect
# from django.http import HttpResponse

#


from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# from .models import OurServices, Datels  # Ensure correct model name

def add_datels(request):
    if request.method == "POST":
        title = request.POST.get('title')
        des = request.POST.get('des')
        # point = request.POST.get('point')
        image = request.FILES.get('image')
        datels_id = request.POST.get('datels_id')  # Correct field name

        print("Received datels_id:", datels_id)  # Debugging output

        if not datels_id:
            return HttpResponse("Please select a valid service.")

        try:
            datels_id = int(datels_id)  # Ensure it's an integer
            data6 = OurServices.objects.get(id=datels_id)

            obj = Datels(  # Use correct model name
                title=title,
                des=des,
                # point=point,
                image=image,
                our_service=data6
            )
            obj.save()
            return HttpResponse("Datels added successfully")
        except ValueError:
            return HttpResponse("Invalid Datels ID format")
        except OurServices.DoesNotExist:
            return HttpResponse("Invalid Datels Selected")

    else:
        data = OurServices.objects.all()
        return render(request, "add_datels.html", {"OurServices": data})


from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# from .models import OurServices, Datels  # Ensure correct model imports

def edit_datels(request, datels_id):
    datel = get_object_or_404(Datels, id=datels_id)
    services = OurServices.objects.all()

    if request.method == "POST":
        title = request.POST.get('title')
        des = request.POST.get('des')
        point = request.POST.get('point')
        image = request.FILES.get('image')
        service_id = request.POST.get('datels_id')

        print("Received service_id:", service_id)  # Debugging

        try:
            service = OurServices.objects.get(id=service_id)
            datel.title = title
            datel.des = des
            datel.point = point
            datel.our_service = service

            if image:  # Only update image if a new one is provided
                 datel.image = image


            datel.save()
            return HttpResponse("Datels updated successfully")
        except OurServices.DoesNotExist:
            return HttpResponse("Invalid OurServices selected")

    return render(request, "edit_datels.html", {"datel": datel, "services": services})



def delete_datels(request, datels_id):
    datel = get_object_or_404(Datels, id=datels_id)
    datel.delete()
    return HttpResponse("Datels deleted successfully")


ADMIN_USERNAME = 'admin@gmail.com'
ADMIN_PASSWORD = 'admin123'

def admin_login(request):
    error_message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            request.session['is_admin_logged_in'] = True
            return redirect('/index1')  # Redirect to your admin dashboard
        else:
            error_message = 'Invalid username or password.'

    return render(request, "LOGIN1.html", {'error': error_message})

def admin_logout(request):
    del request.session['islogin']
    return redirect('/#')

