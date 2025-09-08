from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406354606',
        'name': 'Annisa Fakhira Cendekia',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)