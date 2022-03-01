from django.contrib.auth.hashers import make_password


class ValidatePasswordMixin(object):
    def validate_password(self, cleaned_data: dict) -> dict:
        """
        A custom mixin to make sure the passwords are the same.
        """
        password: str = cleaned_data.get("password")
        confirm_password: str = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error(
                "confirm_password",
                """'Password' and 'Confirm Password' does not match.""",
            )

        if password and confirm_password:
            hashed_password = make_password(password)
            cleaned_data["password"] = hashed_password
            cleaned_data["confirm_password"] = hashed_password

        else:
            cleaned_data.pop("password")
            cleaned_data.pop("confirm_password")
