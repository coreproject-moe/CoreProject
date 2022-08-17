from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MinValueValidator, RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager
from .mixins.resize import ResizeImageMixin
from .validators import username_validator

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin, ResizeImageMixin):
    username = models.CharField(
        _("username"),
        max_length=150,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), blank=True, unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    username_discriminator = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r"^(?=[\S\s]{1,%d}$)[\S\s]*"
                % settings.USERNAME_DISCRIMINATOR_LENGTH,
                message="Length has to be 4",
                code="nomatch",
            ),
            MinValueValidator(1),  # Same thing but remove negative digits
        ],
    )
    avatar = models.ImageField(upload_to="avatars", default=None, blank=True, null=True)
    ip = models.GenericIPAddressField(null=False, blank=False)

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def get_username_with_discriminator(self) -> str:
        return f"{self.username}#{str(self.username_discriminator).zfill(4)}"

    def save(self, *args, **kwargs) -> None:
        # if self.avatar:
        #     file = self.resize(self.avatar)
        #     self.avatar.save(f"{self.username}.avif", file, save=False)

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.get_username_with_discriminator()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        unique_together = ("username", "username_discriminator")
