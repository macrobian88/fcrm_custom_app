from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

setup(
    name="fcrm_custom_app",
    version="0.0.1",
    description="Custom Frappe CRM App with Campaign Management",
    author="FCRM Developer",
    author_email="developer@example.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
