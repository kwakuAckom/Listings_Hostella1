from django.db import models
from django.utils.timezone import now

class Listing(models.Model):
    class HomeType(models.TextChoices):
        HOSTEL = 'Hostel'
        HOMESTEL = 'Homestel'
    
    class Proximity(models.TextChoices):
        CAMPUS = "On campus"
        CLOSE = 'Close to campus'
        NORMAL = 'Normal distance from campus'
        FAR = 'Far from campus'

    class PaymentMethod(models.TextChoices):
        MOBILE_MONEY = 'Mobile money'
        BANK = 'Bank Payment'
        DEBIT_CARD = 'Credit or debit card payment'
        PERSONAL = 'Meet and pay in person'

    realtor = models.EmailField(max_length=100)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    payment_method = models.CharField(max_length=50, choices=PaymentMethod.choices)
    address = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    campus = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    rooms = models.IntegerField()
    room_capacity = models.IntegerField()
    bathroom = models.BooleanField()
    kitchen = models.BooleanField()
    hostel_class = models.CharField(max_length=1)
    hometype = models.CharField(max_length=10, choices=HomeType.choices)
    distance = models.CharField(max_length=50, choices=Proximity.choices)
    photo1 = models.ImageField()
    photo2 = models.ImageField()
    photo3 = models.ImageField()
    is_published = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=now)

    def __str__(self):
        return self.title