# ==========================================
# SMART PG MANAGEMENT SYSTEM
# Console Based Python Project
# ==========================================
import datetime
# ---------------- LOGIN DETAILS ----------------
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"
# ---------------- DATA STORAGE ----------------
residents = []
visitors = []
rooms = {
    101: None,
    102: None,
    103: None,
    104: None,
    105: None
}
# ---------------- FUNCTIONS ----------------
def login():
    print("\n========== ADMIN LOGIN ==========")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("\nLogin Successful!")
        return True
    else:
        print("\nInvalid Username or Password!")
        return False
# --------------------------------------------
def add_resident():
    print("\n========== ADD RESIDENT ==========")
    name = input("Enter Resident Name: ")
    age = input("Enter Age: ")
    phone = input("Enter Phone Number: ")
    if not(phone.isdigit() and len(phone)==10):
        print("Invalid Phone Number!")
        return
    id_proof = input("Enter ID Proof Number: ")
    print("\nRoom Sharing Types")
    print("2 Sharing --> 8000")
    print("3 Sharing --> 7000")
    print("4 Sharing --> 6000")
    sharing = input("Enter Sharing Type: ")
    if sharing == "2":
        rent = 8000
    elif sharing == "3":
        rent = 7000
    elif sharing == "4":
        rent = 6000
    else:
        print("Invalid Sharing Type!")
        return
    resident = {
        "name": name,
        "age": age,
        "phone": phone,
        "id_proof": id_proof,
        "sharing": sharing,
        "rent": rent,
        "room": None,
        "rent_paid": False,
        "join_date": str(datetime.date.today())
    }
    residents.append(resident)
    print("\nResident Added Successfully!")
# --------------------------------------------
def view_residents():
    print("\n========== RESIDENT LIST ==========")
    if len(residents) == 0:
        print("No Residents Found!")
        return
    count = 1
    for resident in residents:
        print(f"\nResident {count}")
        print("Name       :", resident["name"])
        print("Age        :", resident["age"])
        print("Phone      :", resident["phone"])
        print("ID Proof   :", resident["id_proof"])
        print("Sharing    :", resident["sharing"])
        print("Rent       :", resident["rent"])
        print("Join Date  :", resident["join_date"])
        if resident["room"] is None:
            print("Room       : Not Allocated")
        else:
            print("Room       :", resident["room"])
        if resident["rent_paid"]:
            print("Rent Status: Paid")
        else:
            print("Rent Status: Pending")
        count += 1
# --------------------------------------------
def allocate_room():
    print("\n========== ROOM ALLOCATION ==========")
    if len(residents) == 0:
        print("No Residents Available!")
        return
    name = input("Enter Resident Name: ")
    resident_found = None
    for resident in residents:
        if resident["name"].lower() == name.lower():
            resident_found = resident
            break
    if resident_found is None:
        print("Resident Not Found!")
        return
    if resident_found["room"] is not None:
        print("Room Already Allocated!")
        return
    print("\nAvailable Rooms:")
    available = False
    for room_no, occupant in rooms.items():
        if occupant is None:
            print("Room", room_no)
            available = True
    if not available:
        print("No Rooms Available!")
        return
    try:
        room_choice = int(input("Enter Room Number: "))
    except:
        print("Invalid Input!")
        return
    if room_choice not in rooms:
        print("Invalid Room Number!")
        return
    if rooms[room_choice] is not None:
        print("Room Already Occupied!")
        return
    rooms[room_choice] = resident_found["name"]
    resident_found["room"] = room_choice
    print("\nRoom Allocated Successfully!")
# --------------------------------------------
def pay_rent():
    print("\n========== RENT PAYMENT ==========")
    if len(residents) == 0:
        print("No Residents Available!")
        return
    name = input("Enter Resident Name: ")
    for resident in residents:
        if resident["name"].lower() == name.lower():
            print("Amount To Pay :", resident["rent"])
            if resident["rent_paid"]:
                print("Rent Already Paid!")
            else:
                resident["rent_paid"] = True
                print("Rent Payment Successful!")
            return
    print("Resident Not Found!")
