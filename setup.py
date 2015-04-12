from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='webmock',
    version='1.0.0',
    description='Mock web server for testing web clients',
    long_description=long_description,
    #url='https://github.com/pypa/sampleproject',
    author='Dustin J. Mitchell',
    author_email='dustin@v.igoro.us',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        # TODO (only those tested with tox)
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='mock testing web http',
    packages=['webmock'],
    extras_require={
        'test': ['nose', 'coverage'],
    },
)
