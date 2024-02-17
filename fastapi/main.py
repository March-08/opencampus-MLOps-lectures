# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
from sklearn.datasets import load_iris  # Add this import

app = FastAPI()

# Load the trained model
model = joblib.load("trained_model.joblib")

# Load iris dataset for target names
iris = load_iris()
class_names = iris.target_names.tolist()


class Item(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.post("/predict")
async def predict(item: Item):
    try:
        # Convert input to NumPy array
        input_data = np.array(
            [[item.sepal_length, item.sepal_width, item.petal_length, item.petal_width]]
        )

        # Make prediction
        prediction = model.predict(input_data)[0]

        return {
            "prediction": int(prediction),
            "class_name": class_names[int(prediction)],
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
