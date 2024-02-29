from django.shortcuts import render
from django.http import JsonResponse
from openai import OpenAI
from django.core.serializers.json import DjangoJSONEncoder
import json

client = OpenAI(api_key="")

def ask_openai(message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": 'You are a chatbot with deep knowledge in 3GPP'},
            {"role": "user", "content": message}
        ],
        temperature=0.5,
        max_tokens=2000,
        stop=None
    )
    answer = response.choices[0].message
    return answer

# Create your views here.
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        
        # Extract the content attribute from ChatCompletionMessage
        response_content = response.content

        return JsonResponse({'message': message, 'response': response_content})
    
    return render(request, 'chatbot.html')