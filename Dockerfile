FROM ghcr.io/netbox-community/netbox:v4.5.10

COPY configuration/plugins.py /etc/netbox/config/plugins.py
COPY configuration/extra.py /etc/netbox/config/extra.py
COPY configuration/ngcauth.py /etc/netbox/config/ngcauth.py
COPY configuration/logging.py /etc/netbox/config/logging.py
COPY configuration/local_settings.py /opt/netbox/netbox/netbox/local_settings.py
COPY authentication/custom_pipeline.py /opt/netbox/netbox/netbox/custom_pipeline.py
COPY requirements.txt /tmp/requirements.txt

RUN /usr/local/bin/uv pip install -r /tmp/requirements.txt && \
    SECRET_KEY="build-only-dummy-key-not-used-at-runtime-minimum-50-chars" \
      python manage.py collectstatic --no-input && \
    sed -i 's/OpenID Connect/NexGen Cloud Login/g' \
      /opt/netbox/netbox/netbox/authentication/__init__.py && \
    rm -f /tmp/requirements.txt

CMD [ "/opt/netbox/docker-entrypoint.sh", "/opt/netbox/launch-netbox.sh" ]
