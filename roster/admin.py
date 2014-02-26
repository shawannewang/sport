from django.contrib import admin
from roster.models import Member
from roster.models import Mentor

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
	search_fields = ('name',)

admin.site.register(Member, MemberAdmin)

class MentorAdmin(admin.ModelAdmin):
	search_fields = ('name',)

admin.site.register(Mentor, MentorAdmin)
