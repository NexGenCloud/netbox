# Remove first comment(#) on each line to implement this working logging example.
# Add LOGLEVEL environment variable to netbox if you use this example & want a different log level.
from os import environ

# Set LOGLEVEL in netbox.env or docker-compose.overide.yml to override a logging level of INFO.
LOGLEVEL = environ.get('LOGLEVEL', 'INFO')

LOGGING = {

   'version': 1,
   'disable_existing_loggers': False,
   'formatters': {
       'verbose': {
           'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
           'style': '{',
       },
       'simple': {
           'format': '{levelname} {message}',
           'style': '{',
       },
   },
   'root': {
       'handlers': ['console'],
       'level': LOGLEVEL,
   },
   'handlers': {
       'console': {
           'level': LOGLEVEL,
           'class': 'logging.StreamHandler',
           'formatter': 'simple'
       },
       'mail_admins': {
           'level': 'ERROR',
           'class': 'django.utils.log.AdminEmailHandler',
       }
   },
   'loggers': {
       'django': {
           'handlers': ['console'],
           'level': LOGLEVEL,
           'propagate': True,
       },
       'django.request': {
           'handlers': ['mail_admins'],
           'level': 'ERROR',
           'propagate': False,
       },
       'django_auth_ldap': {
           'handlers': ['console',],
           'level': LOGLEVEL,
       }
   }
}