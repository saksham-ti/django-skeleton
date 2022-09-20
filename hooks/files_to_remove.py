files_to_remove = set()
dirs_to_remove = set()

{%- if cookiecutter.tests is not defined %}
files_to_remove = files_to_remove.union(('conftest'))
dirs_to_remove = dirs_to_remove.union(('tests', ))
{%- endif %}