from nose.tools import *
from src.LED_tester import *
from src.main import read_file

def test_1():
    filename = 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt'
    buffer = read_file(filename = filename)
    eq_(len(buffer), 300, 'buffer sizes do not match')
    
def test_readline():
    
    