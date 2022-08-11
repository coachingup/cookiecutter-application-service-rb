import os

if __name__ == "__main__":
    if "{{cookiecutter.create_subdir}}" == "y":
        os.mkdir('app/services/{{cookiecutter.module_name}}')
        os.rename('app/services/{{cookiecutter.service_name}}.rb', 'app/services/{{cookiecutter.module_name}}/{{cookiecutter.service_name}}.rb')
