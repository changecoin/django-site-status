import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-site-status',
    version='0.1.2',
    packages=['site_status'],
    include_package_data=True,
    license='BSD License',  # example license
    description='A simple Django app to issue site wide alerts',
    long_description=README,
    url='https://github.com/changecoin/django-site-status',
    author='Mantas Vidutis',
    author_email='mantas@turbines.io',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    requires=['django'],
)