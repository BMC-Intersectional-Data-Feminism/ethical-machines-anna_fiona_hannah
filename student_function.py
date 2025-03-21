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
        
# Run the activity using the example algorithm
print("\n🔹 Running Example Algorithm: Always Pick Pedestrian and Animals🔹")
urban_planning.run_activity(num_scenarios=25, decision_function = ped_and_animal)
