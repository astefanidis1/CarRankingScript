Car Ranking Project: Development of a Sophisticated Rating System - Expanded Summary
Project Overview and Goals
The Car Ranking Project aims to create an innovative system to accurately rank approximately 500 cars, blending subjective preferences with data-driven precision. The primary goal is to determine an exact or near-exact ranking of all cars based on personal preferences, performance characteristics, and other factors, while dynamically adjusting rankings through advanced algorithms. The system aspires to make the ranking process interactive and engaging, incorporating visuals, audio, and performance data to create a rich user experience.

Methodological Evolution
Transition to Glicko with Custom Enhancements
Why Glicko?
The transition to Glicko addressed several limitations of the initial Elo implementation:
Elo could not account for rating uncertainty or early-stage ranking volatility.
Cross-tier matchups required dynamic adjustments that Elo could not handle efficiently.
Glicko introduced Rating Deviation (RD) to measure rating confidence and adjust dynamically based on match results.
Custom Glicko Adjustments
A significant innovation in this project is the customization of the Glicko system to better align with the project's unique needs:
Dynamic RD Adjustments:
The RD (rating deviation) of cars is dynamically modified based on unexpected results.
RD decreases more quickly for cars that consistently perform as expected, reflecting higher confidence in their ratings.
RD increases for cars involved in unexpected outcomes (e.g., an underdog winning), ensuring flexibility for adjustments.
K-Factor Calibration:
A custom k-factor of 4 balances quick adjustments for misranked cars with long-term stability for well-established rankings.
Dynamic Matchup Ratios:
The 40/30/30 split was tuned to balance cross-tier, close Elo, and random matchups, enabling the discovery of misranked cars and preventing overfitting.
These enhancements ensure the system not only adjusts dynamically to evolving data but also reflects real-world variability and subjectivity in rankings.

Enhanced User Experience Goals
Beyond algorithmic improvements, the project aims to make the ranking process immersive and enjoyable by integrating additional contextual information for each car:
Visual and Audio Integration
Car Images:
During matchups, the script will display images of the two cars being compared.
This visual component allows users to engage with the cars' design and aesthetics during battles.
Audio Clips:
Incorporating audio files of engine sounds or exhaust notes adds a sensory layer to the matchups.
Users can factor auditory impressions into their preferences, making the experience more dynamic.
Performance Data:
Key specifications, such as horsepower, acceleration, and weight, will be displayed during battles.
These metrics provide an objective dimension to complement subjective preferences, helping users make informed decisions.
By combining these multimedia features, the project aims to gamify the ranking process, making it not just a calculation-driven exercise but an engaging and personal experience.

Technical Challenges and Solutions
Data Persistence and Debugging
The system faced early challenges with saving matchup results to the CSV, leading to issues like:
RD values reverting to their default (350).
Elo adjustments failing to persist between sessions.
Matchup counts resetting unexpectedly.
These issues were resolved by:
Refining the save_cars Function:
Implementing row-specific updates to ensure only matched cars are updated in the CSV.
Validating updates before and after saving to prevent data inconsistencies.
Debugging Enhancements:
Adding print statements to track Elo, RD, and matchup counts.
Conducting focused tests with controlled matchups to validate the saving process.

Current Status and Future Directions
Achievements
The project has successfully:
Transitioned from Elo to a customized Glicko system with dynamic RD adjustments.
Resolved critical data persistence issues, ensuring seamless continuity across sessions.
Validated a 40/30/30 matchup ratio, balancing cross-tier integration, precision, and exploration.
Established the foundation for integrating multimedia elements into the matchup process.
Future Development Goals
Enhanced User Experience:
Implement a system to display car images, play audio clips, and showcase performance data during matchups.
Develop an intuitive interface to make the ranking process more engaging.
Validation Mechanisms:
Introduce automated checks to ensure rankings align with subjective assessments.
Create visualizations to track ranking changes and highlight anomalies.
Scalability:
Prepare the system to handle all ten tiers while maintaining performance and ranking stability.
Ensure the database can efficiently store and retrieve large volumes of matchup data.
Gamification and Public Interaction:
Allow users to participate in matchups, contributing their own preferences to the rankings.
Share progress on public platforms to gather feedback and refine the system.

Lessons Learned
This project has underscored the importance of combining subjective judgment with mathematical rigor. Key insights include:
The need for dynamic algorithms that adapt to evolving data and preferences.
The value of robust debugging and data management practices.
The potential of integrating multimedia elements to enhance user engagement.

