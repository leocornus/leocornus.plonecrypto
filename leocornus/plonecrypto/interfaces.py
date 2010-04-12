
# interfaces.py

"""
define the interfaces for leocornus.plonecrypto.
"""

from zope.interface import Interface
from zope.interface import Attribute

__author__ = "Sean Chen"
__email__ = "sean.chen@leocorn.com"

class IPloneCryptoTool(Interface):
    """
    providing easy way for cryptography in Plone
    """

    id = Attribute('id', 'Must set to "leocornus_crypto"')

class IPloneCrypter(Interface):
    """
    providing the APIs for doing cryptography in a Plone site.
    """

    def encrypt(message):
        """
        Return an encrypted message for the given raw message.
        """

    def decrypt(message):
        """
        Return the raw message for the given encrypted message.
        """
