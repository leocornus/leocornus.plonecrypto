
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
from Products.CMFPlone.PropertiesTool import SimpleItemWithProperties
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

    manage_options = (
        { 'label':      'Keys',
          'action':     'manage_keys' },
        ) + SimpleItemWithProperties.manage_options

    manage_keys = PageTemplateFile("crypter/czar.pt", globals())

    def __init__(self, id, title="Plone Cryptographic Tool"):
        self.id = id
        self.title = title

    @property
    def enableLog(self):

        return self.getProperty('enable_log', False)

    @property
    def maximumKeysAmount(self):
        """
        the maximum keys amount that we will be stored!  the value -1 means
        unlimited!
        """

        return self.getProperty('max_keys_amount', -1)

    @property
    def crypter(self):

        return IPloneCrypter(self)

    def getLogs(self):

        return self.crypter.getLogs()

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
        if (self.maximumKeysAmount > 0) and \
           (self.crypter.keysAmount() > self.maximumKeysAmount):
            # demote/remove the oldest one!
            self.crypter.removeOldestKey()

        if REQUEST:
            REQUEST.RESPONSE.redirect('%s/manage_keys?manage_tabs_message=%s' %
                                      (self.absolute_url(), 'New+key+created.'))

    security.declareProtected(ManagePortal, 'manage_clearAndRegenerate')
    def manage_clearAndRegenerate(self, REQUEST=None):
        """
        Clear all existing keys and create a new keyset.
        """

        self.crypter.clearKeys()

        if REQUEST:
            REQUEST.RESPONSE.redirect('%s/manage_keys?manage_tabs_message=%s' %
                                      (self.absolute_url(), 'All+keys+cleared.'))

    security.declareProtected(ManagePortal, 'manage_clearLogs')
    def manage_clearLogs(self, REQUEST=None):
        """
        create a new key for cryptography
        """

        self.crypter.clearLogs()

        if REQUEST:
            REQUEST.RESPONSE.redirect('%s/manage_keys?manage_tabs_message=%s' %
                                      (self.absolute_url(), 'All+logs+removed.'))

InitializeClass(PloneCryptoTool)
registerToolInterface('leocornus_crypto', IPloneCryptoTool)
