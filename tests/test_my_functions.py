import pytest
import src.my_functions as my_functions
import time 

def test_add():
    result = my_functions.add(1,4)
    assert result == 5

def test_add_strings():
    result = my_functions.add("i like", " burgers")
    assert result == "i like burgers"
def test_divide():
    result = my_functions.divide(10, 5)
    assert result == 2

# test FOR errors
def test_divide_by_zero():
    with pytest.raises(ValueError):
      my_functions.divide(10,0)



# mark
# pytest -m slow
@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.add(1,4)
    assert result == 5


#skip test

@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
    assert my_functions.add(1,2) == 3

# xfail, we know that this should fail
@pytest.mark.xfail(reason="we know we cannot divide by 0")
def test_divide_zero_broken():
    my_functions.divide(4,0)