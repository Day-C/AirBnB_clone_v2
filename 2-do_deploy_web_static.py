#!/usr/bin/python3
"""
Script distributes an archive file to a web server
based on the file 1-pack_web_static.py.
"""


from fabric import Connection
from datetime import datetime
from fabric.api import *


def do_deploy(archive_path):
    '''do_deploy distributes an archive fo a server
    Args:
        archive_path: path to the archive file.
    '''

    if not archive_path:
        return False
    else:
        #Set up a connection to the server
        for ip in ('54.144.137.84', 3.83.227.159):
            with Connection(
                    host=ip,
                    user='ubuntu'
                    ) as c:
                #upload archiev to directory on server
                c.put('archive_path', remote='/tmp/')
                #Uncompress archive to folder on server
                c.run('tar xf /tmp/{} --directory=/data/web_static/releases/'.format(archive_path))

                #Delete the archive from web server
                c.run('sudo rm /tmp/{}'.format(archive_path)))
                #Delete the symbolic link on server
                c.run('sudo rm /data/web_static/current')
                #Create new symbolic link to the decompressed file
                c.run('sudo ln -s /data/web_static/releases/{} /data/web_static/current'.format(archive_path))
    return True

