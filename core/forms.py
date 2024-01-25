from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="nom et prenom", required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ecrivez votre nom et prenom'}), min_length=3, max_length=100)
    email = forms.EmailField(label="courriel electronique", required=True, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'ecrivez votre email'}), min_length=3, max_length=100)
    content = forms.CharField(label="message", required=True, widget=forms.Textarea(attrs={'class':'form-control','placeholder':'ecrivez votre message','rows':3}), min_length=10, max_length=1000)
