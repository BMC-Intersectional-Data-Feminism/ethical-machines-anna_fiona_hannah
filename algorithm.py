import urban_planning 

# Example algorithm: Always picks the non-vehicle option
def always_pick_non_vehicle(option1, option2):
    """This algorithm always picks the non-vehicle if possible.
    It will return first the picked option and second the non-chosen option. """
    
    if option1[0] in urban_planning.all_non_vehicles: ## Check if option 1 is a non-vehicle, if so, pick that. 
        return option1, option2
    elif option2[0] in urban_planning.all_non_vehicles:  ## If option 1 is not a non-vehicle, check if option 2 is. If so, pick that. 
        return option2, option1
    else:
        return option1, option2  # Default to first option if both are vehicles

# Student function placeholder
def student_algorithm(option1, option2):
    """Students define their own algorithm here."""
    print('Write your own algorithm here!')

# Function to run the simulation using a given algorithm
# Run the activity
# urban_planning.run_activity()

# Run the activity using the example algorithm
print("\n🔹 Running Example Algorithm: Always Pick Non-Vehicle 🔹")
urban_planning.run_activity(num_scenarios=25, decision_function = always_pick_non_vehicle)

#print("\n🔹 Now it's your turn! Modify 'student_algorithm' and run again. 🔹")

#In class code example
# example 1: always pick emergency vehicles first
def pick_emergency_vehicle(option1, option2):
    """ This algorithm always picks the emergency vehicle first"""

    ## option =(type of vehicle or non cehivle, modifer)
    possible_emergency_vehicle = urban_planning.vehicles("emegency vehicles")

    if option1[0] in possible_emergency_vehicle:
        if option2[0] in possible_emergency_vehicle:
            selected = random.choice([option1, option2]) #both are emergency vehicles
            if option1 == selected:
                return selected, option2
            else:
                return selected, option1
        else:
            return option1, option2 #only option1 is emergency vehicle
    elif option2[0] in possible_emergency_vehicle:
        return option2, option1 #only option2 is emergency vehicle
    else:
        selected = random.choice([option1, option2]) #none are emergency vehicles
        if option1 == selected:
            return selected, option2
        else:
            return selected, option1
