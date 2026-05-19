from itertools import count

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt

from .models import contacts,SERVICES,Technicians,Testimonial,car_rent,BOOK_CAR,OurServices,Datels,accessories,accessories_book,singup,Cart,Order,OrderItem
import razorpay

# def index(request):
#     data = Technicians.objects.all()
#     data1 = Testimonial.objects.all()
#     data2 = car_rent.objects.all()
#     data5 = OurServices.objects.all()
#
#     if request.POST:
#         u = request.POST['Uname']
# Create your views here.
#         E = request.POST['EMAIL']
#         s = request.POST['service']
#         d = request.POST['date']
#         r = request.POST['SREQUEST']
#         obj = SERVICES(Uname = u, EMAIL = E, service = s, date =d, SREQUEST = r)
#         obj.save()
#         return redirect("/#")
#     return render(request,"index.html",{'data':data,"data1":data1,"data2":data2,"data5":data5})

def index(request):
    data = Technicians.objects.all()
    data1 = Testimonial.objects.all()
    data2 = car_rent.objects.all()
    data5 = OurServices.objects.all()
    data6 = Datels.objects.all()  # Include `datels` data
    data7 = accessories.objects.all()


    if request.POST:
        u = request.POST['Uname']
        E = request.POST['EMAIL']
        s = request.POST['service']
        d = request.POST['date']
        r = request.POST['SREQUEST']
        obj = SERVICES(Uname=u, EMAIL=E, service=s, date=d, SREQUEST=r)
        obj.save()
        return redirect("/index")
    return render(request, "index.html", {'data': data, "data1": data1, "data2": data2, "data5": data5, "data6": data6, "data7":data7})


def booking(request):
    services = Datels.objects.all()  # fetch all available services

    if request.method == 'POST':
        u = request.POST['Uname']
        E = request.POST['EMAIL']
        s_id = request.POST['service']  # this is ID of Datels
        d = request.POST['date']
        r = request.POST['SREQUEST']

        service_obj = Datels.objects.get(id=s_id)  # fetch the actual Datels instance

        obj = SERVICES(Uname=u, EMAIL=E, service=service_obj, date=d, SREQUEST=r)
        obj.save()
        return redirect("/payment_process")

    return render(request, "booking.html", {'services': services})


def ser(request,id):
    # data1 = Testimonial.objects.all()
    data6 = Datels.objects.filter(sid=id).all

    # if request.POST:
    #     u = request.POST['Uname']
    #     E = request.POST['EMAIL']
    #     s = request.POST['service']
    #     d = request.POST['date']
    #     r = request.POST['SREQUEST']
    #     obj = SERVICES(Uname = u, EMAIL = E, service = s, date =d, SREQUEST = r)
    #     obj.save()
    #     return redirect("/#")
    return render(request,"service.html", {"data6":data6})


def team(request):
    data = Technicians.objects.all()
    return render(request,"team.html", {"data":data})


def testimonial(request):
    data1 = Testimonial.objects.all()
    return render(request,"testimonial.html", {"data1":data1})


def contact(request):
    if request.POST:
        n = request.POST['name']
        e = request.POST['email']
        s = request.POST['subject']
        m = request.POST['message']
        obj = contacts(name = n , email = e , subject = s , message = m)
        obj.save()
        return redirect("/#")
    return render(request,"contact.html")


def about(request):
    data = Technicians.objects.all()
    return render(request,"about.html", {"data":data})


def error(request):
    data7 = accessories.objects.all()
    data5 = OurServices.objects.all()

    return render(request,"404.html",{"data7":data7,"data5":data5,})


def rental(request):
    data2 = car_rent.objects.all()
    return render(request,"rental.html", {"data2":data2})


def car_book(request,id):
    data3 = car_rent.objects.get(id=id)
    data4 = BOOK_CAR.objects.filter(cid=data3)
    if request.POST:
        un = request.POST['uname']
        ue = request.POST['uemail']
        ph = request.POST['phone_no']
        D = request.POST['DATE']
        f = request.FILES['img']
        s = request.POST['state']
        c = request.POST['city']
        a = request.POST['address']
        obj = BOOK_CAR(uname = un , uemail = ue , phone_no = ph , DATE = D,img = f , state = s , city = c , address = a)
        obj.cid_id = id
        obj.save()
        return redirect("/payment_process")
    return render(request,"car_book.html",{"data3":data3, "data4":data4})

def sign_up(request):
    # data8 = singup.objects.get(Email=e)
    if request.POST:
        UN = request.POST['USER_NAME']
        Email = request.POST['Email']
        password = request.POST['password']
        obj = singup(USER_NAME=UN,Email=Email,password=password)
        obj.save()
        return redirect('/#')
    return render(request , "sign_up.html")

