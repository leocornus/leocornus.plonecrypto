
# base.py

"""
Plone crypter's base implementation by using keyczar 
"""

from zope.interface import implements

from leocornus.plonecrypto.interfaces import IPloneCrypter

__author__ = "Sean Chen"
__email__ = "sean.chen@leocorn.com"

class BaseCrypter(object):
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
