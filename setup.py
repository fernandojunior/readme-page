'''
Contains informations necessaries to build, release and install a distribution.
'''
from setuptools import setup
from pip.req import parse_requirements as parse


# Read the README file
with open("README.md") as f:
    README = f.read()

# Parse a requirements file to string list
requirements = lambda f: [str(i.req) for i in parse(f, session=False)]

setup(
    name='readme-page',
    version='0.0.1',
    author='Fernando Felix do Nascimento Junior',
    author_email='fernandojr.ifcg@live.com',
    url='https://github.com/fernandojunior/readme-page',
    license='MIT License',
    description='A script to create a simple readme GitHub Page for your project.',
    long_description=README,
    platforms='ANY',
    install_requires=requirements('requirements.txt'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],  # see more at https://pypi.python.org/pypi?%3Aaction=list_classifiers
    zip_safe=False,
    scripts=['readme-page']
)
