from .models import User


# login with phone-number:
class PhoneAuthBackend:
    def authenticate(self, request, username=None, password=None):
        # username = phoneNumber
        try:
            user = User.objects.get(phone_number=username)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

# login with Email:
class EmailAuthBackend:
    def authenticate(self, request, username=None, password=None):
        # username = Email
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
