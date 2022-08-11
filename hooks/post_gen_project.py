import subprocess

if __name__ == "__main__":
    if "{{cookiecutter.create_subdir}}" == "y":
        subprocess.call(['mkdir', 'app/services/{{cookiecutter.module_name}}'])
        subprocess.call(['mv', 'app/services/{{cookiecutter.service_name}}.rb', 'app/services/{{cookiecutter.module_name}}'])
