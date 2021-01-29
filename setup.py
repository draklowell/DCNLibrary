import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dcn",
    version="1.0.0",
    author="Drak Lowell",
    description="Decentralized computer network",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/draklowell/DCNLibrary",
    packages=["dcn"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    ],
    install_requires = [
        'pycryptodome>=3.9.9',
        'ansicolors>=1.1.8'
    ],
    python_requires='>=3.8',
)