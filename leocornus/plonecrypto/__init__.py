
# __init__.py

"""
the basic initialization work for a plone product.
"""

from Products.CMFCore.utils import ToolInit

from crypto import PloneCryptoTool

__author__ = "Sean Chen"
__email__ = "sean.chen@leocorn.com"

def initialize(context):
    """
    initialize the tool here.
    """

    ToolInit('Plone Cryptography Tool',
             tools = (PloneCryptoTool,),
             icon = 'tool.gif').initialize(context)
