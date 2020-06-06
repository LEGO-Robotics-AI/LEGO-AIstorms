import json
import os
from setuptools import find_packages, setup


PACKAGE_NAMESPACE_NAME = 'ev3ai'

METADATA_FILE_NAME = 'metadata.json'

REQUIREMENTS_FILE_NAME = 'requirements.txt'


_metadata = \
    json.load(
        open(os.path.join(
                os.path.dirname(__file__),
                PACKAGE_NAMESPACE_NAME,
                METADATA_FILE_NAME)))


setup(
    name=_metadata['PACKAGE'],
    author=_metadata['AUTHOR'],
    author_email=_metadata['AUTHOR_EMAIL'],
    url=_metadata['URL'],
    version=_metadata['VERSION'],
    description=_metadata['DESCRIPTION'],
    long_description=_metadata['DESCRIPTION'],
    keywords=_metadata['DESCRIPTION'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=
        [s for s in open(REQUIREMENTS_FILE_NAME).readlines()
           if not s.startswith('#')])
