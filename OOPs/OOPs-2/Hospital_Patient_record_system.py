'''7. Hospital Patient Record System
Problem

Create a patient management system.

Requirements

Each patient should contain:

patient id
name
disease
doctor assigned
Functionalities
Display patient details
Change doctor
Count total patients admitted
Additional Task

Create patient from formatted string using class method.'''

class Hospital:
    total_patient = 0
    def __init__(self,patient_id,name,disease,doctor_assigned):
        self.__patient_id = patient_id
        self.__name = name
        self.__disease = disease
        self.__doctor_assigned = doctor_assigned

        Hospital.total_patient+=1

    def set_doctor(self,doctor):
        #doctor = input("Enter doctor name :")
        self.__doctor_assigned = doctor

    @classmethod
    def create_patient(cls,data):
        patient_id,name,disease,doctor_assigned = data.split(",")
        return cls(int(patient_id),name,disease,doctor_assigned)
        

    @classmethod
    def count(cls):
        print(f"Total Patients : {cls.total_patient}")

    def display_details(self):
        print(f"Patient's id : {self.__patient_id}\nPatient's Name : {self.__name}\nPatient's Disease : {self.__disease}\nDoctor Assigned : {self.__doctor_assigned}")

p1 = Hospital(101,"Koshiki","Fever","Dr.Sharma")
p1.display_details()
p1.set_doctor("Dr.Arya")
p1.display_details()
p1.count()

p2 = Hospital.create_patient("102,Shriya,Headache,Dr.Sharma")
p2.display_details()
p2.set_doctor("Dr.Arya")
p2.display_details()
p2.count()
