"""Setup script for Sendflare SDK Python"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sendflare-sdk-python",
    version="1.0.0",
    author="Sendflare Team",
    author_email="",
    description="The SDK for sendflare service written in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://docs.sendflare.io",
    project_urls={
        "Bug Tracker": "https://github.com/sendflare/sendflare-sdk-python/issues",
        "Documentation": "https://docs.sendflare.io",
        "Source Code": "https://github.com/sendflare/sendflare-sdk-python",
    },
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=[
        # No external dependencies - uses standard library only
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ],
    },
    keywords="sendflare email sdk api client",
    license="MIT",
)

