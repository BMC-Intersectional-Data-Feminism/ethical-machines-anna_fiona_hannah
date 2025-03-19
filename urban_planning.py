import random

# Define categories
vehicles = {
    "Emergency Vehicle": ["Ambulance", "Police vehicle"],
    "Public Transport": ["Public bus", "Light Rail"],
    "Private Vehicle": ["Human-driven car", "Self-driving car", "Ride-share vehicle", "Carpool"], 
    "Cyclist": ["Bicyclist", "Motorcyclist"]
}
non_vehicles = {
    "Pedestrian": ["Pedestrian", "Pedestrian", "Pedestrian", "Pedestrian"],
    "Animal": ["Animal"],
    "Robot": ["Autonomous delivery robot", 'Street-cleaning robot']
}

ped_and_animals = {
    "Pedestrian": ["Pedestrian", "Pedestrian", "Pedestrian", "Pedestrian"],
    "Animal": ["Animal"], 
}

vehicle_moral_factors = ["Following speed limit", "Speeding", "Wrong lane", "Heavy traffic"]
public_moral_factors = ['Running Late', 'Running on-time']
pedestrian_moral_factors = ['Elderly person', 'Child', 'Family', 'Person using wheelchair or crutches', 'Construction worker', 'Criminal fleeing scene']
animal_moral_factors = ['Pet such as a dog or cat', 'Large wild animal such as a deer', 'Small wild animal such as a squirrel or rabbit']


# Flatten category lists for easy selection
all_vehicles = [item for sublist in vehicles.values() for item in sublist]
all_non_vehicles = [item for sublist in non_vehicles.values() for item in sublist]

# Mapping for category tracking
category_mapping = {entity: category for category, entities in {**vehicles, **non_vehicles}.items() for entity in entities}

# Function to generate a random scenario
def generate_scenario():
    option1 = random.choice(all_vehicles + all_non_vehicles)
    option2 = random.choice(all_vehicles + all_non_vehicles)

    morals = ['', '']
    for i, item in enumerate([option1, option2]):
        if item in all_vehicles:
            if item in vehicles['Public Transport']:
                morals.insert(i, random.choice(public_moral_factors))
                continue
            else:
                morals.insert(i, random.choice(vehicle_moral_factors))
                continue
        elif item in all_non_vehicles:
            if item in non_vehicles['Pedestrian']:
                morals.insert(i, random.choice(pedestrian_moral_factors))
                continue
            elif item in non_vehicles['Animal']:
                morals.insert(i, random.choice(animal_moral_factors))
                continue
        
    
    return (option1, morals[0]), (option2, morals[1])

# Function to run the activity
def run_activity(num_scenarios=25, decision_function = None):
    responses = []  # Store responses

    # Track selections only when they appeared
    vehicle_counts = {category: 0 for category in vehicles.keys()}
    vehicle_appearances = {category: 0 for category in vehicles.keys()}
    
    non_vehicle_counts = {category: 0 for category in non_vehicles.keys()}
    non_vehicle_appearances = {category: 0 for category in non_vehicles.keys()}
    
    moral_counts = {moral: 0 for moral in vehicle_moral_factors + public_moral_factors + pedestrian_moral_factors + animal_moral_factors}
    moral_appearances = {moral: 0 for moral in vehicle_moral_factors + public_moral_factors + pedestrian_moral_factors + animal_moral_factors}

    print("\n🚦 AI Ethics Scenario Activity 🚦\n")
    
    if decision_function == None:
        for i in range(num_scenarios):
            choice1, choice2 = generate_scenario()
            print(f"Scenario {i+1}:")
            print(f"1. {choice1[0]} ({choice1[1]})")
            print(f"2. {choice2[0]} ({choice2[1]})")
            
            # Get valid input
            while True:
                response = input("Choose 1 or 2: ").strip()
                if response in ["1", "2"]:
                    chosen_entity, chosen_moral = (choice1 if response == "1" else choice2)
                    nonchosen_entity, nonchosen_moral = (choice1 if response == "2" else choice2)

                    # Track category appearances and selections
                    category = category_mapping[chosen_entity]
                    nonchosenCategory = category_mapping[nonchosen_entity]
                    
                    if category in vehicles:
                        vehicle_counts[category] += 1
                        vehicle_appearances[category] += 1
                    elif category in non_vehicles:
                        non_vehicle_counts[category] += 1
                        non_vehicle_appearances[category] += 1
                    
                    if nonchosenCategory in vehicles:
                        vehicle_appearances[nonchosenCategory] += 1
                    elif nonchosenCategory in non_vehicles:
                        non_vehicle_appearances[nonchosenCategory] += 1

                    
                    # Track moral factor appearances and selections
                    if chosen_moral != '':
                        moral_counts[chosen_moral] += 1
                    if choice1[1] != '':
                        moral_appearances[choice1[1]] += 1
                    if choice2[1] != '':
                        moral_appearances[choice2[1]] += 1
                    
                    responses.append(response)
                    break
                else:
                    print("Invalid choice. Please enter 1 or 2.")
    else:
        for i in range(num_scenarios):
            choice1, choice2 = generate_scenario()
            chosen_option, nonchosen_option = decision_function(choice1, choice2)
            
            print(f"Scenario {i+1}:")
            print(f"1. {choice1[0]} ({choice1[1]})")
            print(f"2. {choice2[0]} ({choice2[1]})")
            print(f"✅ Picked: {chosen_option[0]} ({chosen_option[1]})\n")

            chosen_entity, chosen_moral = chosen_option[0], chosen_option[1]
            nonchosen_entity, nonchosen_moral = nonchosen_option[0], nonchosen_option[1]

            # Track category appearances and selections
            category = category_mapping[chosen_entity]
            nonchosenCategory = category_mapping[nonchosen_entity]
                    
            if category in vehicles:
                vehicle_counts[category] += 1
                vehicle_appearances[category] += 1
            elif category in non_vehicles:
                non_vehicle_counts[category] += 1
                non_vehicle_appearances[category] += 1
            
            if nonchosenCategory in vehicles:
                vehicle_appearances[nonchosenCategory] += 1
            elif nonchosenCategory in non_vehicles:
                non_vehicle_appearances[nonchosenCategory] += 1

            
            # Track moral factor appearances and selections
            if chosen_moral != '':
                moral_counts[chosen_moral] += 1
            if choice1[1] != '':
                moral_appearances[choice1[1]] += 1
            if choice2[1] != '':
                moral_appearances[choice2[1]] += 1
            
            responses.append(chosen_option)

    # Compute results
    print("\n📊 Activity Summary 📊\n")
    
    # Display vehicle category percentages
    print("🚗 **Vehicle Prioritization**")
    for category, count in vehicle_counts.items():
        if vehicle_appearances[category] > 0:
            percentage = (count / vehicle_appearances[category]) * 100
            print(f" - {category}: {count} times ({percentage:.1f}%)")
    
    # Display non-vehicle category percentages
    print("\n🚶 **Non-Vehicle Prioritization**")
    for category, count in non_vehicle_counts.items():
        if non_vehicle_appearances[category] > 0:
            percentage = (count / non_vehicle_appearances[category]) * 100
            print(f" - {category}: {count} times ({percentage:.1f}%)")

    # Display moral factor percentages
    print("\n⚖️ **Moral Factor Prioritization**")
    for moral, count in moral_counts.items():
        if moral_appearances[moral] > 0:
            percentage = (count / moral_appearances[moral]) * 100
            print(f" - {moral}: {count} times ({percentage:.1f}%)")

