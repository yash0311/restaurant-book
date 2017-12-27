from django.core.exceptions import ValidationError


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )

CATEGORIES=['indian','mexican','chinese','american']

def validate_category(value):
	if value not in CATEGORIES:
		raise ValidationError('this is not a valid category')
