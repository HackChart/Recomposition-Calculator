from datetime import datetime


class User:
    def __init__(self, name: str, height, weight, birthday: datetime, gender, bodyfat_percentage):
        self.name = name.title()
        self.height = height
        self.weight = weight
        self.birthday = birthday
        self.age = (datetime.now() - birthday).days // 365
        if gender.upper()[0] == 'M':
            self.gender = 'Male'
        elif gender.upper()[0] == 'F':
            self.gender = 'Female'
        else:
            self.gender = 'Other'
        self.bodyfat_percentage = bodyfat_percentage

        # TODO: primary goal
            # TODO: check against fringe cases (ie. gain muscle at 40% bf or lose at 6% bf)

        # TODO: lbm and appropriate update methods when weight/bf change - TEST
        self.lean_body_mass = None
        self.update_lean_body_mass()

        # TODO: fbm and appropriate update methods - TEST
        self.adipose_body_mass = None
        self.update_adipose_body_mass()

    # setters
    def rename(self, new_name):
        self.name = new_name

    def change_weight(self, new_weight):
        self.weight = new_weight

    def change_height(self, new_height):
        self.height = new_height

    def change_age(self, new_age):
        self.age = new_age

    def change_bodyfat_percentage(self, new_bf_percentage):
        self.bodyfat_percentage = new_bf_percentage

    def auto_update_age(self):
        now = datetime.now()
        if now.day == self.birthday.day and now.month == self.birthday.month:
            self.age += 1

    def update_lean_body_mass(self):
        lean_mass_percentage = 100 - self.bodyfat_percentage
        self.lean_body_mass = (lean_mass_percentage * 0.1) * self.weight

    def update_adipose_body_mass(self):
        self.adipose_body_mass = (self.bodyfat_percentage * 0.1) * self.weight