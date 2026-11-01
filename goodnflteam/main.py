import nflreadpy as nfl


def main():
    pbp = nfl.load_pbp()
    team_stats = nfl.load_team_stats(seasons=True)


if __name__ == "__main__":
    main()
