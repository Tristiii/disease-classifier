from utils import dataframe, get_model
from joblib import dump

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def train_model() -> float:
    df = dataframe()
    X, y = df.loc[:, 'anxiety and nervousness':], df.loc[:, 'diseases':'diseases']
    Xtrain, Xtest, ytrain, ytest = train_test_split(
        X.values, y.values, test_size=0.2, random_state=42
    )

    model = DecisionTreeClassifier(random_state=42)
    model.fit(Xtrain, ytrain)
    dump(model, get_model())

    ypred = model.predict(Xtest)
    return accuracy_score(ytest, ypred)