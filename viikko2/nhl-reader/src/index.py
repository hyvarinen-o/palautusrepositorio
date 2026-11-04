from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.console import Console
from rich.table import Table

def main():
    countries = "USA/FIN/CAN/SWE/CZE/RUS/SLO/FRA/GBR/SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS"
    country_list = [str(i) for i in countries.split("/")]
    while True:
        console = Console()
        table = Table(border_style="white")
        
        table.add_column("Name", style="blue", no_wrap=True)
        table.add_column("Team", style="magenta")
        table.add_column("Goals", style="green", justify="right")
        table.add_column("Assists", style="green", justify="right")
        table.add_column("Points", style="green", justify="right")

        url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"

        reader = PlayerReader(url)
        stats = PlayerStats(reader)

        print(f"search Season 2024-25 (type {"quit"} to quit)")
        nationality = str(input("Nationality [{countries}]: "))

        if nationality.lower() == "quit":
            print("goodbye")
            break
        elif nationality not in country_list:
            print("Invalid nationality")
            continue
        elif nationality in country_list:
            players = stats.top_scorers_by_nationality(nationality)
            for p in players:
                table.add_row(
                p.name,
                p.team,
                str(p.goals),
                str(p.assists),
                str(p.points))
            console.print(table)

if __name__ == "__main__":
    main()