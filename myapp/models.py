from django.db import models

# Create your models here.

class contacts(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=200)


class Technicians(models.Model):
    image = models.ImageField(upload_to="image/")
    tname = models.CharField(max_length=20)
    Designation = models.CharField(max_length=30)
    facebook = models.CharField(max_length=40)
    twitter = models.CharField(max_length=40)
    instagram = models.CharField(max_length=40)


class Testimonial(models.Model):
    image = models.ImageField(upload_to="image/")
    cname = models.CharField(max_length=20)
    profession = models.CharField(max_length=30)
    feedback = models.CharField(max_length=300)


class car_rent(models.Model):
    img = models.ImageField(upload_to="image/")
    car_name = models.CharField(max_length=20)
    price = models.CharField(max_length=10)


class BOOK_CAR(models.Model):
    cid = models.ForeignKey(car_rent,models.CASCADE)
    uname = models.CharField(max_length=20)
    uemail = models.EmailField()
    phone_no = models.CharField(max_length=10)
    DATE = models.CharField(max_length=10)
    img = models.ImageField(upload_to="image/")
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=300)


class OurServices(models.Model):
    H_title = models.CharField(max_length=100)

    def __str__(self):
        return self.H_title


class Datels(models.Model):
    image = models.ImageField(upload_to='image/')
    title = models.CharField(max_length=100)
    des = models.TextField()
    our_service = models.ForeignKey(OurServices, on_delete=models.CASCADE, related_name='datels')

    def __str__(self):
        return self.title


class SERVICES(models.Model):
    Uname = models.CharField(max_length=20)
    EMAIL = models.EmailField()
    service = models.ForeignKey(Datels, on_delete=models.CASCADE, related_name='services')
    date = models.CharField(max_length=10)
    SREQUEST = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.Uname} - {self.service.title}"



class accessories(models.Model):
    img = models.ImageField(upload_to="image/")
    aname = models.CharField(max_length=20)
    Price = models.CharField(max_length=10)

    def __str__(self):
        return self.aname

class Cart(models.Model):
    product = models.ForeignKey(accessories, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * int(self.product.Price)

    def __str__(self):
        return f"{self.product.aname} - {self.quantity}"

class accessories_book(models.Model):
    aid = models.ForeignKey(accessories,models.CASCADE)
    UNAME = models.CharField(max_length=20)
    UEMAIL = models.EmailField()
    PHONENO = models.CharField(max_length=10)
    CAR_COMPANY = models.CharField(max_length=40)
    CAR_MODEL = models.CharField(max_length=40)
    STATE = models.CharField(max_length=40)
    CITY = models.CharField(max_length=40)
    ADDERESS = models.CharField(max_length=300)


class singup(models.Model):
    USER_NAME = models.CharField(max_length=20)
    Email = models.EmailField()
    password = models.CharField(max_length=10)



class Order(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    phone = models.CharField(max_length=15)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.full_name} - ₹{self.total_price}"


class OrderItem(models.Model):
        order = models.ForeignKey(Order, on_delete=models.CASCADE)
        product = models.ForeignKey(accessories, on_delete=models.CASCADE)
        quantity = models.PositiveIntegerField()

        def __str__(self):
            return f"{self.product.aname} x {self.quantity}"



