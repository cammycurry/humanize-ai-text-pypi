from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="humanize-ai-text",
    version="1.0.1",
    author="Cam Curry",
    author_email="cam@humanize-ai-text.ai",
    description="SDK for Humanized AI Text API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cammycurry/humanize-ai-text-pypi",
    project_urls={
        "Homepage": "https://humanize-ai-text.ai",
        "Source": "https://github.com/cammycurry/humanize-ai-text-pypi",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
