from calculator import add


# When the input is an empty string, the method should return 0
def test_empty_string_returns_zero():
    assert add("") == 0
    
# Handle a single number like "1" (return 1) and two numbers like "1,2" (return 3).
def test_single_number():
    assert add("1") == 1

def test_two_numbers():
    assert add("1,2") == 3

# Test for multiple comma separated numbers
def test_multiple_numbers():
    assert add("1,2,3,4") == 10

# Test for newlines between numbers. "1\n2,3"
def test_newline_delimiter():
    assert add("1\n2,3") == 6    

# Test for custom  delimiters numbers where numbers string startswith. "//[delimiter]\n[numbers...]"
def test_custom_delimiter():
    assert add("//;\n1;2") == 3