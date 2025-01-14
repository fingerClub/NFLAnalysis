# Yahoo Fantasy Football Data Processor

This program takes data scraped from the Yahoo Fantasy API and converts it into a JSON file for further analysis.

## Current Features:
- The program accesses the API in the `accessAPI.pynb` file.
- It calculates fantasy point totals for players.
- The output is written to a JSON file for review and further manipulation.
- CSVs for season stats, and player info have been extracted from the JSON.
- Some preliminary exploration has been done after storing the data on MongoBD (will be deleted).

## Future Considerations:
- **Visualizations**: In the future, the csv data will be used to create visualizations of player performance in the NFL.
- **Free Agents**: The data will also include free agents who are not currently on a team.
- **Database Integration**: It appears that dataBase integrations will be done via PostGreSQL
- **Data Collection**: Data will be collected from other sites using beautiful soup, data will be transformed to fit with Yahoo Data.

Explanation of Formatting:


## Primary Goal:
- Create an amendable database of NFL football stats that takes stats from yahoo sports and also from other sources for stat analysis.
- Make database updatable and scalable
