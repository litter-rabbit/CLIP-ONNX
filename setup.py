import os
import pkg_resources
from setuptools import setup, find_packages


setup(
    name="clip_onnx",
    version="1.2",
    py_modules=["clip_onnx, clip"],
    description="",
    author="Maxim Gerasimov",
    packages=find_packages(),
    include_package_data=True
)
