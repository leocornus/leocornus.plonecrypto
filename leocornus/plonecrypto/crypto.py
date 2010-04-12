
# crypto.py

"""
implements a CMF tool for Plone Cryptography Toolkit to store keys and provide
a management panel.
"""

from Globals import InitializeClass
from AccessControl import ClassSecurityInfo

from zope.interface import implements

from Products.CMFCore.utils import UniqueObject
from Products.CMFCore.utils import SimpleItemWithProperties
from Products.CMFCore.utils import registerToolInterface

from interfaces import IPloneCryptoTool
from interfaces import IPloneCrypter

__author__ = "Sean Chen"
__email__ = "sean.chen@leocorn.com"

class PloneCryptoTool(UniqueObject, SimpleItemWithProperties):
    """
    We implement it to just save some properties!
    """

    implements(IPloneCryptoTool)

    id = 'leocornus_crypto'
    meta_type = 'Plone Cryptographic Tool'

    security = ClassSecurityInfo()

    _properties = (
        { 'id' : 'contact_email',
          'type' : 'string',
          'mode' : 'w',
          'label' : 'Your Contact Email'
          },

        { 'id' : 'favorite_color',
          'type' : 'string',
          'mode' : 'w',
          'label' : 'Your Favorite Color'
          },
        )

    contact_email = ''
    favorite_color = 'testing ...'

    @property
    def crypter(self):

        return IPloneCrypter(self)

    security.declarePrivate('encrypt')
    def encrypt(self, message):
        """
        Return a encrypted message for the given raw message.
        """

        return self.crypter.encrypt(message)

    security.declarePrivate('decrypt')
    def decrypt(self, message):
        """
        Return the raw message from the given encrypted message.
        """

        return self.crypter.decrypt(message)

InitializeClass(PloneCryptoTool)
registerToolInterface('leocornus_crypto', IPloneCryptoTool)
