from setuptools import setup, find_packages

setup(
    name="pyuicompose",
    version="0.1.0",
    description="Python UI Builder",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="smtdfc",
    author_email="me.smtdfc@gmail.com",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)