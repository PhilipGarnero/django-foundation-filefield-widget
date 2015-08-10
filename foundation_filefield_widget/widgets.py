# -*- coding: utf-8 -*-

from django import forms
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.conf import settings


class FoundationFileInput(forms.ClearableFileInput):

    class Media:
        css = {'all': ('foundation_filefield_widget/foundation-filefield.css',)}

    template_with_clear = ''  # We don't need this
    template_with_initial = '%(input)s'

    def __init__(self, attrs=None, template='foundation_filefield_widget/foundation_filefield_widget.html'):
        super(FoundationFileInput, self).__init__(attrs=attrs)
        self.template = template

    def render(self, name, value, attrs=None):
        attrs = attrs or {}
        id = self.build_attrs(attrs, type=self.input_type, name=name)['id']
        attrs.update({"onchange": "$(this).prev().val(this.value.replace('C:\\\\fakepath\\\\', ''));"
                                  "$(this).prev()[0].onclick = null;".format(id),
                      "class": attrs.get("class", "") + " compact hidden"})

        return mark_safe(render_to_string(self.template, {
            'input': super(FoundationFileInput, self).render(name, value, attrs),
            'id': id,
            'value': value
        }))


class FoundationImageInput(forms.ClearableFileInput):

    class Media:
        css = {'all': ('foundation_filefield_widget/foundation-imagefield.css',)}

    template_with_clear = ''  # We don't need this
    template_with_initial = '%(input)s'

    def __init__(self, attrs=None, template='foundation_filefield_widget/foundation_imagefield_widget.html'):
        super(FoundationImageInput, self).__init__(attrs=attrs)
        self.template = template

    def render(self, name, value, attrs=None):
        attrs = attrs or {}
        id = self.build_attrs(attrs, type=self.input_type, name=name)['id']
        attrs.update({"onchange": "if (this.files && this.files[0]) {{"
                                  "var that = this;"
                                  "var reader = new FileReader();"
                                  "reader.onload = function(e) {{$(that).prev(\"img\").attr('src', e.target.result);}};"
                                  "reader.readAsDataURL(this.files[0]);"
                                  "}}".format(id),
                      "class": attrs.get("class", "") + " compact hidden"})

        return mark_safe(render_to_string(self.template, {
            'input': super(FoundationImageInput, self).render(name, value, attrs),
            'id': id,
            'value': value,
            'STATIC_URL': settings.STATIC_URL
        }))
