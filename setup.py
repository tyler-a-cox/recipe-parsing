import os

from setuptools import find_packages, setup

about = {}
here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(os.path.dirname(__file__), "README.md")).read()
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

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
    install_requires=["beautifulsoup4>=4.6.0", "extruct>=0.8.0", "requests>=2.19.1"],
    packages=find_packages(),
    package_data={"": ["LICENSE"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
    ],
    python_requires=">=3.6",
)
