from patient import Patient

patients = dict() # {}

def patient_add(id, name):
    global patients
    patient = Patient(id, name)
    patients[patient.id] = patient
    print('Patient is created')

def patient_remove(id):
    global patients
    patient = patients.get(id)
    if patient == None:
        print(f'Patient with id = {id} not found')
        return
    print(patient)
    if input('Are you sure to delete (Yes/No): ').lower() == 'yes':
        del patients[id]
        print(f'Patient with id = {id} deleted')

def list_patients():
    global patients
    for id in patients:
        print(patients[id])

def list_patient_by_id(id):
    global patients
    patient = patients.get(id)
    if patient == None:
        print(f'Patient with id = {id} not found')
        return
    print(patient)

def patient_update(id):
    global patients
    patient = patients.get(id)
    if patient == None:
        print(f'Patient with id = {id} not found')
        return
    new_name = input(f'Enter new name of the patient {patient.name}: ')
    patient.name = new_name
    print('Patient update completed')
