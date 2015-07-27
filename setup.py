try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description':'String parsing and utilities',
	'author':'Ismail Elouafiq',
	'url':'https://github.com/nidhog/parsley',
	'download_url':'https://github.com/nidhog/parsley/archive/parsley.zip',
	'author_email':'i.elouafiq@gmail.com',
	'version':'0.1',
	'install_requires':['nose'],
	'packages':['parsley'],
	'scripts':[],
	'name':'Parsley'
}

setup(**config)