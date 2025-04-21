from setuptools import setup, find_packages

setup(
    name="python-escpos-jp",
    version="0.1",
    author="chansei",
    author_email="contact@chansei.net",
    url="https://github.com/chansei/python-escpos-jp",
    download_url="http://github.com/chansei/python-escpos-jp/archive/master.zip",
    install_requires=["python-escpos",],
    package_dir={"": "src"},
    packages=find_packages(where="src")
)
