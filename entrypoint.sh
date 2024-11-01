#!/bin/sh

/opt/netbox/venv/bin/python manage.py migrate netbox_topology_views
/opt/netbox/venv/bin/python manage.py collectstatic --no-input
/opt/netbox/docker-entrypoint.sh /opt/netbox/launch-netbox.sh