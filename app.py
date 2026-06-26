from fastapi import FastAPI

app = FastAPI(title="Loan Eligibility API")


@app.get("/")
def home():
    return {
        "message": "Welcome to Loan Eligibility API"
    }


@app.post("/predict")
def predict(income: int, age: int):

    if income >= 30000 and age >= 18:
        return {"loan": "Approved"}

    return {"loan": "Rejected"}