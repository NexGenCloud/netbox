#!/bin/sh

/opt/netbox/venv/bin/python manage.py migrate
/opt/netbox/venv/bin/python manage.py collectstatic --no-input
/opt/netbox/docker-entrypoint.sh /opt/netbox/launch-netbox.sh