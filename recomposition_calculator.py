class RecompositionCalculator:
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

    def calculate_bmr(self, height, weight, age, gender):
        # calculates BMR based on the Mifflin St. Jeor formula
        bmr = 10 * weight + 6.25 * height - 5 * age
        if gender[0].upper() == 'M':
            bmr += 5
        elif gender[0].upper() == 'F':
            bmr -= 161
        else:
            pass
            # todo: throw custom error
        return bmr


if __name__ == '__main__':
    # todo: delete later, for testing purposes only
    calc = RecompositionCalculator()
    height = calc.convert_inches_to_cm(calc.fpi_to_inches(6, 0))
    weight = calc.convert_to_kg(183)
    age = 26
    gender = 'M'
    bmr = calc.calculate_bmr(height, weight, age, gender)
    print(bmr)