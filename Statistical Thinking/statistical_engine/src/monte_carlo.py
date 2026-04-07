import random
# for crash probability
def simulate_crashes(days):
    crash_probability = 0.045
    crashes = 0

    for _ in range(days):
        if random.random() < crash_probability:
            crashes +=1 
    return crashes / days

#for diplaying the results of the simulation
def run_simulations():
    for days in [10,100,10000]:
        prob = simulate_crashes(days)
        print(f"Days: {days}, Simulated Crash Probability: {prob}")

