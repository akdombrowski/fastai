
# coding: utf-8

"""
Setup script for installing fastai
"""

##########################################################################
## Imports
##########################################################################

#from distutils.core import setup
from setuptools import setup


##########################################################################
## Setup
##########################################################################

setup(
    name = "fastai",

    packages = ['fastai', 'fastai/models', 'fastai/models/cifar10'], # this must be the same as the name above

    version = 1.0 ,

    description = "The fast.ai deep learning and machine learning library. Git pull fastai, for all fast.ai sessions and tutorials also",
    
    author = "Jeremy Howard, Rachel Thomas, Yannet Interian and many others",
    
    author_email = "j@fast.ai",

    license = "GNU General Public License",
    
    url = "https://github.com/fastai/fastai",
    
    download_url =  'https://github.com/fastai/fastai/archive/1.0.tar.gz',

    install_requires = 
     ['awscli',
     'bcolz',
    # 'docrepr' ,
     'feather-format',
     'graphviz',
     'jupyter_contrib_nbextensions',
     'kaggle-cli',
     'plotnine',
     'sklearn_pandas',
     'torchtext',


   
    keywords = ['deeplearning', 'pytorch', 'machinelearning'],

        classifiers = ['Development Status :: 3 - Alpha',
                      'Programming Language :: Python',
                    'Programming Language :: Python :: 3.6',]
)
