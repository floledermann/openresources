from django.forms.widgets import Widget, HiddenInput, Select
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.forms.util import flatatt

class ConstWidget(Widget):
    """
    Non-editable Widget that only displays its value.
    """
    def __init__(self, label=None, *args, **kwargs):
        self.label=label
        super(ConstWidget, self).__init__(*args, **kwargs)

    def _format_value(self, value):
        if self.is_localized:
            return formats.localize_input(value)
        return value

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        final_attrs['value'] = force_unicode(self._format_value(value))
        final_attrs['type'] = 'hidden'
        return mark_safe(u'%s <code>[%s]</code><input%s />' % (self.label, value, flatatt(final_attrs)))


class ComboBox(Select):
    """
    Input widget with additional configurable dropdown of values.
    """
    def __init__(self, attrs=None, choices=[]):
        super(ComboBox, self).__init__(attrs, choices)
        # always make sure there is an empty item at the start of the list
        if self.choices and self.choices[0] and self.choices[0][0]:
            self.choices.insert(0,('',''))

    def render(self, name, value, attrs=None):

        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_unicode(value)
        output = [u'<input type="text"%s />' % flatatt(final_attrs)]
        options = self.render_options((), [value])
        if options:
            output.append(u'<select class="combo-select" id="%s_SELECT">' % (final_attrs['id']))
            output.append(options)
            output.append(u'</select>')
        return mark_safe(u'\n'.join(output))

    class Media:
        js = ('openresources/js/edit.js')

