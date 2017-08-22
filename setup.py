import io
import pypandoc
from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from os import path

here = path.abspath(path.dirname(__file__))

# Translate oglhslack README.md to .rst
long_description = pypandoc.convert_file(path.join(here, 'oglhslack/README.md'), 'rst')

# Get the long description from the relevant file
#with io.open(path.join(here, 'README.rst'), encoding='utf-8') as f:
#    long_description = f.read()

setup(
  name = 'oglhslack',
  version = '0.1.5.3',
  description = 'A Slack bot client for Lighthouse API',
  long_description=long_description,
  author = 'Lighthouse Team',
  author_email = 'engineering@opengear.com',
  url = 'https://github.com/opengeardev/oglhslack',
  download_url = 'https://github.com/opengeardev/oglhslack/archive/0.1.5.2.tar.gz',
  keywords = ['api', 'opengear', 'lighthouse', 'slackbot'],
  classifiers = [
    'Development Status :: 3 - Alpha',
    "Intended Audience :: Developers",
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3'
  ],
  install_requires = ['pyyaml', 'slackclient', 'oglhclient', 'requests', 'urllib', 'future'],
  packages=find_packages(),
)
