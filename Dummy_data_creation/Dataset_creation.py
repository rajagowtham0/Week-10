from bson import ObjectId
import json
import random

data = []

# ACNE (33)
for i in range(1, 34):
    data.append({
        "_id": {"$oid": str(ObjectId())},
        "case_id": f"ACNE_{i:03}",
        "clinic_id": "CLINIC_001",
        "symptoms": f"acne lesions with oily skin variation {i}",
        "duration_days": 50 + i,
        "doctor_notes": f"moderate inflammatory acne stage {i%3}",
        "diagnosis": "Acne Vulgaris",
        "treatment": random.choice([
            "Topical retinoid + benzoyl peroxide",
            "Oral antibiotics",
            "Salicylic acid"
        ]),
        "outcome": "Improved",
        "recovery_days": 30 + i,
        "patient": {
            "age": 20 + (i % 10),
            "gender": "Female" if i % 2 == 0 else "Male"
        }
    })

# PIGMENTATION (33)
for i in range(1, 34):
    data.append({
        "_id": {"$oid": str(ObjectId())},
        "case_id": f"PIG_{i:03}",
        "clinic_id": "CLINIC_001",
        "symptoms": f"dark pigmentation patches variation {i}",
        "duration_days": 80 + i,
        "doctor_notes": f"melasma pigmentation level {i%3}",
        "diagnosis": "Melasma",
        "treatment": random.choice([
            "Chemical peel + sunscreen",
            "Laser therapy",
            "Hydroquinone cream"
        ]),
        "outcome": "Partially Improved",
        "recovery_days": 60 + i,
        "patient": {
            "age": 25 + (i % 15),
            "gender": "Female" if i % 2 == 0 else "Male"
        }
    })

# HAIR LOSS (34)
for i in range(1, 35):
    data.append({
        "_id": {"$oid": str(ObjectId())},
        "case_id": f"HAIR_{i:03}",
        "clinic_id": "CLINIC_001",
        "symptoms": f"hair thinning and shedding variation {i}",
        "duration_days": 100 + i,
        "doctor_notes": f"telogen effluvium stage {i%3}",
        "diagnosis": "Telogen Effluvium",
        "treatment": random.choice([
            "PRP therapy",
            "Minoxidil",
            "Finasteride"
        ]),
        "outcome": "Improved",
        "recovery_days": 70 + i,
        "patient": {
            "age": 22 + (i % 20),
            "gender": "Male" if i % 2 == 0 else "Female"
        }
    })

with open("mongo_insert.json", "w") as f:
    json.dump(data, f, indent=2)

print("File generated: mongo_insert.json")