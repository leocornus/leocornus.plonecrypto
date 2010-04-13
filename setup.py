from setuptools import setup, find_packages
import os

version = open(os.path.join('leocornus/plonecrypto', 'version.txt')).read()

setup(name='leocornus.plonecrypto',
      version=version,
      description="Plone Cryptographic Toolkit",
      long_description=open(os.path.join('leocornus/plonecrypto', "README.txt")).read() + "\n" +
                       open(os.path.join("leocornus/plonecrypto", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Zope :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules :: Plone Tool",
        ],
      keywords='Python Plone Zope cryptography',
      author='Sean Chen',
      author_email='sean.chen@leocorn.com',
      url='http://plonexp.leocorn.com/xp/leocornus.plonecrypto',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['leocornus'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
