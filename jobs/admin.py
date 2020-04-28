from django.contrib import admin

# Register your models here.
from jobs.models import JobApply, AddJob,Orders

# Register your models here.
admin.site.register(JobApply)
admin.site.register(AddJob)
admin.site.register(Orders)