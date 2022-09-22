import os
import shutil

files_to_remove = set()
dirs_to_remove = set()

{%- if cookiecutter.tests is not defined %}
files_to_remove = files_to_remove.union(('conftest'))
dirs_to_remove = dirs_to_remove.union(('tests', ))
{%- endif %}

def append_to_gitignore_file(ignored_line):
    with open(".gitignore", "a") as gitignore_file:
        gitignore_file.write(ignored_line)
        gitignore_file.write("\n")

def remove_files(file_names):
    for file_name in file_names:
        os.remove(file_name)

def remove_dirs(dirs):
    for dir in dirs:
        if os.path.exists(dir):
            shutil.rmtree(dir)


REMOVE_PATHS = [
    '{% if cookiecutter.deployment.cdk is not defined %} CDK {% endif %}',
]

def main():
    append_to_gitignore_file(".env")
    append_to_gitignore_file(".envs/*")
    remove_files(files_to_remove)
    remove_dirs(dirs_to_remove)
    for path in REMOVE_PATHS:
        path = path.strip()
        if path and os.path.exists(path):
            if os.path.isdir(path):
                os.rmdir(path)
            else:
                os.unlink(path)




if __name__ == "__main__":
    main()