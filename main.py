from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post("/webhook")
async def dialogflow_webhook(request: Request):
    req_data = await request.json()
    print("Request Data:", req_data)
    intent_name = req_data.get("queryResult", {}).get("intent", {}).get("displayName")
    response_text = "Default response"

    if intent_name == "Default Welcome Intent":
        response_text = "Hello! Welcome to F Salon Academy. How can I assist you today?"
    elif intent_name == "Greeting Intent":
        response_text = (
            "Hey! Our Academy provides expert-led courses in various fields: \n"
            "1. Makeup Artistry (Basic, Bridal, Advanced)\n"
            "2. Beauty Science & Skincare\n"
            "3. Hair Styling and Technology\n"
            "4. Spa & Ayurveda Therapies\n"
            "5. Nail Art and Extension\n"
            "6. Cosmetic Formulations.\n"
            "Would you like to know more about a specific course?"
        )

    return {
        "fulfillmentText": response_text
    }

@app.get("/")
async def read_root():
    return {"message": "FastAPI server is running. Welcome to the F Salon Academy backend!"}

@app.get("/favicon.ico")
async def favicon():
    return {"message": "No favicon available"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)




