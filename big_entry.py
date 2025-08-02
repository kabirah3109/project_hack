import random
from datetime import datetime


def fill_random_value(
    type_id, entry_id, options, required=False, entry_name="", idx=None, village=None
):
    """Fill random value for a form entry
    Customize your own fill_algorithm here
    Note: please follow this func signature to use as fill_algorithm in form.get_form_submit_request
    """
    height = round(random.uniform(1.40, 2.10), 2)
    weight = round(random.uniform(50, 120), 1)
    bmi = round(weight / (height**2), 1)
    systolic = random.randint(90, 180)
    diastolic = random.randint(60, 120)
    waist_circumference = round(random.uniform(60, 120), 1)
    age = random.randint(25, 65)
    # Logical Algorithm
    if age <= 24:
        marital_status = "Single"
    elif age >= 25 and age < 50:
        marital_status = "Married"
    elif age > 50:
        marital_status = random.choices(
            ["Married", "Divorced/Separated", "Widowed"],
            weights=[0.7, 0.15, 0.15],
        )[0]
    else:
        marital_status = random.choices(
            ["Single", "Married", "Divorced/Separated"], weights=[0.2, 0.7, 0.1]
        )[0]

    # Education/Occupation logic
    if age < 20:
        education_level = random.choices(["Secondary", "Tertiary"], weights=[0.7, 0.3])[
            0
        ]
        occupation = random.choices(
            ["Student", "Unemployed", "Trader/Business"],
            weights=[0.7, 0.2, 0.1],
        )[0]
    elif age < 25:
        education_level = random.choices(["Secondary", "Tertiary"], weights=[0.4, 0.6])[
            0
        ]
        occupation = random.choices(
            ["Student", "Trader/Business", "Civil Servant", "Unemployed"],
            weights=[0.5, 0.1, 0.1, 0.3],
        )[0]
    elif age > 50:
        education_level = random.choices(
            ["No formal education", "Primary", "Secondary", "Tertiary"],
            weights=[0.7, 0.2, 0.5, 0.3],
        )[0]
        occupation = random.choices(
            ["Farmer", "Trader/Business", "Civil Servant", "Unemployed"],
            weights=[0.4, 0.4, 0.1, 0.1],
        )[0]
    else:
        education_level = random.choices(["Secondary", "Tertiary"], weights=[0.3, 0.7])[
            0
        ]
        occupation = random.choices(
            ["Trader/Business", "Civil Servant", "Unemployed", "Farmer"],
            weights=[0.4, 0.3, 0.1, 0.2],
        )[0]
    if occupation == "Student" and age > 25:
        occupation = random.choice(
            ["Trader/Business", "Civil Servant", "Unemployed", "Farmer"]
        )

    entry_id = str(entry_id)  # Ensure entry_id is a string for consistency
    # Customize for specific entry_id
    if entry_id == "279914237":
        return age
    if entry_id == "561578224":
        return village
    if entry_id == "1170788130" and idx is not None:
        return idx
    if entry_id == "1636771902":
        return marital_status
    if entry_id == "1351847914":
        return education_level
    if entry_id == "437572206":
        return occupation
    if entry_id == "203009619":
        return height
    if entry_id == "1902473261":
        return weight
    if entry_id == "835606982":
        return bmi
    if entry_id == "97022763":
        return waist_circumference
    if entry_id == "1399974781":
        return systolic
    if entry_id == "1852434929":
        return diastolic
    if entry_id == "emailAddress":
        return "your_email@gmail.com"
    if entry_name == "Short answer":
        return "Random answer!"
    # Random value for each type
    if type_id in [0, 1]:  # Short answer and Paragraph
        return "" if not required else "Ok!"
    if type_id == 2:  # Multiple choice
        return random.choice(options)
    if type_id == 3:  # Dropdown
        return random.choice(options)
    if type_id == 4:  # Checkboxes
        return random.sample(options, k=random.randint(1, len(options)))
    if type_id == 5:  # Linear scale
        return random.choice(options)
    if type_id == 7:  # Grid choice
        return random.choice(options)
    if type_id == 9:  # Date
        return datetime.date.today().strftime("%Y-%m-%d")
    if type_id == 10:  # Time
        return datetime.datetime.now().strftime("%H:%M")
    return ""


def setup(age):
    # age = 12
    # Logical Algorithm
    if age < 24:
        marital_status = "Single"
    elif age > 25 and age < 50:
        marital_status = "Married"
    elif age > 50:
        marital_status = random.choices(
            ["Married", "Divorced/Separated", "Widowed"],
            weights=[0.7, 0.15, 0.15],
        )[0]
    else:
        marital_status = random.choices(
            ["Single", "Married", "Divorced/Separated"], weights=[0.2, 0.7, 0.1]
        )[0]

    # Education/Occupation logic
    if age < 20:
        education_level = random.choices(["Secondary", "Tertiary"], weights=[0.7, 0.3])[
            0
        ]
        occupation = random.choices(
            ["Student", "Unemployed", "Trader/Business"],
            weights=[0.7, 0.2, 0.1],
        )[0]
    elif age < 25:
        education_level = random.choices(["Secondary", "Tertiary"], weights=[0.4, 0.6])[
            0
        ]
        occupation = random.choices(
            ["Student", "Trader/Business", "Civil Servant", "Unemployed"],
            weights=[0.5, 0.1, 0.1, 0.3],
        )[0]
    elif age > 50:
        education_level = random.choices(
            ["No formal education", "Primary", "Secondary", "Tertiary"],
            weights=[0.7, 0.2, 0.5, 0.3],
        )[0]
        occupation = random.choices(
            ["Farmer", "Trader/Business", "Civil Servant", "Unemployed"],
            weights=[0.4, 0.4, 0.1, 0.1],
        )[0]
    else:
        education_level = random.choices(["Secondary", "Tertiary"], weights=[0.3, 0.7])[
            0
        ]
        occupation = random.choices(
            ["Trader/Business", "Civil Servant", "Unemployed", "Farmer"],
            weights=[0.4, 0.3, 0.1, 0.2],
        )[0]
    if occupation == "Student" and age > 25:
        occupation = random.choice(
            ["Trader/Business", "Civil Servant", "Unemployed", "Farmer"]
        )
    return {
        "age": age,
        "marital_status": marital_status,
        "education_level": education_level,
        "occupation": occupation,
    }
        
# if __name__ == "__main__":
#     # Example usage
#     print("Setup complete for age:", setup(21))