from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import random
import asyncio

app = FastAPI(title="AquaGuard AI Backend", description="Flood Detection API")

# Setup CORS so the React frontend can talk to it
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to AquaGuard AI backend"}

@app.get("/api/risk-areas")
def get_risk_areas():
    """ Returns latest known flood risk areas """
    return [
        { "id": 1, "lat": 24.8607, "lng": 67.0011, "radius": 15000, "level": "critical", "name": "South Karachi - High Risk" },
        { "id": 2, "lat": 25.3960, "lng": 68.3578, "radius": 25000, "level": "warning", "name": "Hyderabad - River Basin" },
        { "id": 3, "lat": 27.7244, "lng": 68.8228, "radius": 32000, "level": "critical", "name": "Sukkur Barrage Area" }
    ]

@app.post("/api/analyze")
async def analyze_image(file: UploadFile = File(...)):
    """ Endpoint to upload satellite/drone image and get inference """
    # Simulate processing time for the AI segmentation model (U-Net simulation)
    await asyncio.sleep(3)
    
    # Simulate an AI output
    risk_level = random.choice(["critical", "warning", "safe"])
    water_expansion_percentage = round(random.uniform(5.0, 45.0), 2)
    
    return {
        "status": "success",
        "filename": file.filename,
        "message": "Image analyzed successfully using segmentation model.",
        "analysis": {
            "risk_level": risk_level,
            "detected_water_expansion": f"{water_expansion_percentage}%",
            "evacuation_needed": risk_level == "critical"
        }
    }

# Run via: uvicorn main:app --reload
