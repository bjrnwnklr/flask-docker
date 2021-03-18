from setuptools import setup, find_packages

setup(
    name='flaskexampleapp',
    author='Bjoern Winkler',
    description='A flask / docker example app',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
