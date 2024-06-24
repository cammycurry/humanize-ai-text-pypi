from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="humanize-ai-text",
    version="1.0.0",
    author="Cam Curry",
    author_email="cam@humanize-ai-text.ai",
    description="SDK for Humanized AI Text API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/humanize-ai-text",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
