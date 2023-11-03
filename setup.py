from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ampower_farmaans/__init__.py
from ampower_farmaans import __version__ as version

setup(
	name="ampower_farmaans",
	version=version,
	description="by using custom .docx template create docx file or pdf for documents",
	author="Ambibuzz Technologies LLP",
	author_email="buzz.us@ambibuzz.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
