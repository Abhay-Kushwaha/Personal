# rules/wa_webhook.py  
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from twilio.rest import Client as TwilioClient
import requests
import json

@csrf_exempt
def whatsapp_webhook(request):
    if request.method != "POST":
        return HttpResponse(status=405)

    from_phone = request.POST.get("From", "")
    to_phone = request.POST.get("To", "")
    body = request.POST.get("Body", "")

    if not from_phone or not to_phone:
        return HttpResponse("<Response/>", content_type="text/xml")
    
    fixed_text = (
        "Hello We are your AI Insights Whatsapp Atom AI Assistant! 🚀\n\n "
        "Here are the available insights you can generate. \n"
        "Tap any option to proceed 👇\n\n"
    )

    request_url=settings.PUBLIC_BASE_URL

    try:
        response = requests.get(request_url, timeout=5, auth=(settings.BASIC_AUTH_USER, settings.BASIC_AUTH_PASS))
        prompts = response.json()
    except Exception as e:
        print("Error fetching prompts:", e)
        prompts = []

    #################################
    # Build Buttons
    #################################
    # WhatsApp requires at MOST 3 quick reply buttons
    button1 = prompts[0]["label"][:20] if len(prompts) > 0 else "Option 1"
    button2 = prompts[1]["label"][:20] if len(prompts) > 1 else "Option 2"
    button3 = prompts[2]["label"][:20] if len(prompts) > 2 else "Option 3"
    variables = {
        "1": button1,
        "2": button2,
        "3": button3
    }

    #################################
    # Build numbered List
    #################################
    menu_text = fixed_text
    if prompts:
        for idx, p in enumerate(prompts, start=1):
            menu_text += (
                f"*{idx}. {p['label']}*\n"
                f"_{p['short_description'][:120]}..._\n\n"
            )
    else:
        menu_text += "No active insight prompts are available."


    try:
        client = TwilioClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        client.messages.create(
            from_=to_phone,
            to=from_phone,
            content_sid=settings.TWILIO_TEMPLATE_SID,   # For Different Content Types
            body=menu_text,                             # Plain text message
            content_variables=json.dumps(variables)     # Variables for buttons
        )
    except Exception as e:
        print("Error in whatsapp webhook {}".format(e))

    return HttpResponse("<Response/>", content_type="text/xml")

@csrf_exempt
def whatsapp_status(request):
    return HttpResponse(status=200)
