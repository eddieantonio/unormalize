import codecs

from setuptools import find_packages, setup  # type: ignore

import unormalize


def long_description():
    with codecs.open("README.rst", encoding="utf8") as f:
        return f.read()


setup(
    name="unormalize",
    version=unormalize.__version__,
    description="Unicode normalization filters",
    long_description=long_description(),
    long_description_content_type="text/x-rst",
    url="https://github.com/eddieantonio/unormalize",
    download_url="https://github.com/eddieantonio/unormalize",
    author=unormalize.__author__,
    author_email="easantos@ualberta.ca",
    license=unormalize.__license__,
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "unormalize = unormalize.__init__:main",
            "nfc = unormalize.__init__:nfc",
            "nfd = unormalize.__init__:nfd",
            "nfkc = unormalize.__init__:nfkc",
            "nfkd = unormalize.__init__:nfkd",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Topic :: Text Processing",
        "Topic :: Utilities",
    ],
)
