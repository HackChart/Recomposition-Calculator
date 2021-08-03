from user import User

class RecompositionCalculator:
    # --- HELPER METHODS --- #
    def convert_to_kg(self, weight_in_pounds: float):
        """Takes a weight in pounds and returns kg conversion"""
        return weight_in_pounds / 2.2046

    def convert_to_pounds(self, weight_in_kg: float):
        return weight_in_kg * 2.2046

    def fpi_to_inches(self, feet: int, inches: float):
        """Converts feet plus inches to inches"""
        return (feet * 12) + inches

    def convert_inches_to_cm(self, inches: float):
        return inches * 2.54

    def convert_cm_to_inches(self, centimeters: float):
        return centimeters / 2.54

    # --- CALCULATIONS --- #
    # TODO: retool calc_bmr to use User instead of individual stats
    def calculate_bmr(self, height, weight, age, gender):
        # calculates BMR based on the Mifflin St. Jeor formula
        bmr = 10 * weight + 6.25 * height - 5 * age
        if gender[0].upper() == 'M':
            bmr += 5
        elif gender[0].upper() == 'F':
            bmr -= 161
        else:
            bmr = weight * 10
            print('For the purpose of the Mifflin St. Jeor formula, only binary Male/Female genders are permitted.'
                  'An approximate BMR has been calculated using the standard weight x 10 method, be aware that results '
                  'may be slightly less accurate.')
        # TODO: round bmr to closest int
        return bmr

    def calculate_TDEE(self, user: User):
        # TODO: calculate TDEE based on activity factor
        # TODO: auto adjust activity factor depending on primary goal
        pass

    def calculate_daily_energy_intake(self):
        # TODO: determine total n of cals to consume based on bf % and primary goal
        # TODO: double check to make sure both are congruent
        pass

    # TODO: make sure to keep flexible for use with multiple TDEE's
    def calculate_macros(self):
        # TODO: package for individual macro methods
        pass

    def calculate_protein(self):
        # TODO: calculate protein macro
        pass

    def calculate_carbs(self):
        # TODO: calculate carb macro
        pass

    def calculate_lipids(self):
        # TODO: calc lipid macro
        pass

if __name__ == '__main__':
    # todo: delete later, for testing purposes only
    calc = RecompositionCalculator()
    height = calc.convert_inches_to_cm(calc.fpi_to_inches(6, 0))
    weight = calc.convert_to_kg(183)
    age = 26
    gender = 'M'
    bmr = calc.calculate_bmr(height, weight, age, gender)
    print(bmr)