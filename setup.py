import setuptools

#with open("README.md", "r", encoding="utf-8") as fh:
#    long_description = fh.read()
long_description = 'https://py-createc.readthedocs.io/en/latest/'

with open('requirements.txt') as f:
    required = f.read().splitlines()

# Filter dependencies based on the platform
required = [req for req in required if req.strip() and not req.startswith('#')]
windows_specific = ['pywin32==228']  # Windows-specific dependency

setuptools.setup(
    name="createc",
    author="Chen Xu",
    author_email="cxu.self@gmail.com",
    description="A python interface with the Createc scanning probe microscope",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://py-createc.readthedocs.io/en/latest/",
    packages=setuptools.find_packages(exclude=['examples']),
    package_data={
        'createc': ['*.yaml'],        
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Topic :: System :: Hardware :: Hardware Drivers",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    python_requires='>=3.6, <3.8',
    install_requires=required + [req + '; platform_system=="Windows"' for req in windows_specific],
    extras_require={
        "example_maps": ["matplotlib"],
    },
)
