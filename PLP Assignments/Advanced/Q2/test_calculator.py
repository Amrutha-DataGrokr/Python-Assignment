import pytest
from calculator import add,subtract,multiply,divide

#a) Fixture
@pytest.fixture
def sample_values():
    return {
        "a":10,
        "b":5,
        "expected_sum":15
    }

#b) Test add using fixture
def test_add_positive(sample_values):
    assert add(sample_values["a"],sample_values["b"])==sample_values["expected_sum"]

#c) Parametrized test for multiply
@pytest.mark.parametrize("a,b,expected",[(2,3,6),(4,5,20),(-2,5,-10),(-2,-2,4)])
def test_multiply(a,b,expected):
    assert multiply(a,b)==expected

#d) i:Test divide with pytest.raises
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10,0)

# ii: Edge case
def test_divide_zero():
    assert divide(0,10)==0.0

