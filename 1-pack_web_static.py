#!/usr/bin/python3
'''Fabric script to generate a .tgz archive'''
from datetime import datetime
from fabric import Connection


def do_pack():
    '''Do_pack compreses the content of the web static  folder into a tar achive'''


    now = datetime.now()
    with Connection(host='54.144.137.84', user='ubuntu') as c:
        archive_name = "web_static_" + now.strtftime('%Y%m%d%H%M%S') + '.' + '.tgz'
        local('mkdir -p versions')
        # Create and a .tgz archive file
        create = c.local('tar  -czvf versions/{} web_static'.format(archive_name))
        if create is not None:
            return create
        else:
            return None
