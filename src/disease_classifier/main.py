from utils import dataframe
from train import train_model
from predict import predict_disease

print('I am a disease predictor.')
print(f'Accuracy: {round(train_model() * 100, 2)}%')

all_symptoms = dataframe().columns[1:]
online = True
while online:
    i = input('Enter command: ')
    match i.split():
        case ['quit']:
            online = False
        case ['predict']:
            symptoms = []
            adding = True
            while adding:
                s = input('Enter symptom ("done" if finished): ')
                if s == 'done':
                    adding = False
                elif s in all_symptoms:
                    symptoms.append(s)
                    print(f'Added: {', '.join(symptoms)}.')
                else:
                    print('I do not recognize this symptom.')
            print(f'Disease prediction: {predict_disease(symptoms)}.')
        case ['symptoms']:
            print(f'All symptoms: {', '.join(all_symptoms)}.')
        case _:
            print('I do not recognize this command.')