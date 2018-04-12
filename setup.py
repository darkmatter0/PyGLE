import os

from setuptools import setup

import pygle
from setuptools import find_packages


version = pygle.__version__
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def packages():
    return find_packages(include=['pygle'], exclude=['pygle/dev'])

def read_md(f):
    try:
        from pypandoc import convert
        try:
            rst = convert(os.path.join(THIS_DIR, f), 'rst')
            return rst
        except Exception as e:
            print("error: %s" % e)
            return "PyGLE"
    except ImportError:
        print("warning: pypandoc module not found, could not convert Markdown to RST")
        try:
            with open(os.path.join(THIS_DIR, f), 'r') as f_in:
                return f_in.read()
        except Exception as e:
            print("error: %s" % e)
            return "PyGLE"

setup(
    name='pygle',
    packages=['pygle',
              ],
    version=version,
    description='API wrapper for WiGLE',
    long_description=read_md('README.md'),
    author='Jamie Bull',
    author_email='jamie.bull@oco-carbon.com',
    url='https://github.com/jamiebull1/pygle',
    download_url='https://github.com/jamiebull1/pygle/tarball/v%s' % version,
    license='MIT License',
    keywords=['WiGLE',
              'WiFi',
              'mapping',
              ],
    platforms='any',
    install_requires = [
        "requests>=2.13.0",
        ],
    classifiers = [
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        ],
)
