from netbox.authentication import Group


def sync_groups(response, user, backend, *args, **kwargs):
    """Sync user's NetBox groups to match the OIDC provider response."""
    groups = response.get('groups')
    if groups is None:
        user.groups.clear()
        return

    # Ensure all OIDC groups exist in NetBox
    for group_name in groups:
        Group.objects.get_or_create(name=group_name)

    # Atomically set user's groups to exactly match the OIDC response
    user.groups.set(Group.objects.filter(name__in=groups))


def set_roles(response, user, backend, *args, **kwargs):
    """Set superuser flag based on OIDC group membership."""
    groups = response.get('groups', [])
    user.is_superuser = 'superusers' in groups
    user.save()
