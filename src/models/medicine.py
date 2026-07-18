from datetime import date


class Medicine:
    """
    Represents a medicine in MedGuardian AI.
    """

    def __init__(
        self,
        name,
        dosage_amount,
        dosage_unit,
        medicine_type,
        quantity,
        quantity_unit,
        start_date=None,
        end_date=None,
        meal_instruction=None,
        notes=None
    ):
        # Basic medicine information
        self.name = name
        self.dosage_amount = dosage_amount
        self.dosage_unit = dosage_unit
        self.medicine_type = medicine_type

        # Stock information
        self.quantity = quantity
        self.quantity_unit = quantity_unit

        # Treatment information
        self.start_date = start_date
        self.end_date = end_date
        self.meal_instruction = meal_instruction
        self.notes = notes


    def take_dose(self):
        """
        Reduce medicine quantity by one dose.
        """

        if self.quantity <= 0:
            return {
                "success": False,
                "message": f"{self.name} is finished."
            }

        self.quantity -= 1

        return {
            "success": True,
            "message": f"{self.name} dose taken successfully.",
            "remaining": self.quantity
        }


    def add_stock(self, amount):
        """
        Increase medicine quantity.
        """

        self.quantity += amount

        return {
            "success": True,
            "message": f"{amount} {self.quantity_unit} added.",
            "new_quantity": self.quantity
        }
    
    def is_expired(self):
    # """
    # Check if medicine treatment period has ended.
    # """

    if self.end_date is None:
        return {
            "expired": False,
            "message": "No end date provided."
        }

    if date.today() > self.end_date:
        return {
            "expired": True,
            "message": f"{self.name} treatment period ended."
        }

    return {
        "expired": False,
        "message": f"{self.name} treatment is still active."
    }

def update_details(
    self,
    name=None,
    dosage_amount=None,
    dosage_unit=None,
    medicine_type=None,
    quantity=None,
    quantity_unit=None,
    start_date=None,
    end_date=None,
    meal_instruction=None,
    notes=None
):
    """
    Update medicine information.
    """

    if name is not None:
        self.name = name

    if dosage_amount is not None:
        self.dosage_amount = dosage_amount

    if dosage_unit is not None:
        self.dosage_unit = dosage_unit

    if medicine_type is not None:
        self.medicine_type = medicine_type

    if quantity is not None:
        self.quantity = quantity

    if quantity_unit is not None:
        self.quantity_unit = quantity_unit

    if start_date is not None:
        self.start_date = start_date

    if end_date is not None:
        self.end_date = end_date

    if meal_instruction is not None:
        self.meal_instruction = meal_instruction

    if notes is not None:
        self.notes = notes

    return {
        "success": True,
        "message": "Medicine updated successfully."
    }