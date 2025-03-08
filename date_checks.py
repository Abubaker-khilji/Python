from datetime import datetime

def input_date(prompt):
    """Function to take date input in 'DD MM YYYY' format and return as a datetime object"""
    while True:
        try:
            date_str = input(prompt + " (DD MM YYYY): ")
            return datetime.strptime(date_str, "%d %m %Y")
        except ValueError:
            print("Invalid date format. Please enter again.")

# Ask user what measures are installed
measures = []
valid_measures = ["Loft Insulation", "Internal Wall Insulation", "Cavity Wall Insulation", 
                  "External Wall Insulation", "Boiler & Heating Control"]

print("\nEnter the measures installed (type 'done' when finished):")
while True:
    measure = input("Measure Name: ").strip()
    if measure.lower() == "done":
        break
    elif measure in valid_measures:
        measures.append(measure)
    else:
        print("Invalid measure. Please enter a valid measure.")

# Get dates from user
dates = {}

dates["Survey Date"] = input_date("Enter Survey Date")

for measure in measures:
    dates[measure] = input_date(f"Enter Install Date for {measure}")

if "Boiler & Heating Control" in measures:
    dates["Boiler & Heating Control"] = input_date("Enter Install Date for Boiler & Heating Control (same date as Boiler)")

dates["Handover Date"] = input_date("Enter Handover Date")
dates["Post Reports Date"] = input_date("Enter Post Reports Date")

# Validation
errors = []

# Rule 1: Survey Date must be before all measure install dates
for measure, install_date in dates.items():
    if measure not in ["Survey Date", "Handover Date", "Post Reports Date"] and dates["Survey Date"] >= install_date:
        errors.append(f"Survey Date ({dates['Survey Date'].strftime('%d %m %Y')}) must be before {measure} Install Date ({install_date.strftime('%d %m %Y')}).")

# Rule 2: Insulation install dates can be in any order
insulation_measures = [m for m in measures if "Insulation" in m]
boiler_installed = "Boiler & Heating Control" in measures

# Rule 3: Boiler & Heating Control must have the same install date
if boiler_installed and measures.count("Boiler & Heating Control") > 1:
    errors.append("Boiler & Heating Control must have the same install date.")

# Rule 4: All Insulation must be installed before Boiler & Heating Control
if boiler_installed:
    boiler_date = dates["Boiler & Heating Control"]
    for insulation in insulation_measures:
        if dates[insulation] >= boiler_date:
            errors.append(f"{insulation} Install Date ({dates[insulation].strftime('%d %m %Y')}) must be before Boiler & Heating Control Install Date ({boiler_date.strftime('%d %m %Y')}).")

# Rule 5: Handover Date must be on or after all measure install dates and before Post Reports Date
latest_install_date = max(dates[m] for m in measures)
if dates["Handover Date"] < latest_install_date:
    errors.append(f"Handover Date ({dates['Handover Date'].strftime('%d %m %Y')}) must be on or after the latest Install Date ({latest_install_date.strftime('%d %m %Y')}).")

if dates["Handover Date"] > dates["Post Reports Date"]:
    errors.append(f"Handover Date ({dates['Handover Date'].strftime('%d %m %Y')}) must be on or before Post Reports Date ({dates['Post Reports Date'].strftime('%d %m %Y')}).")

# Output results
if errors:
    print("\n❌ Invalid Dates Found:")
    for error in errors:
        print(f" - {error}")
else:
    print("\n✅ All dates are valid!")
