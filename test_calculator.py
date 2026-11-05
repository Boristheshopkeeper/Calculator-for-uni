from calculator import add, subtract, multiply, divide

def test_add():
	assert add(2, 3) == 5

def test_divide():
	assert divide(6, 2) == 3

def test_subract():
	assert  subtract(5, 3) == 2

def test_multiply():
	assert multiply(4, 3) == 12

def test_divide_uneven():
	a, b = 5, 2 
	result = divide(a, b)
	assert result == 2.5
