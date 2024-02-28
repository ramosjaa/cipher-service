from django.http import JsonResponse
from .ciphers import caesor_encode
def greetings(request):
    result = {"message": "Welcome to cipher service!"}
    return JsonResponse(result)
def encode(request, plaintext, shift):
    parameters = dict(request.GET)
    print(parameters)
    cipher = caesor_encode(plaintext, shift)
    return JsonResponse({"cipher": cipher})