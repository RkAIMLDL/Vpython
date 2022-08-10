import  mthlib
import pytest
@pytest.mark.skip(reason="i dont want to run this test at the moment")

def test_calc_total():
    total=mthlib.calc_total(4,5)
    assert  total==9

def test_calc_multiply():
    result=mthlib.calc_multiply(10,3)
    assert  result==30