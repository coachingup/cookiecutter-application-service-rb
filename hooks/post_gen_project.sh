#!/bin/sh
if [ {{cookiecutter.create_subdir}} = "y" ]; then
  mkdir app/services/{{cookiecutter.module_name}}
  mv app/services/{{cookiecutter.service_name}}.rb app/services/{{cookiecutter.module_name}}
fi
