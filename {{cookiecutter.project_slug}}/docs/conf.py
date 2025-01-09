import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

project = "{{cookiecutter.project_name}}"
author = "{{cookiecutter.full_name}}"
release = "0.1.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "alabaster"
