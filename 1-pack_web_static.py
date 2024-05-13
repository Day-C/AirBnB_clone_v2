#!/usr/bin/python3
# Fabric script to generate a .tgz archive.
import os.path
from datetime import datetime
from fabric import Connection


def do_pack(crt):
    """
    Do_pack compreses the content folder into a tar achive.
    """
    if crt:
        return create
    else:
        return None
