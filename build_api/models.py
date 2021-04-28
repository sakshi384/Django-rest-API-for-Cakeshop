from django.db import models
import datetime
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=200)

    def __str__(self):
        return self.name


# model for add cakes
class Cake(models.Model):
    cakeid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200,default="")
    description=models.CharField(max_length=200,default="")
    price=models.IntegerField(default="")
    flavour=models.CharField(max_length=200,default="")
    weight=models.FloatField(default="")
    ingredients=models.CharField(max_length=200,default="")
    image=models.ImageField(upload_to='pic/',default="")


# model for add cake to cart
class AddCaketoCart(models.Model):
    cakeid = models.IntegerField(default="")
    email = models.EmailField()
    # createdat = models.DateTimeField(default=datetime.datetime.now())
    # name = models.CharField(max_length=200,default="")
    #
    # image = models.ImageField(upload_to='pic/',default="")
    # price = models.IntegerField(default="")
    # weight = models.FloatField(default="")
    # quantity = models.IntegerField(default=1)


# model for check out
class Checkout(models.Model):
    orderid=models.AutoField(primary_key=True)
    email=models.EmailField(max_length=200)
    name=models.CharField(max_length=200,default="")
    phone=models.IntegerField(default="")
    address=models.CharField(max_length=200,default="")
    pincode=models.IntegerField(default="")
    city=models.CharField(max_length=200,default="")
    price=models.IntegerField(default="")


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    print(reset_password_token.user.email)
    email_plaintext_message = " copy this token------->token={}".format(reset_password_token.key)
    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        'modernishi618@gmail.com',
        # to:
        [reset_password_token.user.email])
    # try:
    #     send_mail(
    #         # title:
    #         "Password Reset for {title}".format(title="Some website title"),
    #         # message:
    #         email_plaintext_message,
    #         # from:
    #         'passwortreset58@gmail.com',
    #         # to:
    #         [reset_password_token.user.email] )
    #
    # except:
    #     print("An exception occurred")
