import pandas as pd

# Public Google Sheet URL
sheet_url = "https://docs.google.com/spreadsheets/d/1Gx0MCPiUT_-VwtLQHaqzqK3aQiCe9H1BbDMrenTYcCU/edit#gid=34216304"

# Convert it to the CSV export link
csv_url = sheet_url.replace("/edit#gid=", "/export?format=csv&gid=")

# Read the data into a pandas DataFrame
df = pd.read_csv(csv_url)

# Extract the player names (assuming 'Player' is the column name)
player_names = df["Player"].tolist()

# Save the player names to a text file
with open("hockey_players.txt", "w") as file:
    for name in player_names:
        file.write(name + "\n")

print("Player names saved to hockey_players.txt")
