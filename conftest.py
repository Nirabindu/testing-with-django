import pytest
from pytest_factoryboy import register
# from test import factories
from tests.factories import *



register(UserFactory)
register(CategoryFactory)
register(ProductFactory)
