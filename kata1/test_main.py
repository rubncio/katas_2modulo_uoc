from main import sumarstring

def test_sumarstring1():
    assert sumarstring("1")==1

def test_sumarstring0():
    assert sumarstring("")==0

def test_sumarstring123():
    assert sumarstring("1,2,3")==6

def test_sumarstring12():
    assert sumarstring("1,2")==3

def test_sumarstringn():
    assert sumarstring("\n")==0

def test_sumarstring1n23():
    assert sumarstring("1\n2,3")==6

def test_sumarstring1n2():
    assert sumarstring("1\n2")==3

"""def test_sumarstring123():
    assert sumarstring("1,  ,2,3")==6"""