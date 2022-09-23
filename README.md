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

Sample Context:

```JSON
context = {
  "repo_name": "MyProject",
  "organization_name": "Trilogy",
  "project": {
      "name": "MyProject",
      "slug": "myproject",
      "description": "Sample Project Description",
      "contact_email": "saksham@trilogy.com",
      "owner": "Saksham Mittal",
      "aws": {
        "aws_access_key_id": "",
        "aws_secret_access_key": "",
        "region_name": "",
        "bucket_name": ""
      }
  },
  "authentication": {
      "rest": True,
      "aws_cognito": {
          "key": ""
      },
      "social": {
          "google": {
            "oauth2_key": "",
            "oauth2_secret": "",
            "oauth_absolute_redirect_uri": ""
          },
          "github": {
            "oauth2_key": "",
            "oauth2_secret": "",
            "oauth_absolute_redirect_uri": ""
          },
          "aws_cognito": {
            "cognito_key": "",
            "cognito_secret": "",
            "cognito_pool_domain": ""
          }
      }
  },
  "database": {
    "dynamodb": {
      "endpoint_url": "http://localhost:8080",
      "region_name": "us-east-1",
      "aws_access_key_id": "",
      "aws_secret_access_key": ""
    },
    "sql": {
      "engine": "django.db.backends.sqlite3",
      "host": "postgres",
      "port": "5432",
      "name": "myproject",
      "user": "user",
      "password": "password"
    }
  },
  "documentation": {
    "swagger": True,
    "readme": True,
    "demo_curl_requests": True,
    "sample_crud": True

  },
  "environment": {
    "linter": "pylint",
    "local_debugger": True,
    "env_variables": True,
    "dockerfile": True,
    "gitpod": True
  },

  "prometheus": True,
  "worker": {
    "celery": {
      "sample_tasks": True,
      "timezone": "Asia/Kolkata",
      "workers": 1,
      "broker": "redis"
    },
    "django_q": {

    }
  },
  "tests": {
    "sample_tests": True,
    "pytest": {

    }
  },
  "email": {
    "sendgrid": {
      "email_url": "",
      "username": "",
      "password": ""
    },
    "default": {
      "email_backend": "django.core.mail.backends.console.EmailBackend",
      "host": "",
      "port": "",
      "host_user": "",
      "host_password": "",
      "use_tls": True,
      "use_ssl": True,
      "default_from_email": "info@trilogy.com"
    }
  },
  "storage": {
    "cloudinary": {
      "cloud_name": "",
      "api_key": "",
      "api_secret": ""
    },
    "s3": {
      "aws_access_key_id": "",
      "aws_secret_access_key": "",
      "aws_bucket_name": "",
      "aws_custom_domain": ""
    }
  },
  "use_whitenoise": True,
}
```

Now run it against this repo: 

```python
from cookiecutter.main import cookiecutter

cookiecutter('https://github.com/saksham-ti/django-skeleton', no_input=True, overwrite_if_exists=True,
             extra_context=context)
```

Now take a look at your repo. Don't forget to carefully look at the generated README. Awesome, right?