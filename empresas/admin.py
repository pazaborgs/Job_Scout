from django.contrib import admin

from .models import Company, Jobs, Specializations, Technologies

admin.site.register(Technologies)
admin.site.register(Specializations)
admin.site.register(Company)
admin.site.register(Jobs)

