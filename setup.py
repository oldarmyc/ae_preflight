
from setuptools import setup
from setuptools import find_packages


setup(
    name='aepreflight',
    version='0.1.0',
    url='https://github.com/oldarmyc/ae_preflight.git',
    license='BSD',
    author='Dave Kludt',
    author_email='dkludt@anaconda.com',
    description='Library to interact with swift containers',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=['psutil'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
