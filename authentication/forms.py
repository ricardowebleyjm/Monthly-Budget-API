from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import BudgetUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = BudgetUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = BudgetUser
        fields = ("email",)
