from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post("/webhook")
async def dialogflow_webhook(request: Request):
    req_data = await request.json()
    intent_name = req_data.get("queryResult", {}).get("intent", {}).get("displayName")
    response_text = "Default response"

    if intent_name == "Default Welcome Intent":
        response_text = "Hello! Welcome to F Salon Academy. How can I assist you today?"
    elif intent_name == "Greeting Intent":
        response_text = "Hey! Our Academy provides expert-led courses in various fields: \n1. Makeup Artistry (Basic, Bridal, Advanced)\n 2. Beauty Science & Skincare \n3. Hair Styling and Technology\n4. Spa & Ayurveda Therapies\n5. Nail Art and Extension\n6. Cosmetic Formulations.\nWould you like to know more about a specific course?"

    return {
        "fulfillmentText": response_text
    }
    
@app.get("/")
async def read_root():
    return {"message": "FastAPI server is running. Welcome to the F Salon Academy backend!"}




