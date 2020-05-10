"""
Library initialization module.

# TODO: Redo with pathlib and see if there is a better pattern for handling YAML.
# Create conf module here, or etc?
"""
import os

import yaml

APP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
ETC_DIR = os.path.join(APP_DIR, "etc")
VAR_DIR = os.path.join(APP_DIR, "var")


def read_text(path):
    """
    Read a file and return cleaned rows of content as a list.
    """
    # TODO see cheatsheet
    with open(path) as f_in:
        lines = f_in.read().splitlines()

    return [line.replace("\\n", "\n") for line in lines if line]


def load_conf():
    """
    Read config files and return dict of config data.
    """
    yaml_path = os.path.join(ETC_DIR, "config.local.yml")
    with open(yaml_path) as f_in:
        conf = yaml.safe_load(f_in)

    return conf
