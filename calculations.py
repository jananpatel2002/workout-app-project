def calculate_protein_intake(weight):
    """Takes the weight and calculates the amount of protein
    that the person needs to intake in order to stay healthy"""

    lower_limit = weight * 0.8

    print(f"You should consume around {lower_limit} - {weight} grams of protein daily")


# 0.8 x body weight, 1.0 x body weight;
class Calculations:
    def __init__(self, weight):
        self.weight = weight
        calculate_protein_intake(self.weight)
