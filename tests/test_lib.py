from mlproject.lib import hello_world
from mlproject.lib import try_me

def test_length_of_hello_world():
    assert len(hello_world()) != 0
    
def test_try_me():
    assert len(try_me()) != 0