
# testCrypto.py

"""
test cases for Plone Cryptography CMF Tool.
"""

import unittest

from Products.CMFCore.utils import getToolByName

from base import PlonecryptoTestCase

__author__ = "Sean Chen"
__email__ = "sean.chen@leocorn.com"

class InstallationTestCase(PlonecryptoTestCase):
    """
    make sure plonecrypto tool has been installed properly
    """

    def testInstallation(self):

        self.failUnless(hasattr(self.portal, 'leocornus_crypto'))
        self.failUnless(getattr(self.portal, 'leocornus_crypto'))

    def testCryptoBasic(self):

        crypto = getToolByName(self.portal, 'leocornus_crypto')
        self.failUnless(crypto)

        self.assertEquals(crypto.getProperty('favorite_color'), 'testing ...')
        self.assertEquals(crypto.getProperty('contact_email'), '')

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(InstallationTestCase))
    return suite
