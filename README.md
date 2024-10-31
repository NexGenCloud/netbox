# Nexgen Cloud Netbox Docker

Based on [netbox-community/netbox-docker](https://github.com/netbox-community/netbox-docker), with modifications for use by NexGen Cloud.

## Building

```shell
docker build -t netbox:<version> .
```

## Testing

Create an environment file for each service in `./env`:
- `netbox.env`
- `postgres.env`
- `redis-cache.env`
- `redis.env`

Samples exist in the `./env` directory, suffixed with `.sample`.

Then bring up with Docker compose: `docker compose -f docker-compose.dev.yml up [-d]`