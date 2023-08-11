from setuptools import setup, find_packages

setup(
    name='pycode',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'asgiref==3.7.2',
        'django==4.2.3',
        'sqlparse==0.4.4',
        'typing-extensions==4.7.1',
        'tzdata==2023.3',
        'whitenoise==6.5.0'
    ],
    entry_points={
        'console_scripts': [
            'pycode=pycode.cli:main'
        ]
    }
)
