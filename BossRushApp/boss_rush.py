from openai import OpenAI
from dataclasses import dataclass, asdict

# TODO: add functionality so that player can damage bosses
# TODO: Set up function to fight the actual boss
# Specifiy JSON for the choices that the user will get

# ----- Game State ----- #
@dataclass
class BOBBY:
    hp: int = 25
    turn: int = 1

@dataclass
# (Enviromental sustainability hater1)
# The Landfill Lord - name
# BRAINROTTED - TUNG TUNG TUNG SAHUR
# Carbon King/Queen - name
# Mr. Incinerator - name
class Robert:   
    name: str
    category: str
    hp: int = 50


STATE: Dict[str, Any] = {
    "player": BOBBY(),
    "bosses" : [


    print("Welcome to the eco-sustainible Boss Rush Game, in this game you will fight bosses that aren't eco-sustainible, and by answering sustainible questions right, you can damage the bosses.Good Luck!") 
    # rint(" Welcome to the bike-travelling Boss "scape Game, in this game you will run around and avoid the smashing car on a bike! You can escape! Good Luck!")
    