def login(request):
    if request.session.get("islogin"):
        return redirect('/index')

    if request.method == "POST":
        e = request.POST.get('Email')
        p = request.POST.get('password')

        # Debugging print
        count = singup.objects.filter(Email=e, password=p).count()

        if count>0:
            request.session['islogin'] = True
            request.session['Email'] = e
            return redirect('/index')  # Ensure '/index' route is correctly defined


    return render(request, "Login.html")


def Service(request):
    data1 = Testimonial.objects.all()
    data5 = OurServices.objects.all()
    data6 = Datels.objects.all()  #
    if request.POST:
        u = request.POST['Uname']
        E = request.POST['EMAIL']
        s = request.POST['service']
        d = request.POST['date']
        r = request.POST['SREQUEST']
        obj = SERVICES(Uname = u, EMAIL = E, service = s, date =d, SREQUEST = r)
        obj.save()


        return redirect("/#")
    return render(request,"service.html",{"data1":data1,"data5":data5,"data6":data6})


def Accessories_book(request, id):
    data5 = accessories.objects.get(id=id)  # Fetch the accessory by ID
    data6 = accessories_book.objects.filter(aid=data5)  # Get related bookings

    if request.POST:
        U = request.POST['UNAME']
        E = request.POST['UEMAIL']
        P = request.POST['PHONENO']
        CM = request.POST['CAR_COMPANY']
        M = request.POST['CAR_MODEL']
        S = request.POST['STATE']
        C = request.POST['CITY']
        A = request.POST['ADDERESS']
        obj = accessories_book(UNAME=U, UEMAIL=E, PHONENO=P, CAR_COMPANY=CM, CAR_MODEL=M, STATE=S, CITY=C, ADDERESS=A)
        obj.aid_id = id
        obj.save()
        return redirect("/payment_process")

    return render(request, "Accessories_book.html", {"data5": data5, "data6": data6})

# def cart(request,id):
#     e = request.session.get('Email')
#     data8 = singup.objects.get(Email=e)
#
#
#     # Fetch all items associated with the user's email
#     all_items = accessories.objects.filter(id=id)  # Remove filtering by email
#
#     # Create a set to store unique items based on name and image
#     unique_items = set()
#     #
#     distinct_items = []
#     for item in all_items:
#         item_key = (item.aname, item.img)  # Use pname and image for uniqueness
#         if item_key not in unique_items:
#             unique_items.add(item_key)
#             distinct_items.append(item)
#         elif item_key in unique_items:
#             unique_items.remove(item_key)
#
#         # Calculate total price for distinct items
#         # total_price = sum(float(item.Price) for item in distinct_items)  # Convert price to float
#     return render(request,"Cart.html",{"data8":data8,"data9":distinct_items,"id":id})
#
#
#
#
#
# def update_cart(request, id, a=None):
#     product = get_object_or_404(accessories_deiails, id=id)
#
#     if a is None:
#         if product.quantity > 1:
#             a = product.quantity
#         else:
#             a = 1
#
#     if request.method == 'GET':
#         action = request.GET.get('action')
#
#         if action == 'add':
#             product.quantity += 1
#
#             c = int(product.Price)
#
#             b = c * product.quantity
#             product.Price = b // a  # Perform integer division
#             a += 1
#             product.save()
#             return redirect("/cart")
#         elif action == 'remove':
#             if product.quantity > 1:
#                 product.quantity -= 1
#                 c = int(product.Price)
#
#                 product.price = c * product.quantity // a  # Perform integer division
#                 product.save()
#                 return redirect("/cart")
#             else:
#                 return HttpResponseBadRequest("Cannot decrement below one")
#         else:
#                 return HttpResponseBadRequest("Invalid action")
#     else:
#             return HttpResponseBadRequest("Invalid request method")
#

#
# def p_cart(request, id):
#     # Retrieve the petfood item based on ID
#     petfood_item = get_object_or_404(accessories, pk=id)
#     e = request.session.get('Email')
#
#     existing_cart_item = accessories_deiails.objects.filter(aname=petfood_item.aname, img=petfood_item.img,Email=e).exists()
#
#     if not existing_cart_item:
#         cart_item = accessories_deiails.objects.create(
#             aname=petfood_item.aname,
#             Price=petfood_item.Price,
#             img=petfood_item.img,
#             Email=e,
#         )
#     else:
#         # If the item already exists in the cart, add a message and redirect
#         message.warning(request, 'Item already exists in the cart.')
#         return redirect('/productcheckout')
#


