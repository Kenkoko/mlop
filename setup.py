"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# To use a consistent encoding
from codecs import open
from os import path

# Always prefer setuptools over distutils
from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    # <---- Important ---->
    name='mlop',  # A convenient name
    version='0.1.0',  # A version number
    packages=find_packages(),
    # The directory of your code / will also be the name of your package
    install_requires=[
        'onnx',
        'onnxruntime',
        'scipy',
        'scikit-learn',
        'clearml',
        'matplotlib',
        'pandas',
        'numpy',
    ],  # All its dependencies
    description='Generates Pipeline',  # Required
    # <------ Optional ----->
    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        # Pick your license as you wish
        'License :: Other/Proprietary License',
        # Specify the Python versions you support here.
        # 'Programming Language :: Python :: 3.5',
        # 'Programming Language :: Python :: 3.6',
        # 'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='physics',  # Optional
    #   $ pip install package-name[test]
    extras_require={  # Optional
        'test': ['pytest', 'pytest-cov', 'pandas'],  # Testing
        'docs': [  # Building the docs
            'sphinx',
            'sphinx-rtd-theme',
        ],
        'dev': [  # Linting and autoformatting
            'black',
            'pylint',
        ],
    },
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    # entry_points={  # Optional
    #     'console_scripts': [
    #         (
    #         ),
    #     ],
    # },
    # <------ Don't change ---->
    # Meta information
    url='http://www.kognif.ai',  # Optional
    author='Kongsberg Digital AS',  # Optional
    # Specifies where to look for the long description
    long_description=long_description,  # Imports the
    long_description_content_type='text/markdown',  # Optional (see note above)
)
