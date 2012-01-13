from setuptools import find_packages
from setuptools import setup
import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


version = read('hexagonit', 'portletstyle', 'version.txt').strip()

long_description = (
    read('hexagonit', 'portletstyle', 'docs', 'README.rst') +
    read('hexagonit', 'portletstyle', 'docs', 'FUTURE.rst') +
    read('hexagonit', 'portletstyle', 'docs', 'CREDITS.rst') +
    read('hexagonit', 'portletstyle', 'docs', 'HISTORY.rst') +
    read('hexagonit', 'portletstyle', 'docs', 'LICENSE.rst'))


setup(name='hexagonit.portletstyle',
      version=version,
      description="Assign a CSS style to a portlet",
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
      url='http://hexagonit.fi',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['hexagonit'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'collective.monkeypatcher',
          'manuel',
          'mock',
          'plone.app.registry',
          'plone.app.testing',
          'plone.app.z3cform',
          'plone.browserlayer',
          'plone.portlet.collection',
          'plone.portlet.static',
          'setuptools',
          'unittest2',
          'z3c.jbot',
          'zope.i18nmessageid',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
