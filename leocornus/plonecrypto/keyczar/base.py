
# base.py

"""
Plone crypter's base implementation by using keyczar 
"""

from zope.interface import implements

from keyczar.keyczar import Crypter
from keyczar.errors import KeyczarError

from leocornus.plonecrypto.interfaces import IPloneCrypter

__author__ = "Sean Chen"
__email__ = "sean.chen@leocorn.com"

class BaseKeyczarCrypter(object):
    """
    the base class for keyczar crypter.  Only includes generic functions,
    no exact implementation yet!
    """

    implements(IPloneCrypter)

    def __init__(self, context):

        self.context = context

    def encrypt(self, message):

        raise NotImplemented

    def decrypt(self, message):

        raise NotImplemented

class FileCrypter(BaseKeyczarCrypter):
    """
    A Keyczar crypter implementation based on default File reader.
    """

    def __init__(self, context):

        self.context = context
        self.crypter = Crypter.Read('/usr/local/rd/keyczar/rsa-keys')

    def encrypt(self, message):

        return self.crypter.Encrypt(message)

    def decrypt(self, message):

        return self.crypter.Decrypt(message)
