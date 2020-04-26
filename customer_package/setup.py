from setuptools import setup, find_packages

setup(
    name='hicity',
    version='0.8',
    author="i.Pear",
    author_email="i.pear@outlook.com",
    project_urls={
        "Code": "https://github.com/i-Pear/HiCity",
    },
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'prompt-toolkit>=3.0.5',
        'requests>=2.23.0',
        'SQLAlchemy>=1.3.16',
        'urllib3>=1.25.9',
        'xlwt>=1.3.0',
    ],
)
