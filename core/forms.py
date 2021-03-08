from django.core.mail.message import EmailMessage
from django import forms
from .models import Product


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=80)
    email = forms.EmailField(label='E-mail', max_length=100)
    subject = forms.CharField(label='Assunto', max_length=100)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        content = f'Nome: {name}\nE-mail: {email}\nAssunto: {subject}\nMensagem: {message}'

        mail = EmailMessage(
            subject='BACKEND DJANGO',
            body=content,
            from_email='contato@seudominio.com.br',
            to=['contato@seudominio.com.br, '],
            headers={'Reply-To': email}
        )
        mail.send()


class ProductModelForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'image']
