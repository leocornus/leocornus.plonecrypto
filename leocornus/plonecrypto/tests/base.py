
# base.py

"""
The base unit test cases for Leocornus Plone Cryptography toolkit
"""

from Testing import ZopeTestCase

from Products.Five import zcml
from Products.Five import fiveconfigure

from Products.PloneTestCase import PloneTestCase
from Products.PloneTestCase.layer import onsetup

import leocornus.plonecrypto

__author__ = "Sean Chen"
__email__ = "sean.chen@leocorn.com"

# base package for testing Plone cryptography toolkit.

@onsetup
def setup_product():
    """
    we need install our product so the testing zope server know it.
    """

    fiveconfigure.debug_mode = True
    zcml.load_config('configure.zcml', leocornus.plonecrypto)
    ZopeTestCase.installPackage('leocornus.plonecrypto')

setup_product()
# we need a Plone site for some of the module.
PloneTestCase.setupPloneSite(products=['leocornus.plonecrypto'])

# base test case for our product.
class PlonecryptoTestCase(PloneTestCase.PloneTestCase):
    """
    General steps for all test cases.
    """

    def afterSetUp(self):

        self.loginAsPortalOwner()

class PlonecryptoFunctionalTestCase(PloneTestCase.FunctionalTestCase):
    """
    base test case class for functional test case.
    """

    def afterSetUp(self):

        self.loginAsPortalOwner()
