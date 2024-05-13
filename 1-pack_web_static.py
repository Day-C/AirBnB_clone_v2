#!/usr/bin/python3
# Fabric script to generate a .tgz archive.
import os.path
from datetime import datetime
from fabric import Connection


def do_pack(crt):
    '''Do_pack function create a new package od our crt files.'''

    if crt:
        return (crt)
    else:
        return None
