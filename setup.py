from setuptools import find_packages
from setuptools import setup
import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


version = read('hexagonit', 'portletclass', 'version.txt').strip()

long_description = (
    read('hexagonit', 'portletclass', 'docs', 'README.rst') +
    read('hexagonit', 'portletclass', 'docs', 'FUTURE.rst') +
    read('hexagonit', 'portletclass', 'docs', 'CREDITS.rst') +
    read('hexagonit', 'portletclass', 'docs', 'HISTORY.rst') +
    read('hexagonit', 'portletclass', 'docs', 'LICENSE.rst'))


setup(name='hexagonit.portletclass',
      version=version,
      description="Assign a CSS class to portlet",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Hexagon IT',
      author_email='oss@hexagonit.fi',
      url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['hexagonit'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'manuel',
          'mock',
          'plone.app.testing',
          'plone.app.registry',
          'plone.app.z3cform',
          'plone.browserlayer',
          'setuptools',
          'unittest2',
          'zope.i18nmessageid',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
