#!/usr/bin/python3


from fabric import Connection

with Connection(
        host='54.144.137.84',
        user='ubuntu') as c:
    archive_name = "somefile.tgz"
    c.local('mkdir -p versions')
    c.run('sudo mkdir -p versions')
    c.local('tar  -czvf versions/{} web_static'.format(archive_name))

    print(c.run('cat /etc/nginx/sites-available/default'))
