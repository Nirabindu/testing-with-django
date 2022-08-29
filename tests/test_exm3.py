# using database
import pytest
from django.contrib.auth.models import User

# @pytest.mark.django_db
# def test_user_create():
#     User.objects.create_user('test','test@test.com','test')
#     count = User.objects.all().count()
#     assert User.objects.count() == 1


# @pytest.mark.django_db
# def test_user_create():
#     count = User.objects.all().count()
#     assert count == 0 


# using fixture we bring the database to the function
# @pytest.mark.django_db or db
# this is Arrange
@pytest.fixture()
def user_1(db):
    print("dont know")
    return User.objects.create_user("test-user")

# @pytest.mark.django_db
# db is getting from the above fixture
 
def test_set_check_password(user_1):
    # print(user_1.username)
    user_1.set_password("new-password")  #act or action
    assert user_1.check_password("new-password") is True #assert
    
def test_user_name(user_1):
    # print("2nd time")
    assert user_1.username == "test-user"