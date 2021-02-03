from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from account.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(verbose_name=_('phone number'),
                             max_length=12,
                             null=True, unique=True, validators=[
            RegexValidator(regex=r'^996\d{9}$', message=_('Pass valid phone number'))
        ])
    email = models.EmailField(verbose_name=_('email address'), null=True, unique=True)
    first_name = models.CharField(verbose_name=_('first name'),
                                  max_length=30, blank=True)
    last_name = models.CharField(verbose_name=_('last name'),
                                 max_length=30, blank=True)
    date_joined = models.DateTimeField(verbose_name=_('date joined'), auto_now_add=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(_('active'), default=True)
    avatar = models.ImageField(upload_to='user_avatars/', null=True, blank=True)
    access_level = models.PositiveSmallIntegerField(default=0, verbose_name=_('Access level'))
    objects = UserManager()

    USERNAME_FIELD = 'phone'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.phone or self.email

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def clean(self):
        super(User, self).clean()
        if not (self.email or self.phone):
            raise ValidationError(_('Provide at least phone or email'))
