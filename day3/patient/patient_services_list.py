from patient import Patient

class Patient_service:
    def __init__(self):
        self.patients = list()

    def patient_add(self, id, name):
        patient = Patient(id, name)
        self.patients.append(patient)
        print('Patient is created')

    def patient_remove(self, id):
        for patient in self.patients:
            if patient.id == id:
                if input('Are you sure to delete (Yes/No): ').lower() == 'yes':
                    self.patients.remove(patient)
                    print(f'Patient with id = {id} deleted')
                    return
        print(f'Patient with id = {id} not found')        

    def list_patients(self):
        for patient in self.patients:
            print(patient)

    def list_patient_by_id(self, id):
        for patient in self.patients:
            if patient.id == id:
                print(patient)
                return
        print(f'Patient with id = {id} not found')
        
    def patient_update(self, id):
        i = 0
        for patient in self.patients:
            if patient.id == id:
                new_name = input(f'Enter new name of the patient {patient.name}: ')
                patient.name = new_name        
                self.patients[i] = patient
                print('Patient update completed')
                return
            i += 1
        print(f'Patient with id = {id} not found')
