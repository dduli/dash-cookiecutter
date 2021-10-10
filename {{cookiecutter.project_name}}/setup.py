#!/usr/bin/env python
from setuptools import find_packages, setup


project = "{{cookiecutter.project_name}}"
version = "0.1.0"


setup(
    name=project,
    version=version,
    author="",
    description="",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    python_requires='>=3',
    install_requires=[
        "requests>=2.22.0",
        "click>=7.0",
        "dash-bootstrap-components>=0.3.0",
        "dash-dangerously-set-inner-html",
        "flask",
        "flask-sqlalchemy",
        # "flask-marshmallow",
        # "flask-login",
        "bootstrap-flask",
        # "flask-migrate",
        # "marshmallow-sqlalchemy",
        # "sqlalchemy",
        "flask-session",
        # "numpy",
        # "pandas",
        # "html2text",
    ],
    extras_require={
        "dev": [
            "pytest",
            "mock",
            "flake8",
            "pytest-cov",
            "unittest-xml-reporting",
            "coverage",
            "bump2version",
            "parameterized",
            "wheel",
            "click==7.1.2",
            # "alembic",
        ]
    },
    test_suite="tests",
    keywords="python, flask, microservices, plotly, dash",
    include_package_data=True,
    entry_points={
    },
)
