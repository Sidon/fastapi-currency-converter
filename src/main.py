from fastapi import FastAPI
from src.api.routes import api_router

app = FastAPI(
    title="Currency converter",
    description="Api for currency converter",
    version="0.0.1",
    contact={
        "name": "Sidon",
        "email": "sidoncd@gmail.com",
    },
    license_info={"name": "MIT"},
)
    
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)