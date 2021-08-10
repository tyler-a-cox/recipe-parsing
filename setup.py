import os
import glob

from setuptools import find_packages, setup

about = {}
here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(os.path.dirname(__file__), "README.md")).read()
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join("..", path, filename))
    return paths


extra_files = package_files("recipe_parser/ingredient_parser/models/ner")

setup(
    name="recipe_parser",
    url="https://github.com/tyler-a-cox/recipe_parser/",
    version="0.0.1",
    author="Tyler Cox",
    author_email="tyler.a.cox@berkeley.edu",
    description="Python package, scraping recipes from all over the internet",
    keywords="python recipes scraper harvest recipe-scraper recipe-scrapers",
    long_description=README,
    long_description_content_type="text/x-rst",
    install_requires=["beautifulsoup4", "extruct", "requests", "spacy"],
    packages=["recipe_parser"],
    include_package_data=True,
    package_data={"": extra_files},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
    ],
    python_requires=">=3.6",
)
