from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

# Register your models here.
admin.site.register(Member, MemberAdmin)
