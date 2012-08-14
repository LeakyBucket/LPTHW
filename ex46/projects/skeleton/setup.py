try:
  from setuptools import setup
except ImportError:
  from distutil.core import setup

config = {
  'description': 'My Project',
  'author': 'Glen Holcomb',
  'url': 'URL to get it at.',
  'download_url': 'Where to download it.',
  'author_email': 'lholcomb2@cnm.edu',
  'version': '0.1',
  'install_requires': ['nose'],
  'packages': ['NAME'],
  'scripts': [],
  'name': 'projectname'
}

setup(**config)