def likelihood():
    likelihoods = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
    return likelihoods

def run():
    chance = likelihood()
    
    print(f"The minimum chance of falling is:{chance}%")

run()