# def add_to_cart(request, product_id):
#     product = get_object_or_404(accessories, id=product_id)
#     cart_item, created = Cart.objects.get_or_create(product=product)
#
#     if not created:
#         cart_item.quantity += 1
#         cart_item.save()
#
#     return redirect('/cart_page')
#
#
# def cart_page(request):
#     cart_items = Cart.objects.all()
#     total = sum(item.total_price() for item in cart_items)
#
#     return render(request, "Cart.html", {"cart_items": cart_items, "total": total})
#
#
# def remove_from_cart(request, cart_id):
#     cart_item = get_object_or_404(Cart, id=cart_id)
#     cart_item.delete()
#
#     return redirect('/cart_page')
def add_to_cart(request, product_id):
    product = get_object_or_404(accessories, id=product_id)
    cart_item, created = Cart.objects.get_or_create(product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('/cart_page')


def cart_page(request):
    cart_items = Cart.objects.all()
    total = sum(item.total_price() for item in cart_items)

    return render(request, "Cart.html", {"cart_items": cart_items, "total": total})


def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)
    cart_item.delete()

    return redirect('/cart_page')


def increase_quantity(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)
    cart_item.quantity += 1
    cart_item.save()

    return redirect('/cart_page')


def decrease_quantity(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()  # Remove item if quantity reaches 0

    return redirect('/cart_page')



def checkout_page(request):
    cart_items = Cart.objects.all()
    total = sum(item.total_price() for item in cart_items)

    return render(request, "checkout.html", {"cart_items": cart_items, "total": total})


def process_checkout(request):
    if request.method == "POST":
        full_name = request.POST["full_name"]
        email = request.POST["email"]
        address = request.POST["address"]
        phone = request.POST["phone"]

        cart_items = Cart.objects.all()
        total = sum(item.total_price() for item in cart_items)

        # Create order
        order = Order.objects.create(
            full_name=full_name,
            email=email,
            address=address,
            phone=phone,
            total_price=total,
        )

        # Create order items
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )

        # Clear cart after checkout
        cart_items.delete()

        return redirect("/payment_process")

    return redirect("/checkout_page")


#
# def payment_process(request):
#     # Razorpay KeyId and key Secret
#     key_id = 'rzp_test_PvM4GxK9MYlCUc'
#     key_secret = 'WzsOTRAU4l3oAA1CS7jlVS5E'
#
#     # total_value=request.POST.get
#     # print(total_value)
#
#     amount = int(100) * 100  # Your Amount
#     # float(total_value)
#     client = razorpay.Client(auth=(key_id, key_secret))
#
#     data = {
#         'amount': amount,
#         'currency': 'INR',
#         "receipt": "OIBP",
#         "notes": {
#             'name': 'AK',
#             'payment_for': 'OIBP Test'
#         }
#     }
#     id = request.user.id
#     result = 1
#     payment = client.order.create(data=data)
#     context = {'payment': payment, 'result': result}
#     return render(request, 'Payment.html', context)
#

import razorpay
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def payment_process(request):
    key_id = 'rzp_test_PvM4GxK9MYlCUc'
    key_secret = 'WzsOTRAU4l3oAA1CS7jlVS5E'

    try:
        amount = 100 * 100  # Razorpay expects the amount in paise (e.g., ₹100 = 10000)
        client = razorpay.Client(auth=(key_id, key_secret))

        data = {
            'amount': amount,
            'currency': 'INR',
            'receipt': 'OIBP',
            'notes': {
                'name': 'AK',
                'payment_for': 'OIBP Test'
            }
        }

        payment = client.order.create(data=data)

        context = {
            'payment': payment,
            'result': 1
        }
        return render(request, 'Payment.html', context)

    except razorpay.errors.BadRequestError as e:
        return HttpResponse(f"Bad Request to Razorpay: {e}", status=400)

    except razorpay.errors.ServerError as e:
        return HttpResponse(f"Razorpay Server Error: {e}", status=500)

    except Exception as e:
        return HttpResponse(f"Unexpected Error: {e}", status=500)



@csrf_exempt
def success(request):
    context = {}
    return render(request,"success.html",context)




# from django.shortcuts import render
# from .models import Order, OrderItem, BOOK_CAR, Datels
#
# def order_list(request):
#     orders = Order.objects.prefetch_related('orderitem_set__product').order_by('-created_at')
#     car_bookings = BOOK_CAR.objects.all().order_by('-DATE')
#     service_orders = Datels.objects.select_related('sid').order_by('-id')
#
#     return render(request, 'order_list.html', {
#         'orders': orders,
#         'car_bookings': car_bookings,
#         'service_orders': service_orders,
#     })

from .models import Order, BOOK_CAR, SERVICES

def order_list(request):
    if not request.session.get("islogin"):
        return redirect('/login')

    user_email = request.session.get("Email")

    orders = Order.objects.filter(email=user_email).prefetch_related('orderitem_set__product').order_by('-created_at')
    car_bookings = BOOK_CAR.objects.filter(uemail=user_email).order_by('-DATE')
    service_orders = SERVICES.objects.filter(EMAIL=user_email).select_related('service').order_by('-id')

    return render(request, 'order_list.html', {
        'orders': orders,
        'car_bookings': car_bookings,
        'service_orders': service_orders,
    })



def logout(request):
    del request.session['islogin']
    return redirect('/#')
