from django.contrib import admin
from .models import Fcuser

# Register your models here.
# 관리자 정보

class FcuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
    pass

admin.site.register(Fcuser, FcuserAdmin)