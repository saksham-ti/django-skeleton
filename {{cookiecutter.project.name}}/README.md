# {{ cookiecutter.project.name }}

[![Devspaces](https://img.shields.io/badge/devspaces-enabled-blue)](http://start.devspaces.com/)
[![API Documentation](https://img.shields.io/badge/apidoc-swagger-brightgreen)](https://trilogy-group.github.io/{{cookiecutter.repo_name}}/docs/)


## Setting up development environment

### DevSpaces
DevSpaces is the recommended development environment for this repo. To get started, just open this repo with [DevSpaces](https://trilogy.devspaces.com/). 

It will start a dev server by default (on port 8000). If it doesn't you can start it by executing the following command in a terminal

```
source scripts/devspace/setup_project_gitpod.sh
```


### Local Setup

Follow these steps to setup a local development environment

```bash
git clone https://github.com/trilogy-group/{{cookiecutter.repo_name}}.git
python3 -m venv ./venv

# You need GH token to install npm package from GH
eval $(gp env -e GITHUB_TOKEN=<YOUR_GH_TOKEN>) # this is for devspace, you can also configure it here https://trilogy.devspaces.com/variables
export GITHUB_TOKEN=<YOUR_GH_TOKEN> # for local env

# On Linux/Mac
source ./venv/bin/activate
# On windows, you run:
# source ./venv/Scripts/activate

# Run the following command first time on local setup (it runs automatically on devspace startup)
source scripts/setup_project.sh

# setup_project.sh will start the server, for subsequent server restart
python ./integration_hub_v2/manage.py runserver_plus 4000
```