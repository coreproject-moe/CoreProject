from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_str
from rest_framework import serializers


# https://stackoverflow.com/a/28011896
class GetOrCreateSlugRelatedField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        queryset = self.get_queryset()
        try:
            return queryset.get_or_create(**{self.slug_field: data})[0]
        except ObjectDoesNotExist:
            self.fail("does_not_exist", slug_name=self.slug_field, value=smart_str(data))
        except (TypeError, ValueError):
            self.fail("invalid")
