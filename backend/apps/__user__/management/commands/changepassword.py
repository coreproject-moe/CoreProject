import getpass

from django.conf import settings
from django.contrib.auth.management.commands.changepassword import (
    Command as ChangePasswordCommand,
    UserModel,
)
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.management.base import CommandError
from django.db.models import CharField, Value
from django.db.models.functions import Cast, Concat, LPad


class Command(ChangePasswordCommand):
    def handle(self, *args, **options):
        if options["username"]:
            username = options["username"]
        else:
            username = getpass.getuser()

        try:
            u = (
                UserModel._default_manager.using(options["database"])
                .annotate(
                    username_discriminator_as_string=Cast(
                        "username_discriminator", output_field=CharField()
                    ),
                    username_with_discriminator=Concat(
                        "username",
                        Value("#"),
                        LPad(
                            "username_discriminator_as_string",
                            int(settings.USERNAME_DISCRIMINATOR_LENGTH),
                            Value("0"),
                        ),
                        output_field=CharField(),
                    ),
                )
                .get(
                    username_with_discriminator=username,
                )
            )
        except UserModel.DoesNotExist:
            raise CommandError("user '%s' does not exist" % username)
        self.stdout.write("Changing password for user '%s'" % u)

        MAX_TRIES = 3
        count = 0
        p1, p2 = 1, 2  # To make them initially mismatch.
        password_validated = False
        while (p1 != p2 or not password_validated) and count < MAX_TRIES:
            p1 = self._get_pass()
            p2 = self._get_pass("Password (again): ")
            if p1 != p2:
                self.stdout.write("Passwords do not match. Please try again.")
                count += 1
                # Don't validate passwords that don't match.
                continue
            try:
                validate_password(p2, u)
            except ValidationError as err:
                self.stderr.write("\n".join(err.messages))
                count += 1
            else:
                password_validated = True

        if count == MAX_TRIES:
            raise CommandError(
                "Aborting password change for user '{}' after {} attempts".format(
                    u, count
                )
            )

        u.set_password(p1)
        u.save()

        return "Password changed successfully for user '%s'" % u
