from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=80)
    email = forms.EmailField(label='E-mail', max_length=100)
    subject = forms.CharField(label='Assunto', max_length=100)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())
