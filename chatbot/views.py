from openai import OpenAI
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def chat(request):
    return render(request, 'chatbot/index.html')

from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key='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')
@csrf_exempt
def generate_response(prompt):
    try:
        # Use the OpenAI API to generate a response
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt}
            ]
        )
        # Extract and return the response content from the choices
        return response.choices[0].message.content
    except Exception as e:
        print("Error occurred:", e)  # Print the error message for debugging
        return None


@csrf_exempt
def get_response(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')

        if user_input.strip() == '':
            return JsonResponse({'response': 'Please provide a valid input.'})

        try:
            response = generate_response(user_input)
        except Exception as e:
            print("Error occurred:", e)  # Print the error message for debugging
            return JsonResponse({'response': 'An error occurred while generating the response.'})

        return JsonResponse({'response': response})

    else:
        return JsonResponse({'response': 'Invalid request method.'})
