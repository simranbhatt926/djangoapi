from django.http import HttpResponse, JsonResponse
def home_page(request):
    print("home page requested")
    friends=[
        "simran",
        "Sivani"
    ]
    return JsonResponse(friends,safe=False)
    # return HttpResponse("This is home page")