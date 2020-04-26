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
    install_requires=['Flask>=1.1.2',
                      'Flask-SQLAlchemy>=2.4.1',
                      'requests>=2.23.0',
                      'SQLAlchemy>=1.3.16',
                      'gevent>=20.4.0'],
)
