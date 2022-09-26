# Initialize function to display a random fact about prime numbers
def randomFact():
    # Load facts from file
    with open("facts.txt", "r") as f:
        facts = f.readlines()
    
    # Pick a random fact
    import random
    fact = random.choice(facts)
    
    return fact
