# act_project/act/metadata/admin.py
from django import forms
from django.contrib import admin

from act.services.transmeta import canonical_fieldname

from act.admin import (
    admin_site, DefaultOrderingModelAdmin,
    ForbidAddMixin, ForbidDeleteMixin,
)

from .models import Metadata


@admin.register(Metadata, site=admin_site)
class MetadataAdmin(
    ForbidAddMixin, ForbidDeleteMixin, DefaultOrderingModelAdmin
):
    readonly_fields = ('url_name', 'image_preview', )
    list_display = ('title_uk', )
    fieldsets = (
        (None, {
            'fields': ('image_preview', 'image', 'url_name', 'robots', )
        }),
        ('Локалізована інформація', {
            'fields': ('title_uk', 'description_uk',)
        }),
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(MetadataAdmin, self).formfield_for_dbfield(
            db_field, **kwargs
        )
        db_fieldname = canonical_fieldname(db_field)

        if db_fieldname == 'description':
            field.widget = forms.Textarea(attrs={'cols': '80', 'rows': '4'})

        return field
