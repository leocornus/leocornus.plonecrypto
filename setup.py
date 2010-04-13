from setuptools import setup, find_packages
import os

version = open(os.path.join('leocornus/plonecrypto', 'version.txt')).read().split('\n')[0]

setup(name='leocornus.plonecrypto',
      version=version,
      description="Plone Cryptographic Toolkit",
      long_description=open(os.path.join('leocornus/plonecrypto', "README.txt")).read() + "\n" +
                       open(os.path.join("leocornus/plonecrypto", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Zope",
        "Topic :: Security :: Cryptography",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        ],
      keywords='Python Plone Zope Cryptography',
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
