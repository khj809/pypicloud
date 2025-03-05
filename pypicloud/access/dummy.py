""" Backend that accepts any dummy value of Basic Authorization header """
from .config import ConfigAccessBackend


class DummyAccessBackend(ConfigAccessBackend):
    """
    This backend accepts any dummy values of Basic Authorization header as long as
    the format of Authorization header is a valid Basic Auth.
    """

    def __init__(self, request=None, **kwargs):
        super(DummyAccessBackend, self).__init__(request, **kwargs)
    
    def verify_user(self, username, password):
        return True

    def _get_password_hash(self, username):
        # We don't have to do anything here because we overrode 'verify_user'
        pass
