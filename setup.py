"""
Setup document defining all needed info for creating the package and deploying to pypi.
"""

import os
from setuptools import setup

requires = [
    "xmltodict>=0.13.0",
    "zeep>=4.2.1",
]

about = {}
here = os.path.abspath(os.path.dirname(__file__))
version_file = os.path.join(here, "src", "nmbrs", "__version__.py")
with open(version_file, "r", encoding="utf-8") as f:
    exec(f.read(), about)

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name=about["__title__"],
    version=about["__version__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    maintainer=about["__maintainer__"],
    maintainer_email=about["__maintainer_email__"],
    description=about["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    license=about["__license__"],
    keywords=["nmbrs", "soap"],
    python_requires=">=3.10",
    install_requires=requires,
    package_data={"": ["LICENSE", "NOTICE"]},
    package_dir={"": "src"},
    include_package_data=True,
    project_urls={
        "Homepage": "https://github.com/LarsKluijtmans/Visma-NMBRS-SOAP-API-SDK",
        "Source": "https://github.com/LarsKluijtmans/Visma-NMBRS-SOAP-API-SDK",
        "Issues": "https://github.com/LarsKluijtmans/Visma-NMBRS-SOAP-API-SDK/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
