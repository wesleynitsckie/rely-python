from django.contrib import admin

from .models import Sanction
from .models import PEP

admin.site.register(Sanction)
admin.site.register(PEP)
