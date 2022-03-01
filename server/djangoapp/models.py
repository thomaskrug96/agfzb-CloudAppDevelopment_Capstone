from django.db import models
from django.utils.timezone import now

car_types = (
    ('Sedan', u'Sedan'),
    ('SUV', u'SUV'),
    ('Wagon', u'Wagon'),
)

# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, null=True)
    dealer_id = models.IntegerField()
    car_type = models.CharField(max_length=200, choices=car_types,  null=True)
    year = models.DateField()

    def __str__(self):
        return self.car_make


class DealerReview(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    dealership = models.CharField(max_length=200, null=True)
    review = models.CharField(max_length=500, null=True)
    purchase = models.BooleanField(default=False)

    def __str__(self):
        return self.id
# <HINT> Create a plain Python class `CarDealer` to hold dealer data
# <HINT> Create a plain Python class `DealerReview` to hold review data


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object