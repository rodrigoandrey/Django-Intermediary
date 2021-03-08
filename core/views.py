from django.shortcuts import render
from django.contrib import messages

from .forms import ContactForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def contact(request):
    form = ContactForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['name']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['subject']
            mensagem = form.cleaned_data['message']

            print('Mensagem Enviada')
            print(f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}')

            messages.success(request, 'Mensagem enviada com sucesso')
            form = ContactForm()
        else:
            messages.error(request, 'Erro ao enviar Mensagem')

    context = {
        'form': form
    }
    return render(request, 'contact.html', context)


def product(request):
    return render(request, 'product.html')
