import os, sys

sys.path.insert(0, '/var/www/u3120090/data/www/goose-cycle.ru/django-gcw')
sys.path.insert(1, '/var/www/u3120090/data/venv/lib/python3.10/site-packages')

os.environ['DJANGO_SETTING_MODULE'] = 'GCW.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
