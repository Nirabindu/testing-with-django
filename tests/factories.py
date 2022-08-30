import factory
from django.contrib.auth.models import User
from faker import Faker 
from core.app1 import models



fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    
    # this is default parameter to User table 
    # username = "user1"
    # is_stuff = 'True'
    # creating random data using faker
    
    username = fake.name()
    is_staff='True'
    

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category
        
    # for i in range(3):
    #     name = 
    name = "T-Shirt"
    
 
# passing foreign key here
class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product
        

    # these data should be in the data base in the time of test call or override those static value while we pass these data from parameterize
    title = 'round-nack'
    category = factory.SubFactory(CategoryFactory)
    description = fake.text()
    slug = fake.slug()
    regular_price = "9.99"

    
    