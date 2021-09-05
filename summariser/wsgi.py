

import os
import sys
from django.core.wsgi import get_wsgi_application

# path = "/summeriser/summeriser"
# if path not in sys.path:
#     sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'summeriser.settings')

application = get_wsgi_application()
