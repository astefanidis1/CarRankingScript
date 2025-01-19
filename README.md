# Car Ranking Script

This project ranks cars based on personal preference using the Glicko ranking system. The goal is to find the exact order of favorite cars, meshing tiers and refining rankings through pairwise matchups.

## How It Works
- Cars are ranked within their tiers and across tiers using Glicko logic.
- Matchups are selected with a mix of close Elo scores, cross-tier battles, and random matchups.

## Installation & Usage
1. Clone this repo: `git clone https://github.com/astefanidis1/CarRankingScript.git`
2. Add your car data to `Car Rank Elos.csv`.
3. Run `carrank.py` to start ranking cars through pairwise matchups.

## Current Status
- Tier meshing underway.
- Addressing matchups between close Elo cars across tiers.

## Next Steps
- Improve matchup logic based on user feedback.
- Expand project to include car images or details in the rankings.

## Credits
- Glicko rating system adapted for this project.
- Script inspired by personal passion for cars and ranking systems.