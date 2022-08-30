import pytest


# @pytest.mark.skip
# @pytest.mark.xfail
@pytest.mark.slow
def test_example():
    print("test1")
    assert 1==1


# # using fixture
@pytest.fixture(scope="session")
def fix_1():
    print("run fixture 1")
    return 1

def test_using_fixture(fix_1):
    num = fix_1
    assert num ==1

def test_checking_scope(fix_1):
    num = fix_1
    assert num == 1    