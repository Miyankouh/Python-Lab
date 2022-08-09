import pytest
import tow


class TestTow:
    def test_add(self):
        assert tow.add(4, 5) == 9 
        assert tow.add(-1, 4) == 3 
    
    def test_subtract(self):
        assert tow.subtract(5, 0) == 5

    def test_multiply(self):
        assert tow.multiply(7, 0) == 0
    
    def test_division(self):
        assert tow.division(30, 5) == 6
        with pytest.raises(ZeroDivisionError): # except
            tow.division(3, 0)
