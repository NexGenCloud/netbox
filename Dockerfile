FROM netboxcommunity/netbox:v3.7.8

ENV LANG=C.utf8 \
    PATH=/opt/netbox/venv/bin:$PATH \
    TOPOLOGY_STATIC=/opt/netbox/netbox/static/netbox_topology_views

COPY configuration/configuration.py /etc/netbox/config/configuration.py
COPY configuration/plugins.py /etc/netbox/config/plugins.py
COPY configuration/extra.py /etc/netbox/config/extra.py
COPY configuration/ngcauth.py /etc/netbox/config/ngcauth.py
COPY authentication/custom_pipeline.py /opt/netbox/netbox/netbox/custom_pipeline.py
COPY authentication/authentication.py /opt/netbox/netbox/netbox/authentication.py
COPY requirements.txt /tmp/requirements.txt

RUN /opt/netbox/venv/bin/python -m pip install --upgrade -r /tmp/requirements.txt && \
    mkdir -p $TOPOLOGY_STATIC/img && chown unit:root -R $TOPOLOGY_STATIC && \
    rm -rf /tmp/requirements.txt

ENTRYPOINT [ "/usr/bin/tini", "--" ]

CMD [ "/opt/netbox/docker-entrypoint.sh", "/opt/netbox/launch-netbox.sh" ]