# --------------------------------------------
def visitor_entry():
    print("\n========== VISITOR ENTRY ==========")
    visitor_name = input("Enter Visitor Name: ")
    resident_name = input("Enter Resident Name To Visit: ")
    found = False
    for resident in residents:
        if resident["name"].lower() == resident_name.lower():
            found = True
            break
    if not found:
        print("Resident Not Found!")
        return
    entry_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    visitor = {
        "visitor_name": visitor_name,
        "resident_name": resident_name,
        "entry_time": entry_time
    }
    visitors.append(visitor)
    print("\nVisitor Entry Recorded Successfully!")
# --------------------------------------------
def view_visitors():
    print("\n========== VISITOR RECORDS ==========")
    if len(visitors) == 0:
        print("No Visitor Records Found!")
        return
    count = 1
    for visitor in visitors:
        print(f"\nVisitor {count}")
        print("Visitor Name :", visitor["visitor_name"])
        print("Resident     :", visitor["resident_name"])
        print("Entry Time   :", visitor["entry_time"])
        count += 1
# --------------------------------------------
def room_status():
    print("\n========== ROOM STATUS ==========")
    total_rooms = len(rooms)
    occupied = 0
    vacant = 0
    for room_no, occupant in rooms.items():
        if occupant is None:
            status = "Vacant"
            vacant += 1
        else:
            status = "Occupied"
            occupied += 1
        print(f"Room {room_no} --> {status}")
    print("\nTotal Rooms   :", total_rooms)
    print("Occupied Rooms:", occupied)
    print("Vacant Rooms  :", vacant)
# --------------------------------------------
def search_resident():
    print("\n========== SEARCH RESIDENT ==========")
    name = input("Enter Resident Name: ")
    for resident in residents:
        if resident["name"].lower() == name.lower():
            print("\nResident Found!")
            print("Name       :", resident["name"])
            print("Age        :", resident["age"])
            print("Phone      :", resident["phone"])
            print("ID Proof   :", resident["id_proof"])
            print("Sharing    :", resident["sharing"])
            print("Rent       :", resident["rent"])
            print("Join Date  :", resident["join_date"])
            if resident["room"] is None:
                print("Room       : Not Allocated")
            else:
                print("Room       :", resident["room"])
            if resident["rent_paid"]:
                print("Rent Status: Paid")
            else:
                print("Rent Status: Pending")
            return
    print("Resident Not Found!")
# --------------------------------------------
def hostel_report():
    print("\n========== HOSTEL REPORT ==========")
    total_residents = len(residents)
    paid = 0
    pending = 0
    for resident in residents:
        if resident["rent_paid"]:
            paid += 1
        else:
            pending += 1
    print("Total Residents :", total_residents)
    print("Rent Paid       :", paid)
    print("Rent Pending    :", pending)
    print("Total Visitors  :", len(visitors))
# --------------------------------------------
def main_menu():
    while True:
        print("\n===================================")
        print(" SMART PG HOSTEL MANAGEMENT SYSTEM ")
        print("===================================")
        print("1. Add Resident")
        print("2. View Residents")
        print("3. Allocate Room")
        print("4. Pay Rent")
        print("5. Visitor Entry")
        print("6. View Visitors")
        print("7. Room Status")
        print("8. Search Resident")
        print("9. Hostel Report")
        print("10. Exit")
        choice = input("\nEnter Your Choice: ")
        if choice == "1":
            add_resident()
        elif choice == "2":
            view_residents()
        elif choice == "3":
            allocate_room()
        elif choice == "4":
            pay_rent()
        elif choice == "5":
            visitor_entry()
        elif choice == "6":
            view_visitors()
        elif choice == "7":
            room_status()
        elif choice == "8":
            search_resident()
        elif choice == "9":
            hostel_report()
        elif choice == "10":
            print("\nThank You For Using The System!")
            break
        else:
            print("\nInvalid Choice! Please Try Again.")
# ---------------- MAIN PROGRAM ----------------
print("===================================")
print("     WELCOME TO PG HOSTEL APP      ")
print("===================================")
if login():
    main_menu()
else:
    print("\nAccess Denied!")