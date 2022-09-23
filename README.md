# Cookiecutter Django 

Powered by [Cookiecutter](https://github.com/cookiecutter/cookiecutter), Cookiecutter Django is a framework for jumpstarting
production-ready Django projects quickly.

- Documentation: <https://cookiecutter-django.readthedocs.io/en/latest/>
- See [Troubleshooting](https://cookiecutter-django.readthedocs.io/en/latest/troubleshooting.html) for common errors and obstacles
- If you have problems with Cookiecutter Django, please open [issues](https://github.com/saksham-ti/django-skeleton/issues/new)

## Features

- For Django
- Works with Python 3.9

## Usage

First, get Cookiecutter. Trust me, it's awesome:

    $ pip install "cookiecutter>=1.7.0"

Now run it against this repo: 

context = [Sample Context](cookiecutter.json)

```python
from cookiecutter.main import cookiecutter

cookiecutter('https://github.com/saksham-ti/django-skeleton', no_input=True, overwrite_if_exists=True,
             extra_context=context)
```

Now take a look at your repo. Don't forget to carefully look at the generated README. Awesome, right?