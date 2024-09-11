from django.shortcuts import render

def show_main(request):
    context = {
        'application' : 'The Goods Place',
        'name': 'Meisya Najla Aqilah',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
