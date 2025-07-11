import pandas as pd
from pathlib import Path
import random
import csv
import json
from datetime import datetime, timedelta


def collect_sample():
    filename = "sample.csv"
    path = Path(filename)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    df = pd.read_csv(
        path,
        sep="\t" if "\t" in open(path).read(1024) else ",",
        dtype={
            "time": str,  # Keep as string to avoid timezone issues
            "open": float,
            "high": float,
            "low": float,
            "close": float,
            "volume": float,
        },
    )

    print(f"data shape: {df.shape}, columns: {df.columns.tolist()}")


def random_multi(options, max_n=2):
    n = random.randint(1, max_n)
    return random.sample(options, n)
    # return "; ".join(random.sample(options, n))


def generate_sample(ward, num_rows=1):
    # This function is a placeholder for generating sample data.
    # In a real application, you would implement logic to create or fetch sample data.
    sexes = ["Male", "Female"]
    ethnicities = [
        "Yoruba",
        "Igbo",
        "Hausa",
    ]
    wards = [
        "Ajawa",
        "Iresi",
        "Aka",
        "Lagbedu",
        "Iwo Ate",
        # "Otamokun",
        # "Ojutaye",
        # "Idewure",
    ]
    last_bp_check = [
        # "Less than 6 months",
        "6–12 months ago",
        "Over 1 year ago",
        # "Never",
    ]
    salt_limit = [
        "Less than 1 teaspoon (5g) per day",
        "More than 2 teaspoons (10g) per day (",
        "Don't know",
    ]
    health_conditions = [
        "Hypertension (High blood pressure)",
        "Stroke",
        "Heart disease",
        "Kidney disease",
        "None of the above",
        "Don't know",
    ]
    high_salt_foods = [
        "Processed meats (e.g., sausages, bacon)",
        "Canned soups and sauces",
        "Bread and baked goods",
        "Fresh fruits and vegetables",
    ]
    frequency = ["Never", "Rarely", "Sometimes", "Often", "Always"]
    time_frequency = [
        "Daily",
        "3-4 times a week",
        "1-2 times a week",
        "Rarely",
        "Never",
    ]
    importance = ["Not important", "Somewhat important", "Very important", "Don't know"]
    barriers = [
        "Lack of knowledge about low-salt alternatives",
        "Preference for salty foods",
        "High cost of low-sodium products",
        "Availability",
        "Family or cultural preferences",
        "None",
    ]
    yes_no_activity = ["Yes", "No"]
    smoke = ["Never", "Former smoker", "Current smoker"]
    alcohol = ["Never", "Formerly do", "Currently do"]
    hypertension_status = [
        "Hypertensive (≥140/90 mmHg or on medication)",
        "Non-hypertensive",
    ]

    data = []
    for idx in range(0, num_rows):
        height = round(random.uniform(1.40, 2.10), 2)
        weight = round(random.uniform(50, 120), 1)
        bmi = round(weight / (height**2), 1)
        systolic = random.randint(90, 180)
        diastolic = random.randint(60, 120)
        waist_circumference = round(random.uniform(60, 120), 1)
        age = random.randint(18, 65)

        # Marital Status logic
        if age < 22:
            marital_status = random.choices(
                ["Single", "Married"], weights=[0.85, 0.15]
            )[0]
        elif age > 50:
            marital_status = random.choices(
                ["Married", "Divorced/Separated", "Widowed"], weights=[0.7, 0.15, 0.15]
            )[0]
        else:
            marital_status = random.choices(
                ["Single", "Married", "Divorced/Separated"], weights=[0.2, 0.7, 0.1]
            )[0]

        # Education/Occupation logic
        if age < 20:
            education_level = random.choices(
                ["Secondary", "Tertiary"], weights=[0.7, 0.3]
            )[0]
            occupation = random.choices(
                ["Student", "Unemployed", "Trader/Business"], weights=[0.7, 0.2, 0.1]
            )[0]
        elif age < 25:
            education_level = random.choices(
                ["Secondary", "Tertiary"], weights=[0.4, 0.6]
            )[0]
            occupation = random.choices(
                ["Student", "Trader/Business", "Civil Servant", "Unemployed"],
                weights=[0.5, 0.2, 0.2, 0.1],
            )[0]
        elif age > 50:
            education_level = random.choices(
                ["no formal education", "Primary", "Secondary", "Tertiary"],
                weights=[0.7, 0.2, 0.5, 0.3],
            )[0]
            occupation = random.choices(
                ["Farmer", "Trader/Business", "Civil Servant", "Unemployed"],
                weights=[0.4, 0.3, 0.2, 0.1],
            )[0]
        else:
            education_level = random.choices(
                ["Secondary", "Tertiary"], weights=[0.3, 0.7]
            )[0]
            occupation = random.choices(
                ["Trader/Business", "Civil Servant", "Unemployed", "Farmer"],
                weights=[0.4, 0.3, 0.1, 0.2],
            )[0]
        if occupation == "Student" and age > 25:
            occupation = random.choice(
                ["Trader/Business", "Civil Servant", "Unemployed", "Farmer"]
            )

        data.append(
            {
                "entry.279914237": str(age),
                "entry.1170788130": str(idx + 1),
                "entry.817048268": str(random.choice(sexes)),
                "entry.1636771902": str(marital_status),
                "entry.613220278": str(random.choice(ethnicities)),
                "entry.1351847914": str(education_level),
                "entry.437572206": str(occupation),
                "entry.561578224": str(ward),
                "entry.1230467456": str(
                    random.choice(
                        [
                            "Diabetes",
                            "Kidney disease",
                            "Obesity",
                            "Coronary heart disease",

                        ]
                    )
                ),
                "entry.642871565": str(random.choice(yes_no_activity)),
                "entry.107324300": str(random.choice(yes_no_activity)),
                "entry.1063940088": str(random.choice(last_bp_check)),
                "entry.1964941990": random.choice(salt_limit),
                "entry.1559166723": random_multi(health_conditions, 3),
                "entry.164879328": random_multi(high_salt_foods, 3),
                "entry.275698267": str(random.choice(yes_no_activity)),
                "entry.155659930": "Sometimes",
                "entry.1889485344": "1-2 times a week",
                "entry.2095272921": "Rarely",
                "entry.1682387336": "Don't know what it is",
                "entry.1614334911": "Don't know",
                "entry.963672502": "Not sure",
                "entry.1650080281": "Not sure",
                "entry.188663812": [
                    "Lack of knowledge about low-salt alternatives",
                    "High cost of low-sodium products",
                ],
                "entry.1499536321": "Yes",
                "entry.480672891": "Former smoker",
                "entry.326783893": "Currently do",
                "entry.1567036380": "No",
                "entry.203009619": "Ok!",
                "entry.1902473261": "Ok!",
                "entry.835606982": "Ok!",
                "entry.97022763": "Ok!",
                "entry.1399974781": "Ok!",
                "entry.1852434929": "Ok!",
                "entry.1217212537": "Hypertensive (≥140/90 mmHg or on medication)",
            }
        )

    print(f"Generated {len(data)} rows of sample data.")
    return data
