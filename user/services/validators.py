from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import re


validate_phone = RegexValidator(
    regex=r"^998\d{9}$",
    message="Phone number must begin with 998 and contain only 12 numbers",
)

# def validate_phone(value):
#     phone = re.compile(r'^998\d{9}$')
#     if phone.match(value):
#         return value
#     else:
#         raise ValidationError('Wrong phone number!')
