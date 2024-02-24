from django.shortcuts import render
from lead.models import lead
from django.core.mail import send_mail
import datetime

# Create your views here.

def index_view(request):

    if request.method == 'POST':

        name = request.POST.get('nome_usuario')
        email = request.POST.get('email_usuario')
        phone = request.POST.get('telefone_usuario')
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        lead_obj = lead.objects.create(
            name = name,
            email = email,
            phone = phone,
            date = date
        )
        lead_obj.save()

        send_mail(
            'Um novo lead foi capturado',
            f'Nome: {name}\nEmail:{email}\nTelefone:{phone}\nData:{date} ',
            'lead@gmail.com',
            ['gabrielrfreitas2707@gmail.com'],
            fail_silently=False
        )


        return render (request,
                 'index.html')

    

    return render (request,
                 'index.html')