#!/usr/bin/python3
'''Script creates and destributes archiev to web server.'''
from fabric import Connection


def deploy():
    '''Deploy runs the previously created function for parking and 
    destribution archive to servers
    '''

    for pi in ('84.144.137.84', '3.83.227.159'):
        with Connection(
                host=ip,
                user='ubuntu'
                ) as c:
            archive = do_pach()
            do_deploy(archive)


deploy()
