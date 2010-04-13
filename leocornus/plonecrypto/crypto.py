
# crypto.py

"""
implements a CMF tool for Plone Cryptography Toolkit to store keys and provide
a management panel.
"""

from Globals import InitializeClass
from AccessControl import ClassSecurityInfo

from zope.interface import implements

from Products.CMFCore.permissions import ManagePortal
from Products.CMFCore.utils import UniqueObject
from Products.CMFCore.utils import SimpleItemWithProperties
from Products.CMFCore.utils import registerToolInterface

from Products.PageTemplates.PageTemplateFile import PageTemplateFile

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
        { 'id' : 'title',
          'type' : 'string',
          'mode' : 'w',
          'label' : 'Title'
          },
        )

    title = "Plone Cryptographic Tool"

    manage_options = (
        { 'label':      'Keys',
          'action':     'manage_keys' },
        ) + SimpleItemWithProperties.manage_options

    manage_keys = PageTemplateFile("crypter/czar.pt", globals())

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

    security.declareProtected(ManagePortal, 'manage_addNewKey')
    def manage_addNewKey(self, REQUEST=None):
        """
        create a new key for cryptography
        """

        self.crypter.addPrimaryKey()

        if REQUEST:
            REQUEST.RESPONSE.redirect('%s/manage_keys?manage_tabs_message=%s' %
                                      (self.absolute_url(), 'New+key+created.'))

    security.declareProtected(ManagePortal, 'manage_clearAndRegenerate')
    def manage_clearAndRegenerate(self, REQUEST=None):
        """
        Clear all existing keys and create a new keyset.
        """

        self.crypter.clearKeys()
        self.crypter

        if REQUEST:
            REQUEST.RESPONSE.redirect('%s/manage_keys?manage_tabs_message=%s' %
                                      (self.absolute_url(), 'All+keys+cleared.'))

InitializeClass(PloneCryptoTool)
registerToolInterface('leocornus_crypto', IPloneCryptoTool)
