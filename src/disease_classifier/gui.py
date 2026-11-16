from utils import dataframe
from predict import predict_disease

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton
)
from PySide6.QtCore import Qt

all_symptoms = dataframe().columns[1:]

class DiseaseClassifier(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Disease Classifier')
        self.setFixedSize(500, 250)

        layout = QVBoxLayout()

        self.description = QLabel('This disease classifier has an accuracy of 81.44%. Please enter your symptoms below.')
        layout.addWidget(self.description)

        self.symptoms = []
        self.added = QLabel(f'Added symptoms: {', '.join(self.symptoms)}')
        layout.addWidget(self.added)

        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText('Please enter your symptoms')
        layout.addWidget(self.text_input)

        self.add_button = QPushButton('Add')
        self.add_button.clicked.connect(self.add_symptom)
        layout.addWidget(self.add_button)

        self.predict_button = QPushButton('Predict')
        self.predict_button.clicked.connect(self.add_prediction)
        layout.addWidget(self.predict_button)

        self.result = QLabel('Please enter your symptoms')
        self.result.setStyleSheet(f"""
            background-color: orange;
            color: white;
            font-weight: bold;
            padding: 10px;
        """)
        self.result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.result)

        self.setLayout(layout)

    def add_symptom(self) -> None:
        message = self.text_input.toPlainText()
        if message not in all_symptoms:
            self.result.setText(f'{message} is not recognised as a symptom')
            self.result.setStyleSheet(f"""
                background-color: red;
                color: white;
                font-weight: bold;
                padding: 10px;
            """)
        else:
            self.symptoms.append(message)
            self.added.setText(f'Added symptoms: {', '.join(self.symptoms)}')
            self.result.setText(f'Successfully added {message}')
            self.result.setStyleSheet(f"""
                background-color: green;
                color: white;
                font-weight: bold;
                padding: 10px;
            """)

    def add_prediction(self) -> None:
        if not self.symptoms:
            self.result.setText(f'Please enter your symptoms')
            self.result.setStyleSheet(f"""
                background-color: orange;
                color: white;
                font-weight: bold;
                padding: 10px;
            """)
        else:
            prediction = predict_disease(self.symptoms)

            self.result.setText(f'Prediction: {prediction}')
            self.result.setStyleSheet(f"""
                background-color: blue;
                color: white;
                font-weight: bold;
                padding: 10px;
            """)
            self.symptoms = []
            self.added.setText(f'Added symptoms: {', '.join(self.symptoms)}')