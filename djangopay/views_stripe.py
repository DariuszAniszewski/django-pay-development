from django.http.response import HttpResponse


def start_payment(request):
    print(request.POST)
    return HttpResponse("DD")