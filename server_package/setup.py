from setuptools import setup, find_packages

setup(
    name='hicityserver',
    version='0.8',
    author="i.Pear",
    author_email="i.pear@outlook.com",
    project_urls={
        "Code": "https://github.com/i-Pear/HiCity",
    },
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
)
