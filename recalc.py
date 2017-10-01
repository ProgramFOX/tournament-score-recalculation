import time
import requests
import bs4
from game import Game
from tournamentpoints import TournamentPoints

tournament_url = input("Enter tournament URL here: ")
tournament_id = tournament_url.rstrip("/").split("/")[-1]

tournament_page_1 = requests.get("https://lichess.org/api/tournament/" + tournament_id + "?page=1").json()
time.sleep(1)
tournament_page_2 = requests.get("https://lichess.org/api/tournament/" + tournament_id + "?page=2").json()

player_names = []
for ranking in tournament_page_1["standing"]["players"]:
    player_names.append(ranking["name"])
for ranking in tournament_page_2["standing"]["players"]:
    if ranking["rank"] <= 15:
        player_names.append(ranking["name"])

new_standings = []

for player in player_names:
    page = 1
    games = []
    users_to_check = []
    non_selected_games = -1
    while True:
        adv_search = bs4.BeautifulSoup(requests.get("https://lichess.org/@/{}/search?source=5&page={}".format(player, page)).text, "html.parser")
        found_games = adv_search.find_all("div", { "class": "game_row" })
        must_break = False
        if len(found_games) == 0:
            break
        for g in found_games:
            this_tourn_id = g.find("div", { "class": "header" }).find("a", { "class": "text" })["href"].split("/")[-1]
            if this_tourn_id == tournament_id:
                non_selected_games = 0
                result = g.find("div", { "class": "result" }).find("span")["class"][0]
                if result == "up":
                    num_res = 1
                elif result == "down":
                    num_res = 0
                else:
                    num_res = 0.5
                white = g.find("div", { "class": "player white" }).find("a", { "class": "user_link" }).find(text=True).lower()
                white_berserk = len(g.find("div", { "class": "player white" }).find_all("span", { "data-icon": "`" })) > 0
                black = g.find("div", { "class": "player black" }).find("a", { "class": "user_link" }).find(text=True).lower()
                black_berserk = len(g.find("div", { "class": "player black" }).find_all("span", { "data-icon": "`" })) > 0
                if player.lower() == white:
                    opponent = black
                    player_berserk = white_berserk
                else:
                    opponent = white
                    player_berserk = black_berserk
                if player_berserk:
                    berserk_int = 1
                else:
                    berserk_int = 0
                users_to_check.append(opponent)
                games.append(Game(num_res, opponent, berserk_int))
            else:
                if non_selected_games != -1:
                    non_selected_games += 1
                    if non_selected_games > 2:
                        must_break = True
                        break
        if must_break:
            break
        page += 1
    users_to_check = list(set(users_to_check))
    cheaters = []
    time.sleep(1)
    fetched_checked_users = requests.post("https://lichess.org/api/users", data=",".join(users_to_check)).json()
    for u in fetched_checked_users:
        if "engine" in u and u["engine"] is True:
            cheaters.append(u["username"].lower())
    filtered_games = [x for x in games if x.result != 0 or (x.result == 0 and x.opponent not in cheaters)]
    filtered_games.reverse()
    points = TournamentPoints(player.lower())
    for g in filtered_games:
        if g.result == 1:
            points.add_win(g.berserk)
        elif g.result == 0.5:
            points.add_draw()
        else:
            points.add_loss()
    new_standings.append(points)
    print("{} - {} points - {}".format(player, points.sum(), "".join([str(x) for x in points.points])))

print("---------------------")
new_standings.sort(key=lambda x: x.sum(), reverse=True)
i = 1
for ns in new_standings:
    print("{}. {} - {}".format(i, ns.player, ns.sum()))
    i += 1
