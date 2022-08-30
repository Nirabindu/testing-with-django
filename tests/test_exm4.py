import pytest
from tests.factories import UserFactory,ProductFactory,CategoryFactory

def test_new_user(db,user_factory):
    
    # return an user instance that not saved
    user = user_factory.build()
    
    # Returns a saved User instance to test database.
    user = user_factory.create()
    print(user.username)
    assert True
 
 
#  just check for random item create by faker   
def test_category(db,category_factory):
    category = category_factory.create()
    print(category.name)
    assert True

# create random data and implementing foreign key
def test_product(db,product_factory):
    product = product_factory.create()
    print(product.title)
    print(product.category.name)
    print(product.description)
    print(product.slug)
    print(product.regular_price)
    
    assert True