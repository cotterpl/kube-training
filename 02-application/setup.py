import re

import setuptools

with open("VERSION.txt") as fh:
    VERSION = fh.read()

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.in", "r") as fh:
    install_requires = [line.rstrip('\n') for line in fh.readlines()]
    install_requires = [re.sub(r'#.*', '', line).strip() for line in install_requires]  # remove comments
    install_requires = [line for line in install_requires if line != '']  # remove empty lines

setuptools.setup(
    name='myapp',
    version=VERSION,
    packages=setuptools.find_packages(),
    url='https://github.com/cotterpl/kube-training',
    description='Simple application for Kubernetes training',
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.8',
        "Operating System :: Linux",
    ],
    install_requires=install_requires,
)
