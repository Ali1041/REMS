from django.db import models
import datetime
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

# Create your models here.
user = get_user_model()


# a general seller model of property
class SellerProperty(models.Model):
    alphanumeric = RegexValidator(r'^[a-zA-Z ]*$', 'Only alphabetic characters are allowed.')

    by = models.ForeignKey(user, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=100, default='1 million')
    unit_choice = [('Square feet', 'square feet'),
                   ('Square meter', 'square meter'),
                   ('Square Yard', 'Square Yard'),
                   ('Marla', 'marla'),
                   ('Kanal', 'kanal')]
    size = models.PositiveIntegerField()
    unit = models.CharField(choices=unit_choice, max_length=12)
    bedrooms = models.PositiveIntegerField()
    bathroom = models.PositiveIntegerField()
    image_house = models.ImageField(upload_to='property', default='property/c2.jpg')
    purpose_choice = [('Sale', 'sale'), ('Rent', 'rent')]
    purpose = models.CharField(choices=purpose_choice, max_length=4)
    type_choices = [('Plot', 'plot'), ('Commercial', 'commercial'), ('House', 'house')]
    type = models.CharField(max_length=10, choices=type_choices)
    city = models.CharField(max_length=30, validators=[alphanumeric])
    sector = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)

    # ordering the model objects
    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title + ',' + str(self.price)

    # getting the photo url
    def get_photo_url(self):
        if self.image_house and hasattr(self.image_house, "url"):
            return self.image_house.url


# approval model for the property
class Approve(models.Model):
    request_choices = [('Approve', 'Approve'), ('Reject', 'Reject'), ('Sold', 'Sold'), ('Pending', 'pending')]
    request_approval = models.CharField(choices=request_choices, max_length=10, default='pending')
    approval = models.ForeignKey(SellerProperty, on_delete=models.CASCADE, related_name='approval_seller')

    def __str__(self):
        return 'Approval detail fo this property title: ' + self.approval.title

    def seller_title(self):
        return self.approval.title
