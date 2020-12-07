from django import forms

class RelyForm(forms.Form):
    first_name = forms.CharField(label="First Name",
                                    max_length=100,
                                    widget=forms.TextInput(attrs={'class': 'form-control'})
                                    )
    last_name = forms.CharField(label="Last Name",
                                    max_length=100,
                                    widget=forms.TextInput(attrs={'class': 'form-control'})
                                    )
    dob = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))
    income = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'min':'1', 'step': 'any'}))