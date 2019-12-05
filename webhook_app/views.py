from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse
import json

@csrf_exempt
@require_http_methods(['GET', 'POST'])
def webhook(request):
    # Grabbing JSON data
    json_data = json.loads(request.body)

    # Getting the user that made the request
    current_user = json_data['object']

    # Getting the user's username
    username = current_user["username"]

    # Getting the last character of the username
    last_character = username[0]

    # Checking if last letter is a number
    if last_character.is_alpha(): # Letter
        username += "0" # Adding a zero to the end of the username
    else: # Number
        # Adding the number + 1 to the end of the username
        number = int(last_character)
        number += 1
        username += str(number)

    # Forming the JSON data
    output_json = {
        "success": {
            "username": username
        }
    }

    # Returning the JSON data
    return JsonResponse(output_json)
