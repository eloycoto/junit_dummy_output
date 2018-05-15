import unittest

def test_a():
    assert True == True

def test_b():
    assert "aa" == "aa"

def test_c():
    print "[[ATTACHMENT|/absolute/path/to/some/file]]"
    assert "aa" == "aa123"

def test_d():
    print "[[ATTACHMENT|/absolute/path/to/some/file]]"
    assert "aa" == "aa"

def test_j():
    assert "aa" == "aa"

@unittest.skip("temporarily disabled")
def test_k():
    assert "aa" == "aa"

@unittest.skip("temporarily disabled")
def test_l():
    assert "aa" == "aa"
