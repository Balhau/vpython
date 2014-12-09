from distutils.core import setup
import os
import codecs
from setuptools import setup, find_packages


pname="balhau-violent-python"

#packages=[pname]+[pname+ "." + name
#	for name in os.listdir(os.path.join(pname)) if os.path.isdir(os.path.join(pname, name))]

current_dir=os.path.dirname(__file__)

with codecs.open(os.path.join(current_dir,'README.md'),'r','utf8') as readme_file:
		long_description=readme_file.read()

setup(	name='balhau-violent-python',
	version='1.0',
	url='https://github.com/balhau',
	license='MIT License',
	description='A bunch of python scripts with agressive purposes',
	long_description=long_description,
	packages=find_packages())
