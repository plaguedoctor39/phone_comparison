from django.shortcuts import render
from phones.models import Phone, SamsungPhone, ApplePhone


def show_catalog(request):
    template = 'catalog.html'
    phones = list(Phone.objects.all())
    apple = ApplePhone
    samsung = SamsungPhone
    context = {'phones': phones,
               'apple': apple.add_info,
               'samsung': samsung.add_info
               }
    return render(
        request,
        template,
        context
    )
