import urban_planning
import random

# Student function placeholder
"""Students define their own algorithm here."""
#Algorithm prioritizing pedestrians and animals
def ped_and_animal(option1, option2):

    ## option =(type of vehicle or non vehicle, modifer)
    ped_and_animal = urban_planning.ped_and_animals

    if option1[0] in ped_and_animal:
        if option2[0] in ped_and_animal:
            selected = random.choice([option1, option2]) #both are pedestrians and animals
            if option1 == selected:
                return selected, option2
            else:
                return selected, option1
        else:
            return option1, option2 #only option1 is emergency vehicle

    elif option2[0] in ped_and_animal:
        return option2, option1 #only option2 is emergency vehicle
    else:
        selected = random.choice([option1, option2]) #none are emergency vehicles
        if option1 == selected:
            return selected, option2
        else:
            return selected, option1
"""
if option1[0] in urban_planning.all_non_vehicles: ## Check if option 1 is a non-vehicle, if so, pick that. 
    return option1, option2
elif option2[0] in urban_planning.all_non_vehicles:  ## If option 1 is not a non-vehicle, check if option 2 is. If so, pick that. 
    return option2, option1
else:
    return option1, option2  # Default to first option if both are vehicles
"""

# Run the activity using the example algorithm
print("\n🔹 Running Example Algorithm: Always Pick Non-Vehicle 🔹")
urban_planning.run_activity(num_scenarios=25, decision_function = ped_and_animal)
