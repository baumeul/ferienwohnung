from django.shortcuts import render
from django.utils import timezone
from .models import Gast


def fw_list(request):
    gaeste = Gast.objects.filter(created__lte=timezone.now()).order_by('created')
    return render(request, 'fw/fw_list.html', {'gaeste': gaeste})
