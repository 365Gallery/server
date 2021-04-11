from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from members.models import Member


@admin.register(Member)
class MemberAdmin(UserAdmin):
    pass
