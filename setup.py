from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="anuvaad-rev",
    version="0.1.2",
    author="Indian Language Translation Tool",
    author_email="your.email@example.com",
    description="Python package for Indian language translation using AI4Bharat's IndicTrans2 API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ai4bharat.iitm.ac.in/",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.1",
        "typing>=3.7.4",
        "urllib3>=1.26.0",
        "langdetect>=1.0.9",
    ],
    keywords="translation, indian languages, nlp, ai4bharat, indic languages, language detection, anuvaad",
)