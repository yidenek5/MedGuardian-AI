from src.models.medicine import Medicine


paracetamol = Medicine(
    name="Paracetamol",
    dosage_amount=500,
    dosage_unit="mg",
    medicine_type="Tablet",
    quantity=20,
    quantity_unit="tablets"
)


print(paracetamol.name)

result = paracetamol.take_dose()

print(result)

result = paracetamol.add_stock(10)

print(result)