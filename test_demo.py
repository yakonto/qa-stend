import pytest

@pytest.fixture()
def before_tst_dem1():
    print("before-test_dem1")
    yield

def test_dem1():
    assert 1==1
    print("Demo 1")

def test_dem2(before_tst_dem1):
    assert 2==2
    print("Demo 2")