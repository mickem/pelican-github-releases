from os.path import abspath, dirname, join, normpath
from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(

    # Basic package information:
    name = 'pelican-advthumbnailer',
    version = '0.4.0',
    py_modules = ('advthumbnailer',),

    # Packaging options:
    zip_safe = False,
    include_package_data = True,

    # Package dependencies:
    install_requires = ['pelican>=3.4.0', 'requests>=2.8.1'],

    # Metadata for PyPI:
    author = 'Michael Medin',
    author_email = 'michael@medin.name',
    license = 'GPLv2',
    url = 'https://github.com/mickem/pelican-github-releases',
    download_url = 'https://github.com/mickem/pelican-github-releases/zipball/0.0.1',
    keywords = 'pelican blog static release github',
    description = ('A plugin which generates release pages (for downloading artifacts) based on a github project releases'),
    use_2to3 = True,
    long_description = long_description
)
