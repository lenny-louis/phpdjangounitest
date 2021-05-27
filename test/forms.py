from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean(self):
        cleaned_data = super(CustomUserCreationForm, self).clean()
        username = cleaned_data.get('username')
        if ('@', '.', '-', '+') in username:
            self.add_error('username', 'Symbols @/./-/+ are not allowed in username.')
        return cleaned_data

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name')
        

    def clean(self):
        cleaned_data = super(CustomUserChangeForm, self).clean()
        username = cleaned_data.get('username')
        if ('@', '.', '-', '+') in username:
            self.add_error('username', 'Symbols @/./-/+ are not allowed in username.')
        return cleaned_data

