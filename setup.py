# stdlib
import os
from setuptools import setup, find_packages


# Use register to create temporary README.txt from README.md.
# Default incase README.txt was not created
long_description = 'Prepare and send emails using jinja2, and envelopes.'
if os.path.exists('README.txt'): long_description = open('README.txt').read()


# Setup Package
setup(
    name = 'email-courier',
    version = '0.0.1',
    description = 'Prepare and send emails using jinja2, and envelopes.',
    long_description = long_description,
    keywords = 'Email, Templating',
    url = 'firstopinion.github.io/courier',
    author = 'Jarid Margolin',
    author_email = 'jaridmargolin@gmail.com',
    license ='MIT',
    install_requires = [
		'Jinja2==2.7',
        'flexmock==0.9.4',
        'envelopes==0.2'
	],
    packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    test_suite = "tests"
)