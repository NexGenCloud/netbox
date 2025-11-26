import sys
import os

FIELD_CHOICES = {
    'dcim.Device.status+': (
        ('rma', 'RMA', 'orange'),
    ),
    'dcim.Module.status+': (
        ('rma', 'RMA', 'orange'),
    )
}

# NetBox Branching Configuration
# Add config directory to path to import configuration.py
sys.path.append('/etc/netbox/config')

try:
    # Import the configuration module provided by netbox-docker
    import configuration
    from netbox_branching.utilities import DynamicSchemaDict
    
    if hasattr(configuration, 'DATABASES'):
        # Wrap the existing DATABASES config
        DATABASES = DynamicSchemaDict(configuration.DATABASES)
        
        DATABASE_ROUTERS = [
            'netbox_branching.database.BranchAwareRouter',
        ]
    else:
        print("⚠️ extra.py: configuration module imported but has no DATABASES attribute")

except ImportError:
    pass
except Exception as e:
    print(f"❌ extra.py: Error configuring netbox_branching: {e}")
