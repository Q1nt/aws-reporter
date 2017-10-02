from setuptools import setup, find_packages

setup(
    name='aws-reporter',
    version='0.1',
    py_modules=['app'],
    install_requires=[
        'boto3',
        'click'
    ],
    entry_points='''
        [console_scripts]
        aws-reporter=app:reporter
    '''
)
