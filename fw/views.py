from django.shortcuts import render

def fw_list(request):
    return render(request, 'fw/fw_list.html', {})
