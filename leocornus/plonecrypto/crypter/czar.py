
# czar.py

"""
keyczar implementation for Plone Crypter.
"""

from zope.annotation.interfaces import IAnnotations

from keyczar import keyinfo
from keyczar.keydata import KeyMetadata
from keyczar.readers import Reader
from keyczar.keyczar import GenericKeyczar
from keyczar.keyczar import Crypter
from keyczar.errors import KeyczarError

from base import BaseCrypter

__author__ = "Sean Chen"
__email__ = "sean.chen@leocorn.com"

# key prefix for annotation used for keyczar
KEYCZAR_ANNO_KEY = 'leocornus.plonecrypto.crypter.keyczar'

class PloneKeyczarCrypter(BaseCrypter):
    """
    depends on keyczar-python to imeplement Plone Crypter.
    """

    def __init__(self, context):

        self.context = context
        self.metaKey = '%s.%s' % (KEYCZAR_ANNO_KEY, 'meta')
        self.anno = IAnnotations(self.context)

        if not self.anno.has_key(self.metaKey):
            # create one with default settings.
            self.createKeyset()
            self.addPrimaryKey()

    def createKeyset(self, asymmetric=keyinfo.RSA_PRIV):
        """
        create a new keyset and save to the annotation
        """

        name = 'PloneCrypter'
        # only using the encrypt/decrypt purpose for now.
        purpose = keyinfo.DECRYPT_AND_ENCRYPT

        kmd = KeyMetadata(name, purpose, asymmetric)

        self.anno[self.metaKey] = str(kmd)

    def addPrimaryKey(self):
        """
        add a new key as primary key.
        """

        keyczar = GenericKeyczar(AnnotationReader(self.context))
        status = keyinfo.PRIMARY
        size = None
        keyczar.AddVersion(status, size)

        # update the key storage.
        self.anno[self.metaKey] = str(keyczar.metadata)
        for v in keyczar.versions:
            keyKey = '%s.%s' % (KEYCZAR_ANNO_KEY, str(v.version_number))
            self.anno[keyKey] = str(keyczar.GetKey(v))

    def clearKeys(self):
        """
        remove the key metadata and destroy all keys.
        """

        keyczar = GenericKeyczar(AnnotationReader(self.context))
        for v in keyczar.versions:
            keyKey = '%s.%s' % (KEYCZAR_ANNO_KEY, str(v.version_number))
            self.anno.pop(keyKey)

        self.anno.pop(self.metaKey)

    def encrypt(self, message):

        crypter = Crypter(AnnotationReader(self.context))
        return crypter.Encrypt(message)

    def decrypt(self, message):

        crypter = Crypter(AnnotationReader(self.context))
        return crypter.Decrypt(message)

class AnnotationReader(Reader):
    """
    using annotations to store the metadata and keys.
    """

    def __init__(self, context):

        self.context = context
        self.anno = IAnnotations(self.context)

    def GetMetadata(self):

        metaKey = '%s.%s' % (KEYCZAR_ANNO_KEY, 'meta')
        return self.anno[metaKey]

    def GetKey(self, version_number):

        versionKey = '%s.%s' % (KEYCZAR_ANNO_KEY, version_number)
        return self.anno[versionKey]

# testing purpose implementation.
class FileKeyczarCrypter(BaseCrypter):
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
