from utils import dataframe, get_model
from train import train_model
from gui import DiseaseClassifier

import sys
from PySide6.QtWidgets import QApplication

if not get_model().exists():
    train_model()

app = QApplication(sys.argv)
window = DiseaseClassifier()
window.show()
app.exec()