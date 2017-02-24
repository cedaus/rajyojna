from django.db import models

#http://bitofpixels.com/blog/unique-on-charfield-when-blanktrue/
class NullableEmailField(models.EmailField):
    description = "EmailField that stores NULL but returns ''"
    def to_python(self, value):
        if isinstance(value, models.EmailField):
            return value
        return value or ''
    def get_prep_value(self, value):
        return value or None
