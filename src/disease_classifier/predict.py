from utils import get_model, dataframe
from joblib import load

def predict_disease(symptoms: list[str]) -> str:
    model = load(get_model())
    all_symptoms = dataframe().columns[1:]

    data = []
    for s in all_symptoms:
        if s in symptoms and s != 'diseases':
            data.append(1)
        else:
            data.append(0)

    pred = model.predict([data])[0]
    return pred