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
{
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
        "enabled": true,
        "rest": {
            "enabled": true
        },
        "social": {
            "enabled": true,
            "google": {
                "enabled": true,
                "oauth2_key": "",
                "oauth2_secret": "",
                "oauth_absolute_redirect_uri": ""
            },
            "github": {
                "enabled": true,
              "oauth2_key": "",
              "oauth2_secret": "",
              "oauth_absolute_redirect_uri": ""
            },
            "aws_cognito": {
                "enabled": true,
              "key": "",
              "secret": "",
              "cognito_pool_domain": ""
            }
        }
    },
    "database": {
        "enabled": true,
      "dynamodb": {
        "enabled": false,
        "endpoint_url": "http://localhost:8080",
        "region_name": "us-east-1",
        "aws_access_key_id": "",
        "aws_secret_access_key": ""
      },
      "sql": {
        "enabled": true,
        "engine": "django.db.backends.sqlite3",
        "host": "postgres",
        "port": "5432",
        "name": "myproject",
        "user": "user",
        "password": "password"
      }
    },
    "documentation": {
      "swagger": true,
      "readme": true,
      "demo_curl_requests": true,
      "sample_crud": true
  
    },
    "environment": {
      "linter": "pylint",
      "local_debugger": true,
      "env_variables": true,
      "dockerfile": true, 
      "gitpod": true
    },
    "tracing": {
        "prometheus": {
            "enabled": true
        }
    },
    
    "worker": {
      "celery": {
        "enabled": false,
        "sample_tasks": true,
        "timezone": "Asia/Kolkata",
        "workers": 1,
        "broker": "redis"
      },
      "django_q": {
        "enabled": false
      }
    },
    "tests": {
        "enabled": true,
      "sample_tests": true,
      "pytest": {
  
      }
    },
    "email": {
        "enabled": true,
      "sendgrid": {
        "enabled": false,
        "email_url": "",
        "username": "",
        "password": ""
      },
      "default": {
        "enabled": false,
        "email_backend": "django.core.mail.backends.console.EmailBackend",
        "host": "",
        "port": "",
        "host_user": "",
        "host_password": "",
        "use_tls": true,
        "use_ssl": true,
        "default_from_email": "info@trilogy.com"
      }
    },
    "storage": {
        "enabled": false,
      "cloudinary": {
        "enabled": false,
        "cloud_name": "",
        "api_key": "",
        "api_secret": ""
      },
      "s3": {
        "enabled": false,
        "aws_access_key_id": "",
        "aws_secret_access_key": "",
        "aws_bucket_name": "",
        "aws_custom_domain": ""
      }
    },
    "use_whitenoise": true,
    "deployment": {
        "enabled": true,
      "cdk": {
        "enabled": true,
        "default_region": "",
        "default_account": "",
        "vpc_name": "",
        "vpc_id": "vpc-....",
        "security_group_name": "",
        "cluster_name": "",
        "loadbalancer": {
          "cpu": 256,
          "desired_count": 2,
          "memory_limit_mib": 512,
          "max_healthy_percent": 200,
          "min_healthy_percent": 50,
          "certificate_arn": "arn:aws:acm:region_name:account:certificate/....",
          "auto_scale_task_count": {
            "min_capacity": 1,
            "max_capacity": 5
          },
          "target_cpu_utilization_percent": 40,
          "target_memory_utilization_percent": 40,
          "health_check": {
            "healthy_threshold_count": 2,
            "interval_secs": 20,
            "timeout_secs": 10
          }
        },
        "domain_record": {
          "record_name": "",
          "domain_name": "devfactory.com",
          "ttl_minutes": 1
        }
      },
      "eyk": {
        "enabled": false
      }
    }
  }
```

Now run it against this repo: 

```python
from cookiecutter.main import cookiecutter

cookiecutter('https://github.com/saksham-ti/django-skeleton', no_input=True, overwrite_if_exists=True,
             extra_context=context)
```

Now take a look at your repo. Don't forget to carefully look at the generated README. Awesome, right?