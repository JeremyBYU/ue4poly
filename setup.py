import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ue4poly",
    version="0.0.1",
    author="Jeremy Castagno",
    author_email="jdcata@umich.edu",
    description="UE4 Polygon Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/microsoft/airsim",
    packages=setuptools.find_packages(),
	license='MIT',
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
          'msgpack-rpc-python', 'numpy'
    ]
)