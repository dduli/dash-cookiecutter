# {{cookiecutter.project_name}}

## Install

```bash
cd {{cookiecutter.project_name}}/
python3 -m venv venv
source venv/bin/activate
pip install -U pip wheel setuptools
pip install -e .

```

## Local run

```bash
cd {{cookiecutter.project_name}}/
source venv/bin/activate
python {{cookiecutter.project_slug}}/main.py

```

Visit [http://localhost:8030/pages/{{cookiecutter.sample_page}}](http://localhost:8030/pages/{{cookiecutter.sample_page}})


## Development