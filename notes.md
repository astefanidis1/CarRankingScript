# Project Notes

## Development Timeline
- **Jan 2025**: Added Glicko ranking system for pairwise matchups.
- **Jan 19, 2025**: Implemented tier meshing and debugging tools.
- **Jan 20, 2025**: Finalized dynamic RD adjustments and matchup logic.

## Challenges and Solutions
### Data Persistence Issues
**Challenge**: Matchup results weren't being saved properly.
**Solution**:
- Debugging with print statements.
- Refining the `save_cars` function to ensure row-specific updates.

### Elo Inflation in Early Matchups
**Challenge**: Early matchups caused extreme Elo score inflation.
**Solution**:
- Transitioned to Glicko with custom RD adjustments.
- Tuned parameters for balanced rating adjustments.

## Ideas and Future Goals
- Add car images, audio clips, and performance data for matchups.
- Develop a web-based interface for better usability.
- Incorporate public voting for additional feedback.
