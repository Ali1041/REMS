from django.db import models

from django.contrib.auth import get_user_model

# Create your models here.
user = get_user_model()


class SellerProperty(models.Model):
    by = models.ForeignKey(user, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    unit_choice = [('Square feet', 'square feet'),
                   ('Square meter', 'square meter'),
                   ('Square Yard', 'Square Yard'),
                   ('Marla', 'marla'),
                   ('Kanal', 'kanal')]
    size = models.PositiveIntegerField()
    unit = models.CharField(choices=unit_choice, max_length=12)
    bedrooms = models.PositiveIntegerField()
    bathroom = models.PositiveIntegerField()
    image_house = models.ImageField(upload_to='property',default='property/c2.jpg')
    purpose_choice = [('Sale', 'sale'), ('Rent', 'rent')]
    purpose = models.CharField(choices=purpose_choice, max_length=4)
    type_choices = [('Plot', 'plot'), ('Commercial', 'commercial'), ('House', 'house')]
    type = models.CharField(max_length=10, choices=type_choices)
    city = models.CharField(max_length=30)
    sector = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.title + ',' + str(self.price)

    def get_photo_url(self):
        if self.image_house and hasattr(self.image_house,"url"):
            return self.image_house.url


class Approve(models.Model):
    request_choices = [('Approve', 'Approve'), ('Reject', 'Reject'), ('Sold', 'Sold'),('Pending','pending')]
    request_approval = models.CharField(choices=request_choices, max_length=10,default='pending')
    approval = models.ForeignKey(SellerProperty, on_delete=models.CASCADE)

    def __str__(self):
        return 'Approval detail fo this property title: ' + self.approval.title
