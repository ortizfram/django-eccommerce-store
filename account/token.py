from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):

    def _make_hask_value(self)