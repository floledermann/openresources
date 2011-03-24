
from django.conf import settings

TAG_HELP_LINKS = getattr(settings, 'OPENRESOURCES_TAG_HELP_LINKS', None)

MAP_ATTRIBUTION = getattr(settings, 'OPENRESOURCES_MAP_ATTRIBUTION', 'Resource Data collected with <a href="http://bitbucket.org/floledermann/openresources/">OpenResources</a>')

