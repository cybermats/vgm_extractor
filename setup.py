from setuptools import setup, find_packages

setup(
    name="vgm_extractor", packages=find_packages(where="src"), package_dir={"": "src"}
)
