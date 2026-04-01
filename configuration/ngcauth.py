from os import environ

# Upstream configuration.py now reads all OIDC env vars natively
# (SOCIAL_AUTH_OIDC_OIDC_ENDPOINT, SOCIAL_AUTH_OIDC_KEY, SOCIAL_AUTH_OIDC_SECRET,
# LOGOUT_REDIRECT_URL, REMOTE_AUTH_BACKEND, REMOTE_AUTH_ENABLED).
#
# We only override:
# 1. SOCIAL_AUTH_OIDC_SCOPE — upstream parses it as space-separated string,
#    but we need 'roles' scope for authentik group sync which the env var handles.
#    This Python list takes priority over the upstream's _AS_LIST parsing.
# 2. SOCIAL_AUTH_PIPELINE — to include our custom group sync and role mapping.

SOCIAL_AUTH_OIDC_SCOPE = ["openid", "profile", "email", "roles"]

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'netbox.custom_pipeline.sync_groups',
    'netbox.custom_pipeline.set_roles',
)
