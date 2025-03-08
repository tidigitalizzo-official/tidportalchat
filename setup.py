from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in clefincode_chat/__init__.py
from clefincode_chat import __version__ as version

setup(
	name="Portal Chat",
	version=version,
	description="TID Portal Business Chat: A self-hosted communication solution.",
	author="TIDigitalizzo SA",
	author_email="info@tidigitalizzo.ch",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
