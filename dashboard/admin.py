from django.contrib import admin
from models import *
# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'dob', 'gender']
    pass

class BloodWorkAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'date']
    pass

class BloodWorkTypeAdmin(admin.ModelAdmin):
    pass


class MedicationAdmin(admin.ModelAdmin):
    pass

class VisitAdmin(admin.ModelAdmin):
    list_display = [ 'visit_time', 'type_of_visit']
    pass

admin.site.register(AccountInfo, AccountAdmin)
admin.site.register(BloodWork, BloodWorkAdmin)
admin.site.register(BloodWorkType, BloodWorkTypeAdmin)
admin.site.register(Medication, MedicationAdmin)
admin.site.register(Visit, VisitAdmin)

