import os
from django.core.wsgi import get_wsgi_application

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

# Get WSGI application
app = get_wsgi_application()

# Required by Vercel
handler = app
