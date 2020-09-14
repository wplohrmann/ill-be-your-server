from setuptools import setup, find_packages

setup(
    name="ill-be-your-server",
    version="0.0.1",
    author="William Lohrmann",
    author_email="willia2501@gmail.com",
    description="",
    packages=find_packages(),
    install_requires=[
        "requests",
        "peewee",
        "beautifulsoup4",
        "lxml"],
    python_requires='>=3.6',
)
