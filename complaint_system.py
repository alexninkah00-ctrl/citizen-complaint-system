"""
Citizen Complaint System
PROG211 Object-Oriented Programming 1 - Individual Assignment

A simple, open-source tool that lets citizens report public service
problems (water, roads, electricity...) and lets officials track them.

Digital Public Goods (DPG) notes:
- No sensitive personal data is stored (only an ID, first name, district).
- Plain-language menus and messages for easy use by everyone.
- Classes are separate and reusable in other projects.
"""


class Citizen:
    """A citizen who submits complaints. Stores NO sensitive data."""

    # Class attribute: shared by all Citizen objects
    total_citizens = 0

    def __init__(self, citizen_id, first_name, district):
        self.citizen_id = citizen_id
        self.first_name = first_name
        self.district = district
        Citizen.total_citizens += 1

    # Instance method: works on one specific citizen
    def display_info(self):
        print(f"Citizen ID: {self.citizen_id} | Name: {self.first_name} "
              f"| District: {self.district}")

    # Instance method: shows how two objects interact
    def submit_complaint(self, complaint_id, category, description):
        """Create a Complaint object that belongs to this citizen."""
        return Complaint(complaint_id, category, description, self)

    # Class method: works on the whole class, not one object
    @classmethod
    def get_total_citizens(cls):
        return cls.total_citizens


class Complaint:
    """A single complaint about a public service."""

    # Tuples: fixed lists that should never change
    CATEGORIES = ("Water", "Roads", "Electricity", "Health", "Education",
                  "Waste")
    VALID_STATUSES = ("Pending", "In Progress", "Resolved")

    def __init__(self, complaint_id, category, description, citizen):
        self.complaint_id = complaint_id
        self.category = category
        self.description = description
        self.citizen = citizen          # link to a Citizen object
        self.status = "Pending"         # every complaint starts as Pending

    # Instance method: change the status of this complaint
    def update_status(self, new_status):
        if new_status in Complaint.VALID_STATUSES:
            self.status = new_status
            return True
        return False

    # Instance method: show this complaint
    def display_info(self):
        print(f"Complaint {self.complaint_id} | {self.category} | "
              f"Status: {self.status}")
        print(f"   Description: {self.description}")
        print(f"   Reported by: {self.citizen.first_name} "
              f"({self.citizen.district})")

    # Class method: returns the allowed statuses
    @classmethod
    def get_valid_statuses(cls):
        return cls.VALID_STATUSES


# ---------------------------------------------------------------------
# Data structure: ONE dictionary. Key = complaint ID, value = Complaint
# ---------------------------------------------------------------------
def add_complaint(records, complaint):
    """Add a Complaint object to the dictionary."""
    if complaint.complaint_id in records:
        print("That complaint ID already exists. Please use a new one.")
        return False
    records[complaint.complaint_id] = complaint
    print(f"Complaint {complaint.complaint_id} saved successfully.")
    return True


def display_all_complaints(records):
    """Loop through the dictionary and display every complaint."""
    if not records:
        print("No complaints recorded yet.")
        return
    print("\n--- ALL COMPLAINTS ---")
    for complaint in records.values():
        complaint.display_info()
        print()


# ---------------------------------------------------------------------
# Menu helpers
# ---------------------------------------------------------------------
def load_sample_data(records):
    """Create sample citizens and complaints to demonstrate the system."""
    ama = Citizen("C001", "Ama", "Western Area")
    musa = Citizen("C002", "Musa", "Bo")

    add_complaint(records, ama.submit_complaint(
        "CMP001", "Water", "No running water in our street for 3 days."))
    add_complaint(records, musa.submit_complaint(
        "CMP002", "Roads", "Large pothole near the market junction."))
    add_complaint(records, ama.submit_complaint(
        "CMP003", "Electricity", "Street light has not worked for a week."))


def submit_new_complaint(records):
    print("\nPrivacy tip: do NOT type phone numbers or home addresses.")
    citizen_id = input("Your citizen ID (e.g. C010): ").strip()
    first_name = input("Your first name: ").strip()
    district = input("Your district: ").strip()

    print("Categories:", ", ".join(Complaint.CATEGORIES))
    category = input("Choose a category: ").strip().capitalize()
    if category not in Complaint.CATEGORIES:
        print("Invalid category. Complaint not saved.")
        return

    description = input("Describe the problem briefly: ").strip()
    complaint_id = input("New complaint ID (e.g. CMP010): ").strip().upper()

    citizen = Citizen(citizen_id, first_name, district)
    add_complaint(records, citizen.submit_complaint(
        complaint_id, category, description))


def change_status(records):
    complaint_id = input("Enter complaint ID: ").strip().upper()
    complaint = records.get(complaint_id)
    if complaint is None:
        print("Complaint not found.")
        return
    print("Allowed statuses:", ", ".join(Complaint.get_valid_statuses()))
    new_status = input("New status: ").strip().title()
    if complaint.update_status(new_status):
        print("Status updated.")
    else:
        print("Invalid status. Nothing changed.")


def main():
    records = {}   # the one data structure (dictionary)
    while True:
        print("\n=== CITIZEN COMPLAINT SYSTEM ===")
        print("1. Submit a complaint")
        print("2. View all complaints")
        print("3. Update complaint status")
        print("4. Load sample data")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            submit_new_complaint(records)
        elif choice == "2":
            display_all_complaints(records)
        elif choice == "3":
            change_status(records)
        elif choice == "4":
            load_sample_data(records)
        elif choice == "5":
            print(f"Citizens registered this session: "
                  f"{Citizen.get_total_citizens()}")
            print("Thank you. Goodbye!")
            break
        else:
            print("Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()