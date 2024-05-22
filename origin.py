#!/usr/bin/python3
# Fabric script to generate a .tgz archive.
from datetime import datetime
from fabric import Connection


def do_pack():
    """
    Do_pack compreses the content folder into a tar achive.
    """

    with Connection(host='54.144.137.84', user='ubuntu') as c:
        now = datetime.now()
        txt = "web_static_" + now.strtftime('%Y%m%d%H%M%S') + '.' + '.tgz'
        archive_name = txt
        local('mkdir -p versions')
        # Create and a .tgz archive file
        crt = c.local('tar  -czvf versions/{} web_static'.format(archive_name))
        if crt is not None:
            return create
        else:
            return None
