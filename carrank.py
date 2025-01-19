
import random
import pandas as pd
import math

# Load car data from CSV file
def load_cars(filename="Car Rank Elos.csv", tiers=["T10 (Cooler than a pedestrian car)", "T9 (Kinda cool, why not?)"]):
    df = pd.read_csv(filename)
    tier_cars = {}
    matchup_tracker = {}
    rd_tracker = {}
    for tier in tiers:
        tier_cars[tier] = df[df['Tier'] == tier].set_index('Car')['Elo'].to_dict()
        matchup_tracker[tier] = df[df['Tier'] == tier].set_index('Car')['Matchups'].to_dict()
        rd_tracker[tier] = df[df['Tier'] == tier].set_index('Car')['RD'].to_dict()
    return df, tier_cars, matchup_tracker, rd_tracker

# Save updated Glicko scores, RD, and matchups to CSV
def save_cars(df, all_cars, all_rd, car1, car2, filename="Car Rank Elos.csv"):
    # Update only the rows for the two cars involved in the matchup
    updated_cars = [car1, car2]
    for car in updated_cars:
        # Update Elo
        df.loc[df['Car'] == car, 'Elo'] = all_cars[car]
        # Update RD
        df.loc[df['Car'] == car, 'RD'] = all_rd[car]

    # Save the DataFrame to the CSV file
    df.to_csv(filename, index=False)
    print(f"Saved updates to {filename}")

# Glicko functions
def g(phi):
    return 1 / math.sqrt(1 + 3 * (phi ** 2) / (math.pi ** 2))

def expected_score_glicko(r1, r2, phi2):
    g_phi2 = g(phi2)
    return 1 / (1 + math.exp(-g_phi2 * (r1 - r2) / 400))

def update_glicko(r1, r2, phi1, phi2, result, k=4, tau=0.5):
    g_phi2 = g(phi2)
    e = expected_score_glicko(r1, r2, phi2)
    d2 = 1 / ((g_phi2 ** 2) * e * (1 - e))
    delta = g_phi2 * (result - e)
    new_phi1 = math.sqrt(1 / (1 / (phi1 ** 2) + 1 / d2))
    new_phi1 += k * abs(result - e)  # Adjust RD dynamically
    new_r1 = r1 + (delta / (1 / (phi1 ** 2) + 1 / d2)) * 400 / math.log(10)
    return new_r1, new_phi1

# Load cars and matchup tracker
filename = "Car Rank Elos.csv"
tiers = ["T10 (Cooler than a pedestrian car)", "T9 (Kinda cool, why not?)"]
df, tier_cars, matchup_tracker, rd_tracker = load_cars(filename, tiers)

# Combine all cars for matchups
all_cars = {car: tier_cars[tier][car] for tier in tiers for car in tier_cars[tier]}
all_rd = {car: rd_tracker[tier][car] for tier in tiers for car in rd_tracker[tier]}

# Matchup selection logic
car1 = random.choice(list(all_cars.keys()))  # Randomly select the first car

# Determine second car based on matchup ratio logic
random_choice = random.random()
if random_choice < 0.4:  # 40% Cross-Tier Matchups
    car2 = random.choice(list(all_cars.keys()))
elif random_choice < 0.7:  # 30% Close Elo Matchups
    potential_opponents = [
        car for car in all_cars.keys()
        if car != car1 and abs(all_cars[car] - all_cars[car1]) <= 50
    ]
    car2 = random.choice(potential_opponents) if potential_opponents else random.choice([car for car in all_cars.keys() if car != car1])
else:  # 30% Random Matchups
    car2 = random.choice([car for car in all_cars.keys() if car != car1])

# Display the matchup
print(f"1: {car1} (RD: {all_rd[car1]:.2f})")
print(f"2: {car2} (RD: {all_rd[car2]:.2f})")
choice = input("Enter winner (1, 2, or T for tie): ").strip().upper()

# Process the match result
if choice == "1":
    result = 1
elif choice == "2":
    result = 0
elif choice == "T":
    result = 0.5
else:
    print("Invalid input. Please enter 1, 2, or T.")
    result = None

if result is not None:
    all_cars[car1], all_rd[car1] = update_glicko(all_cars[car1], all_cars[car2], all_rd[car1], all_rd[car2], result)
    all_cars[car2], all_rd[car2] = update_glicko(all_cars[car2], all_cars[car1], all_rd[car2], all_rd[car1], 1 - result)

    # Save progress back to the spreadsheet
    save_cars(df, all_cars, all_rd, car1, car2, filename)

    # Confirmation message
    print("Matchup processed and Glicko scores updated.")