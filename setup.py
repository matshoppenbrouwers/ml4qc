#  Copyright (c) 2022 Orange Chair Labs LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from setuptools import setup

with open('README.rst') as file:
    readme = file.read()

setup(
    name='ml4qc',
    version='0.1.9',
    packages=['ml4qc'],
    python_requires='>=3.7',
    install_requires=['pandas', 'numpy', 'scikit-learn', 'seaborn', 'matplotlib', 'tensorflow', 'importlib_metadata',
                      'k-means-constrained'],
    package_dir={'': 'src'},
    url='https://github.com/orangechairlabs/ml4qc',
    project_urls={'Documentation': 'https://ml4qc.readthedocs.io/'},
    license='Apache 2.0',
    author='Christopher Robert',
    author_email='crobert@orangechairlabs.com',
    description='Toolkit for ML-based survey quality control',
    long_description=readme
)
