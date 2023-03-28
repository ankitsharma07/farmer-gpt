import json
import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from django.shortcuts import render
from .models import Message

# Set up the OpenAI API key
openai.api_key = settings.OPENAI_API_KEY


def chat(request):
    messages = Message.objects.order_by("timestamp")
    context = {"messages": messages}
    return render(request, "chatter/chat.html", context)


@csrf_exempt
def process_message(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print("data:", data)


        if data.get("message"):
            # Connecting with OpenAI
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=data["message"],
                max_tokens=200,
                n=1,
                stop=None,
                temperature=0.7,
            )

            print("reponse from openai:: ", response)
            generated_text = response.choices[0].text.strip()
            print("generated text:", generated_text)

            return JsonResponse({"response": generated_text})

        elif data.get("audio"):
            # process the audio using whisper api
            pass

    return JsonResponse({"error": "Invalid Request"}, status=400)