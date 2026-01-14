#!/usr/bin/env python
import os
import glob
import requests

from setuptools import setup, find_packages

def get_lastest():
    response = requests.get(
        url="https://api.github.com/repos/bogdanfinn/tls-client/releases/latest"
    )
    data = response.json()

    return data["tag_name"].lstrip("v")

shared_library_version = get_lastest()

print(f"Downloading tls-client shared libraries version: {shared_library_version}")

github_download_url = f"https://github.com/bogdanfinn/tls-client/releases/download/v{shared_library_version}/{{}}"
github_repo_filenames = [
    
    # Windows
    f"tls-client-windows-32-{shared_library_version}.dll",
    f"tls-client-windows-64-{shared_library_version}.dll",
    
    # MacOS
    f"tls-client-darwin-arm64-{shared_library_version}.dylib",
    f"tls-client-darwin-amd64-{shared_library_version}.dylib",
    
    # Linux
    f"tls-client-linux-alpine-amd64-{shared_library_version}.so",
    f"tls-client-linux-ubuntu-amd64-{shared_library_version}.so",
    f"tls-client-linux-arm64-{shared_library_version}.so"
]

dependency_filenames = [
    
    # Windows
    "tls-client-32.dll",
    "tls-client-64.dll",

    # MacOS
    "tls-client-arm64.dylib",
    "tls-client-x86.dylib",
    
    # Linux
    "tls-client-amd64.so",
    "tls-client-x86.so",
    "tls-client-arm64.so"
]

for github_filename, dependency_filename in zip(github_repo_filenames, dependency_filenames):
    response = requests.get(
        url=github_download_url.format(github_filename)
    )

    with open(f"tls_client/dependencies/{dependency_filename}", "wb") as f:
        f.write(response.content)


data_files = []
directories = glob.glob('tls_client/dependencies/')

for directory in directories:
    files = glob.glob(directory+'*')
    data_files.append(('tls_client/dependencies', files))

about = {}
here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "tls_client", "__version__.py"), "r", encoding="utf-8") as f:
    exec(f.read(), about)

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()


setup(
    data_files=data_files,
    name=about["__title__"],
    version=about["__version__"],
    author=about["__author__"],
    description=about["__description__"],
    license = "MIT",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['*'],
    },
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
    ],
    project_urls={
        "Source": "https://github.com/defnotsamuel/tls-client",
    }
)