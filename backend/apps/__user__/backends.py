from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ValidationError
from django.db.models import Q


class EmailOrUsernameModelBackend(ModelBackend):
    """
    Authentication backend which allows users to authenticate using either their
    username or email address

    Source: https://stackoverflow.com/a/35836674/59984
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()
        query = Q(**{user_model.USERNAME_FIELD: username}) | Q(email__iexact=username)
        # So `username` is something like baseplate-admin#0001
        # we need to split to get the username and discriminator
        try:
            _username_ = username.split("#")
            username = _username_[0]
            username_discriminator = _username_[1]
            query &= Q(username_discriminator=username_discriminator)
        except IndexError:
            pass

        # The `username` field is allows to contain `@` characters so
        # technically a given email address could be present in either field,
        # possibly even for different users, so we'll query for all matching
        # records and test each one.
        users = user_model._default_manager.filter(query)

        # Test whether any matched user has the provided password:
        for user in users:
            if user.check_password(password):
                return user

        if not users:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (see
            # https://code.djangoproject.com/ticket/20760)
            user_model().set_password(password)
