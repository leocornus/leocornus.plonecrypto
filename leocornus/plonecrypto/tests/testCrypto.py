
# testCrypto.py

"""
test cases for Plone Cryptography CMF Tool.
"""

import unittest

from Products.CMFCore.utils import getToolByName

from keyczar.errors import KeyNotFoundError

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

        self.assertEquals(crypto.getProperty('title'),
                          'Plone Cryptographic Tool')

class CryptoTestCase(PlonecryptoTestCase):

    def testEncryptAndDecrypt(self):

        crypto = getToolByName(self.portal, 'leocornus_crypto')

        rawMsg = "hello world!"

        encrypted = crypto.encrypt(rawMsg)
        self.failIf(encrypted == rawMsg)

        decrypted = crypto.decrypt(encrypted)
        self.failUnless(decrypted == rawMsg)

        crypto.crypter.addPrimaryKey()
        encryptedNew = crypto.encrypt(rawMsg)
        self.failIf(encryptedNew == rawMsg)
        self.failIf(encryptedNew == encrypted)

        stillGood = crypto.decrypt(encrypted)
        self.failUnless(stillGood == rawMsg)
        self.failUnless(stillGood == decrypted)
    
        decryptedNew = crypto.decrypt(encryptedNew)
        self.failUnless(decryptedNew == rawMsg)
        self.failUnless(decrypted == decryptedNew)

    def testManageKeys(self):

        crypto = getToolByName(self.portal, 'leocornus_crypto')
        rawMsg = 'Good Tool!'

        first = crypto.encrypt(rawMsg)
        self.failIf(first == rawMsg)
        first_d = crypto.decrypt(first)
        self.failUnless(first_d == rawMsg)

        anno = crypto.__annotations__
        self.failUnless(len(anno.keys()) == 2)

        crypto.manage_addNewKey()
        self.failUnless(len(anno.keys()) == 3)

        second = crypto.encrypt(rawMsg)
        self.failIf(first == second)
        second_d = crypto.decrypt(second)
        self.failUnless(second_d == rawMsg)
        # after create a new key, the previous encrypted message
        # still can be decrypted properly!
        first_d_again = crypto.decrypt(first)
        self.failUnless(first_d_again == rawMsg)

        crypto.manage_clearAndRegenerate()
        self.failUnless(len(anno.keys()) == 2)

        third = crypto.encrypt(rawMsg)
        self.failIf(third == rawMsg)
        self.failIf(third == first)
        self.failIf(third == second)
        third_d = crypto.decrypt(third)
        self.failUnless(third_d == rawMsg)
        # now after clear and regenerate keys, none of the previous encrypted
        # message could be decrypted properly!
        self.assertRaises(KeyNotFoundError, crypto.decrypt, second)
        self.assertRaises(KeyNotFoundError, crypto.decrypt, first)

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(InstallationTestCase))
    suite.addTest(unittest.makeSuite(CryptoTestCase))
    return suite
