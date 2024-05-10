from django.contrib import admin
from testapps.models import HydJobs,PuneJobs,BangJobs

# Register your models here.
class HybJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(HydJobs,HybJobsAdmin)
class PuneJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']
admin.site.register(PuneJobs, PuneJobsAdmin)
class BangJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']
admin.site.register(BangJobs, BangJobsAdmin)


