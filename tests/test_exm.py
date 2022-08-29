import pytest


# @pytest.mark.skip
# @pytest.mark.xfail
@pytest.mark.slow
def test_example():
    print("test1")
    assert 1==1