import unittest

def test_a():
    assert True == True

def test_b():
    assert "aa" == "aa"

def test_c():
    print "[[ATTACHMENT|/absolute/path/to/some/file]]"
    assert "aa" == "aa"

def test_d():
    f = open("test_d.txt","w+")
    f.write("My new test")
    f.close()
    print "[[ATTACHMENT|/absolute/path/to/some/file]]"
    assert "aa" == "aa"

def test_j():
    f = open("test_j.txt","w+")
    f.write("My new test")
    f.close()
    assert "aa" == "aa"

@unittest.skip("temporarily disabled")
def test_k():
    assert "aa" == "aa"

@unittest.skip("temporarily disabled")
def test_l():
    assert "aa" == "aa"
