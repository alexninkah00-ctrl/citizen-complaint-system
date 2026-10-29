# Citizen Complaint System

A simple Python program (Object-Oriented Programming) that lets citizens report public service problems such as water, roads, electricity, health, education and waste, and lets officials track the status of each complaint.

Built for PROG211 Object-Oriented Programming 1 (Limkokwing University of Creative Technology, Sierra Leone) in the Government domain.

## How to run

1. Install Python 3.8 or newer.
2. Download complaint_system.py
3. Run: python complaint_system.py

No extra libraries are needed.

## What the program does

- Submit a new complaint
- View all complaints
- Update the status of a complaint (Pending, In Progress, Resolved)
- Load sample data for a quick demonstration

## OOP concepts used

- Classes: Citizen and Complaint
- Attributes: citizen_id, first_name, district, complaint_id, category, description, status
- Objects interacting: Citizen.submit_complaint() creates a Complaint linked to that citizen
- Instance methods: display_info(), submit_complaint(), update_status()
- Class methods (@classmethod): Citizen.get_total_citizens(), Complaint.get_valid_statuses()
- Data structure: one dictionary (complaint ID is the key, the Complaint object is the value)
- Tuples (optional): Complaint.CATEGORIES and Complaint.VALID_STATUSES

## How this solution aligns with Digital Public Goods (DPG) standards

- Open-source: The full source code is public on GitHub so anyone can read, use and improve it.
- Inclusive and accessible: Simple numbered menus, plain-language messages and clear error messages. It runs on any computer with Python and needs no special equipment.
- Privacy-respecting: The program stores only a citizen ID, a first name and a district. It does not ask for phone numbers, home addresses or national ID numbers, and it reminds users not to type them. Data is kept in memory only and is not saved to a file or sent anywhere.
- Modular and reusable: Citizen and Complaint are separate classes, and the add and display functions are separate from the menu, so they can be reused in other systems.

## Example usage (sample input and output)

=== CITIZEN COMPLAINT SYSTEM ===
1. Submit a complaint
2. View all complaints
3. Update complaint status
4. Load sample data
5. Exit
Choose an option (1-5): 4
Complaint CMP001 saved successfully.
Complaint CMP002 saved successfully.
Complaint CMP003 saved successfully.

Choose an option (1-5): 2

--- ALL COMPLAINTS ---
Complaint CMP001 | Water | Status: Pending
   Description: No running water in our street for 3 days.
   Reported by: Ama (Western Area)

Choose an option (1-5): 3
Enter complaint ID: CMP001
Allowed statuses: Pending, In Progress, Resolved
New status: In Progress
Status updated.

## Licence

Open-source. Free to use for learning.