from django.contrib import admin

from .models import Sanction
from .models import PEP
from .models import Transaction

admin.site.register(Sanction)
admin.site.register(PEP)
admin.site.register(Transaction)