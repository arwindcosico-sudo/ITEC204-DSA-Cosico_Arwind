incidents = [
    ["INC1392939", "BOT-Inventory", "Failed to generate the daily report"],
    ["INC1392940", "BOT-Email", "Failed to send the scheduled notification"],
    ["INC1392941", "BOT-DataSync", "Encountered an error during data transfer"],
    ["INC1392942", "BOT-Invoice", "Failed to process an invoice"],
    ["INC1392943", "BOT-Report", "Failed to generate the weekly report"],
    ["INC1392944", "BOT-FileTransfer", "Failed to upload the required file"],
    ["INC1392945", "BOT-DataEntry", "Encountered an error while entering records"],
    ["INC1392946", "BOT-Backup", "Failed to complete the scheduled backup"],
    ["INC1392947", "BOT-Validation", "Failed to validate the submitted records"],
    ["INC1392948", "BOT-Notification", "Failed to send the system alert"]
]


def line():
    print("╚══════════════════════════════════════════════════════════════╝")


def header(title):
    print("\n╔══════════════════════════════════════════════════════════════╗")
    print(f"║{title:^62}║")
    print("╚══════════════════════════════════════════════════════════════╝")


def add_ticket():
    header("ADD INCIDENT TICKET")

    incident_id = input("Enter Incident ID: ").strip()

    if incident_id == "":
        print("\nERROR: Incident ID cannot be empty.")
        return

    for ticket in incidents:
        if ticket[0] == incident_id:
            print("\nERROR: Incident ID already exists.")
            return

    bot = input("Enter Bot: ").strip()

    if bot == "":
        print("\nERROR: Bot cannot be empty.")
        return

    description = input("Enter Short Description: ").strip()

    if description == "":
        print("\nERROR: Short Description cannot be empty.")
        return

    incidents.append([incident_id, bot, description])

    print("\n╔══════════════════════════════════════════════════════════════╗")
    print("║                TICKET ADDED SUCCESSFULLY                   ║")
    print("╚══════════════════════════════════════════════════════════════╝")


def display_tickets():
    header("ACTIVE INCIDENT TICKETS")

    if len(incidents) == 0:
        print("No active incident tickets.")
        return

    print("┌───────────────┬────────────────────┬───────────────────────────────────────┐")
    print("│ Incident ID   │ Bot                │ Short Description                      │")
    print("├───────────────┼────────────────────┼───────────────────────────────────────┤")

    for ticket in incidents:
        incident_id = ticket[0][:13]
        bot = ticket[1][:18]
        description = ticket[2][:37]

        print(f"│ {incident_id:<13} │ {bot:<18} │ {description:<37} │")

    print("└───────────────┴────────────────────┴───────────────────────────────────────┘")
    print(f"\nTotal Active Tickets: {len(incidents)}")


def search_ticket():
    header("SEARCH INCIDENT TICKET")

    incident_id = input("Enter Incident ID: ").strip()

    if incident_id == "":
        print("\nERROR: Incident ID cannot be empty.")
        return

    for ticket in incidents:
        if ticket[0] == incident_id:
            print("\n╔══════════════════════════════════════════════════════════════╗")
            print("║                     TICKET FOUND                            ║")
            print("╠══════════════════════════════════════════════════════════════╣")
            print(f"║ Incident ID : {ticket[0]:<46}║")
            print(f"║ Bot         : {ticket[1]:<46}║")
            print(f"║ Description : {ticket[2]:<46}║")
            print("╚══════════════════════════════════════════════════════════════╝")
            return

    print("\nERROR: Incident ID does not exist.")


def remove_ticket():
    header("REMOVE RESOLVED INCIDENT")

    incident_id = input("Enter Incident ID to remove: ").strip()

    if incident_id == "":
        print("\nERROR: Incident ID cannot be empty.")
        return

    for ticket in incidents:
        if ticket[0] == incident_id:
            incidents.remove(ticket)

            print("\n╔══════════════════════════════════════════════════════════════╗")
            print("║             TICKET REMOVED SUCCESSFULLY                    ║")
            print("╚══════════════════════════════════════════════════════════════╝")
            return

    print("\nERROR: Incident ID does not exist.")


def count_tickets():
    header("ACTIVE INCIDENT COUNT")

    print(f"\n              Total Active Tickets: {len(incidents)}")


while True:
    print("\n")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║              IT AUTOMATION INCIDENT MANAGER                 ║")
    print("╠══════════════════════════════════════════════════════════════╣")
    print("║  [1] Add Incident Ticket                                    ║")
    print("║  [2] Display Active Tickets                                 ║")
    print("║  [3] Search Incident Ticket                                 ║")
    print("║  [4] Remove Resolved Ticket                                 ║")
    print("║  [5] Count Active Tickets                                   ║")
    print("║  [6] Exit                                                   ║")
    print("╚══════════════════════════════════════════════════════════════╝")

    choice = input("\nEnter your choice (1-6): ").strip()

    if choice == "1":
        add_ticket()

    elif choice == "2":
        display_tickets()

    elif choice == "3":
        search_ticket()

    elif choice == "4":
        remove_ticket()

    elif choice == "5":
        count_tickets()

    elif choice == "6":
        print("\n╔══════════════════════════════════════════════════════════════╗")
        print("║              PROGRAM TERMINATED. GOODBYE!                  ║")
        print("╚══════════════════════════════════════════════════════════════╝")
        break

    else:
        print("\nERROR: Invalid choice. Please enter 1-6.")
