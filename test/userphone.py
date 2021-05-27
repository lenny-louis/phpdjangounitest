class UserCreateProfileForm(forms.ModelForm):
    fields = ['phone_mobile']

    def clean(self):
        cd = self.cleaned_data
        validate_phonenumber(cd.get('phone_mobile', None))
        return cd

    def validate_phonenumber(phone_number):
        for char in phone_number:
            if not char.isdigit():
                raise ValidationError("Phone number must be number")

