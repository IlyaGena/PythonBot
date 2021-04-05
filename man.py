class Man(object):
    def __init__(self, name, surname, age, sex):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
        
    def set_surname(self, surname):
        self.surname = surname

    def get_surname(self):
        return self.surname
        
    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age
        
    def set_sex(self, sex):
        self.sex = sex

    def get_sex(self):
        return self.sex