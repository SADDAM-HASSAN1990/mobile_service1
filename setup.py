from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mobile_services/__init__.py
from mobile_services import __version__ as version

setup(
	name="mobile_services",
	version=version,
	description="Mobile Services Project",
	author="saddam hassan",
	author_email="saddam.hassan222@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
