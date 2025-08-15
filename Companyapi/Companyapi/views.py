from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("Return home page")
    friends=[
        "Sneha",
        "Supriyo",
        "Saidul"
    ]
    # return HttpResponse("This is home page")
    return JsonResponse(friends, safe=False)