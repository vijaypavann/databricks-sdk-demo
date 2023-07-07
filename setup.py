from setuptools import setup

setup(
    name='databricks-sdk-demo',
    version='1.0',
    packages=['repos', 'secrets', 'spark-connect'],
    url='https://github.com/vijaypavann/databricks-sdk-demo.git',
    license='',
    author='Vijay Pavan N',
    author_email='vijaypavann@gmail.com',
    description='Databricks SDK for Python : Usages and Examples',
    setup_requires=['virtualenv', 'wheel', 'check-wheel-contents'],
    python_requires='>=3'
)
