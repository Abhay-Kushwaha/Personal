# WhatsApp Script via Twilio

This project allows you to send WhatsApp messages using the **Twilio API**.  
It’s ideal for automated notifications, recovery codes, or alert systems.

## Environment Variables

Before running the script, create a `.env` file in your project root directory and add the following:

```bash
Recovery_Code=
Account_SID=
Auth_Token=
From_Twilio=whatsapp:+<number>
```

## Activate the Virtual Environment
```bash
venv\Scripts\activate       # For Windows
source venv/bin/activate    # For macOS / Linux
```

## Install Required Dependencies
```bash
pip install -r req.txt
```

## Run the Script
```bash
python whatsapp.py
```