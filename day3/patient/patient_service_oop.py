from patient import Patient

class Patient_service:
    def __init__(self):
        self.patients = dict()

    def patient_add(self, id, name):
        patient = Patient(id, name)
        self.patients[patient.id] = patient
        print('Patient is created')

    def patient_remove(self, id):
        patient = self.patients.get(id)
        if patient == None:
            print(f'Patient with id = {id} not found')
            return
        print(patient)
        if input('Are you sure to delete (Yes/No): ').lower() == 'yes':
            del self.patients[id]
            print(f'Patient with id = {id} deleted')

    def list_patients(self):
        for id in self.patients:
            print(self.patients[id])

    def list_patient_by_id(self, id):
        patient = self.patients.get(id)
        if patient == None:
            print(f'Patient with id = {id} not found')
            return
        print(patient)

    def patient_update(self, id):
        patient = self.patients.get(id)
        if patient == None:
            print(f'Patient with id = {id} not found')
            return
        new_name = input(f'Enter new name of the patient {patient.name}: ')
        patient.name = new_name
        print('Patient update completed')
