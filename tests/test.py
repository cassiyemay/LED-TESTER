from nose.tools import *
from src.main import *

def test_1():
    filename = 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt'
    buffer = read_file(filename = filename)
    eq_(readline(), 301, 'buffer sizes do not match')
    
def test_count():
    line = "turn, on, 0, 0, through, 9, 9"
    line = "turn, off, 0, 0, through, 9, 9"
    res = count()
    eq_(res,400410, "{}".format(res))
    
    
    
    