import sys
from patient_service import patient_add, patient_remove, patient_update, list_patients, list_patient_by_id

def menu():
    choice = int(input('1:Add 2:Delete 3:Update 4:ListAll 5:Search 6:Exit \nYour choice: '))
    if choice == 1:
        id = int(input('Enter patient id: '))
        name = input('Enter patient name: ')
        patient_add(id, name)
    elif choice == 2:
        id = int(input('Enter patient id: '))
        patient_remove(id)
    elif choice == 3:
        id = int(input('Enter patient id: '))
        patient_update(id)
    elif choice == 4:
        list_patients()
    elif choice == 5:
        id = int(input('Enter patient id: '))
        list_patient_by_id(id)
    elif choice == 6:
        pass
    else:
        print('Invalid choice enetered')
    return choice

def patient_app():
    choice = menu()
    while choice != 6:
        choice = menu()
    print('Thank you being patient')