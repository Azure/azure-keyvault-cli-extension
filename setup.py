#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from codecs import open
from setuptools import setup, find_packages

VERSION = "0.1.1"

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'License :: OSI Approved :: MIT License',
]
DEPENDENCIES = [
    'cryptography>=2.1.4',
    'requests>=2.18.4',
    'pyOpenSSL'
]

setup(
    name='keyvault_preview',
    version=VERSION,
    description='An Azure CLI Extension providing support for Azure Key Vault preview commands.',
    long_description='An Azure CLI Extension providing support for Azure Key Vault preview commands.',
    license='MIT',
    author='Azure Key Vault',
    author_email='azurekeyvault@microsoft.com',
    url='https://github.com/Azure/azure-keyvault-cli-extension',
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    install_requires=DEPENDENCIES
)