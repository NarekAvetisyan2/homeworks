from abc import ABC,abstractmethod


class Patients:
    def __init__(self, name, age, med_history):
        self.name = name
        self.age = age
        self.med_history = med_history

class Doctors:
    def __init__(self, name, contact):
        self.name = name
        self.contanct = contact
        self.appointments = []

    def Appoinments(self, appoinment):
        return self.appointments.append(appoinment)

    def View_Appoinments(self):
        return self.appointments

class Medical_Staff:
    def __init__(self, name, position):
        self.name =name
        self.position = position

    def Hospital_Oper(self):
        return (f"{self.name} today works on sekcia {self.position}")

class Med_Proc(ABC):
    @abstractmethod
    def Med_Oper(self):
        pass

class Surgeries(Med_Proc):
    def __init__(self, name, surgeries_type):
        self.name = name
        self.surgeries_type = surgeries_type

    def Med_Oper(self):
        return (f"Surgeries type: {self.surgeries_type}\n"
                f"Patient name: {self.name}")

class Check_Ups(Med_Proc):
    def __init__(self, name, check_type):
        self.name = name
        self.check_type = check_type

    def Med_Oper(self):
        return (f"Name is: {self.name}\n"
                f"Check_Ups is: {self.check_type}")

med_proc = Surgeries("Vaghinak", "Botex")
print(med_proc.Med_Oper())
med_proc = Check_Ups("Armenak", "Aryan analiz")
print((med_proc.Med_Oper()))
doc = Doctors("Xuan", 1111)
doc.Appoinments("Hashish")
doc.Appoinments("Crystal")
print(doc.View_Appoinments())
staff = Medical_Staff("Macak", "Mashkaban")
print(staff.Hospital_Oper())
