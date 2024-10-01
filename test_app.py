""" tests the app """
from app import version

def test_version():
    """ tests the version route """
    assert version() == 'v0.0.1'
