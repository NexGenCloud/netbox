### Branching plugin settings

from netbox_branching.utilities import DynamicSchemaDict
from .configuration import DATABASE
from os import environ


# Wrap DATABASES with DynamicSchemaDict for dynamic schema support
DATABASES = DynamicSchemaDict({
    'default': DATABASE,
})

# Employ our custom database router
DATABASE_ROUTERS = [
    'netbox_branching.database.BranchAwareRouter',
]

###

CACHE_TIMEOUT = environ.get('CACHE_TIMEOUT', 0)