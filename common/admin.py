from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserCreationForm,UserChangeForm
from .models import User

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm # forms.py 에서 제작한 form을 적용
    add_form = UserCreationForm

    # 관리자페이지에 나타낼 부분 설정
    list_display = ('phone_number','email','car_number','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None,{'fields':('phone_number','email','password')}),
        ("Personal info",{'fields':('car_number',)}),
        ("Permissions",{'fields':('is_admin',)})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number','email', 'car_number', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# admin에 등록하고 Group(기본제공)은 사용하지 않도록 설정
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)