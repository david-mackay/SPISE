import random

outcomes = ['H', 'T']

num_trials = 1000
desired_outcome = 'H'

def simulation(num_trials, outcomes, desired_outcome):
    last = None
    current = None
    counter = 0
    for i in range(num_trials):
        if i ==0:
            last = random.choice(outcomes)
            continue

        current = random.choice(outcomes)
        if last == 'H' and current == 'T':
            counter +=1
        last = current

            
    return(counter/num_trials)
    

print(simulation(num_trials, outcomes, desired_outcome))






























