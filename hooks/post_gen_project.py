import os
import shutil



def append_to_gitignore_file(ignored_line):
    with open(".gitignore", "a") as gitignore_file:
        gitignore_file.write(ignored_line)
        gitignore_file.write("\n")


REMOVE_PATHS = [
    {% if not cookiecutter.authentication.enabled == 'True' %}
        'tests/test_auth.py',
    {% endif %}
    {% if not cookiecutter.documentation.enabled == 'True' %}
        'docs',
    {% endif %}
    {% if not cookiecutter.configuration.env_variables.dotenv.enabled == 'True' %}
        '.env',
    {% endif %}
    {% if cookiecutter.configuration.logger.enabled %}
    '{{cookiecutter.project.slug}}/settings/logger.py',
    {% endif %}
    {% if not cookiecutter.worker.celery.enabled == 'True' %}
        '{{cookiecutter.project.slug}}/celery.py',
    {% endif %}
    {% if not cookiecutter.deployment.cdk.enabled == 'True' %} 
        'cdk-deployment',
    {% endif %}

    {%- if not cookiecutter.tests.enabled == 'True' %}
        'conftest.py',
        'tests',
    {%- endif %}
]

def main():
    append_to_gitignore_file(".env")
    append_to_gitignore_file(".envs/*")
    for path in REMOVE_PATHS:
        path = path.strip()
        if path and os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.unlink(path)




if __name__ == "__main__":
    main()