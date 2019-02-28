from django import forms
from .models import CarModel


class CarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = "__all__"

    def clean_mpg(self):
        mpgData = self.cleaned_data["mpg"]

        if mpgData < 20:
            raise forms.ValidationError("That's less than a truck")

        if mpgData > 500:
            raise forms.ValidationError("That's impossible!!")
        return mpgData

    def clean_year(self):
        yearData = self.cleaned_data['year']

        if yearData < 2019:
            raise forms.ValidationError("That's not new")
