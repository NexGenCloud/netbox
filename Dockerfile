FROM ghcr.io/netbox-community/netbox:v4.1.6

ENV LANG=C.utf8 \
    PATH=/opt/netbox/venv/bin:$PATH \
    TOPOLOGY_STATIC=/opt/netbox/netbox/static/netbox_topology_views

COPY configuration/plugins.py /etc/netbox/config/plugins.py
COPY configuration/extra.py /etc/netbox/config/extra.py
COPY configuration/ngcauth.py /etc/netbox/config/ngcauth.py
COPY authentication/custom_pipeline.py /opt/netbox/netbox/netbox/custom_pipeline.py
COPY requirements.txt /tmp/requirements.txt
COPY entrypoint.sh /opt/netbox/entrypoint.sh

RUN /opt/netbox/venv/bin/python -m pip install --upgrade -r /tmp/requirements.txt && \
    mkdir -p $TOPOLOGY_STATIC/img && chown unit:root -R $TOPOLOGY_STATIC && \
    chown unit:root /opt/netbox/entrypoint.sh; chmod +x /opt/netbox/entrypoint.sh && \
    sed -i 's/OpenID Connect/NexGen Cloud Login/g' /opt/netbox/netbox/netbox/authentication/__init__.py && \
    rm -rf /tmp/requirements.txt

ENTRYPOINT [ "/usr/bin/tini", "--" ]

CMD [ "/opt/netbox/entrypoint.sh" ]