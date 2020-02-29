class Hospital():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"welcome to {self.name} hospital!"

# -------------------------------------------------------------------------------------


class Employee():
    doctors = []
    sick_ppl = []

    def __init__(self, name):
        self.name = name

    def employ_signin(self, doctor='', super_admin=''):
        enter_email = input("please enter your email address: ")
        enter_password = input("please enter your password: ")
        for doctor in self.doctors:
            if doctor.email == enter_email and doctor.password == enter_password:
                print('signed in successfully!')
        if enter_email == admin.email and enter_password == admin.password:
            print(
                f'welcome back Super Admin, Jordan. your access level is {admin.authorization}')

    def employ_doc(self, doctor=''):
        doc_first_name = input("enter first name: ")
        doc_last_name = input("enter last name: ")
        doc_specialist = input("what do you specialize in: ")

        new_doctor = Doctor(doc_first_name, doc_last_name,
                            doc_specialist)
        print(new_doctor)
        print(f'your email: {new_doctor.email}')
        doc_pw = input('enter your password: ')
        new_doctor.password = doc_pw
        new_doctor.create_doc_acc()

    def create_patient(self):
        pat_first_name = input("please enter patient's first name: ")
        pat_last_name = input("please enter patient's last name: ")
        pat_age = input("please enter patient's age: ")
        pat_sickness = input("what sickness does the patient have? : ")
        new_patient = Patients(
            pat_first_name, pat_last_name, pat_age, pat_sickness)
        print(new_patient)
        self.sick_ppl.append(new_patient)
        print(self.sick_ppl)

    def delete_patient(self):
        del_first_name = input("please enter the patient's first name: ")
        del_last_name = input("please enter the patient's last name: ")
        print(self.sick_ppl)
        for ind, ppl in enumerate(self.sick_ppl):
            if ppl.first_name == del_first_name and ppl.last_name == del_last_name:
                del self.sick_ppl[ind]
                print(self.sick_ppl)

    def check_patient_info(self):
        check_first_name = input("please enter the patient's first name: ")
        check_last_name = input("please enter the patient's last name: ")
        for ppl in self.sick_ppl:
            if ppl.first_name == check_first_name and ppl.last_name == check_last_name:
                print('______________________')
                print('Patient Details: ')
                print(ppl.first_name, ppl.last_name)
                print(ppl.age)
                print(ppl.sickness)
# -------------------------------------------------------------------------------------


class Super_admin():
    def __init__(self, email, password, authorization=''):
        self.email = email
        self.password = password
        self.authorization = 'Super_Admin'

    def __repr__(self):
        return "{" + f'"email": "{self.email}", "password": "{self.password}", "authorization": "Super_Admin"' + "}"
# -------------------------------------------------------------------------------------


class Doctor(Employee):
    def __init__(self, first_name, last_name, expertise, password='', email=''):
        self.first_name = first_name
        self.last_name = last_name
        self.expertise = expertise
        self.email = f'{first_name}.{last_name}@NEXT.com'
        self.password = password

    def create_doc_acc(self):
        self.doctors.append(self)
        print(self.doctors)

    def __repr__(self):
        return "{" + f'"email": "{self.email}", "password": "{self.password}", "expertise": "{self.expertise}", "authorization": "Doctor"' + "}"
        # return f'{self.first_name} {self.last_name}, {self.expertise}, welcome!'

# -------------------------------------------------------------------------------------


class Patients():
    def __init__(self, first_name, last_name, age, sickness):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sickness = sickness

    def __repr__(self):
        return "{" + f'"first_name": "{self.first_name}", "last_name": "{self.last_name}", "age": "{self.age}", "sickness": "{self.sickness}", "authorization": "Patient"' + "}"

# -------------------------------------------------------------------------------------


 # ------Driver Code----
new_hospital = Hospital("NEXT")
new_Employs = Employee("NEXT")
admin = Super_admin(email="Jordan@NEXT.com", password="jjw93")
print(new_hospital)
show_directory = True
show_logindirectory = True

while show_directory == True:
    print('How can we help you today?')
    print('choose one of our services:')
    print('1. Create Doctor Account')
    print('2. Employee Sign in')
    print('3. Patient Sign up')
    print('4. Exit')
    user_input = input("your choice: ")

    if user_input == '1':
        new_Employs.employ_doc()
    if user_input == '2':
        new_Employs.employ_signin()
        show_directory = False
        while show_logindirectory == True:
            print('_______________________')
            print('Directory:')
            print('1. Add Patient information')
            print('2. Delete Patient information')
            print('3. Check Patient information')
            print('4. Back')
            user_input = input("your choice: ")
            if user_input == '1':
                new_Employs.create_patient()
            if user_input == '2':
                new_Employs.delete_patient()
            if user_input == '3':
                new_Employs.check_patient_info()
            if user_input == '4':
                show_logindirectory = False
                user_input = ''
    show_directory = True
    if user_input == '3':
        new_Employs.create_patient()
    if user_input == '4':
        show_directory = False
        print('bye bye')
