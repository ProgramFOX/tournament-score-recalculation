# What is this?

This tool is built to re-calculate the tournament standings of the top 15 of a Lichess tournament.

It has this effect:

* If a streak got broken due to a cheater that got banned later, the re-calculation will restore this streak.
* A game that finished after the tournament clock does hit zero, does get counted.

This tool is built for the purpose of the FV Variants World Cup, where these points are more important than in any regular Lichess tournament. You can use this tool if you run a similar tournament.

# How to run it?

You need to have Python **3** installed. After the tournament finished, _and_ the top 15 finished their running games, run the tool like this:

```
python3 recalc.py
```
(or `python` if that refers to Python 3)

... and it will prompt for a tournament URL.

# Also important to know

If you use this tool, it's on your own responsibility.

# Sample output

First, it will go through the top 15 one-by-one and calculate the new score. When that's done, it will output the new standings:

```
Enter tournament URL here: https://lichess.org/tournament/6MRjAkgv
puressence - 66 points - 3355555503345555
Belerfon - 31 points - 2245400202244
Kielileike - 23 points - 23550224
Vempele - 24 points - 02244444
antisuicide - 18 points - 22002244002
chessfriendship - 16 points - 202022400220
Tal_fanclub - 16 points - 224402200
ishak37 - 10 points - 224020
dampooo - 10 points - 20220022
chessking2151 - 9 points - 234
googa - 10 points - 2202202
Calanthe - 8 points - 22022
godo1 - 8 points - 02240
wanyonyi - 8 points - 00202000020200
dedechess - 6 points - 0002002020
---------------------
1. puressence - 66
2. belerfon - 31
3. vempele - 24
4. kielileike - 23
5. antisuicide - 18
6. chessfriendship - 16
7. tal_fanclub - 16
8. ishak37 - 10
9. dampooo - 10
10. googa - 10
11. chessking2151 - 9
12. calanthe - 8
13. godo1 - 8
14. wanyonyi - 8
15. dedechess - 6
```
