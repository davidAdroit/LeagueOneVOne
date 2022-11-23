import random

import streamlit


str.title("League of Legends 1v1 Generator")
streamlit.title("League of Legends 1v1 Generator")
streamlit.write("Created by David, the coding mastermind           || discord: airpodenjoyer#9126 |")
streamlit.write("Link back to main site: https://davidadroit-personalsite-personalwebsite-8fhv1n.streamlit.app/")

streamlit.success("Before generating, decide who is player A and player B")
champ_pool = ["Ezreal", "Jhin", "Jayce", "Tristana", "Morgana", "Kayle", "Nunu", "Varus", "Malphite", "Yorick", "Maokai", "Ivern", "Annie", "Malzahar", "Anivia", "Aatrox", "Ashe", "Caitlyn", "Brand", "Gragas", "Gangplank", "Garen", "Heiemerdinger", "Illaoi", "Lux", "Ryze", "Syndra"]
adc_pool = ["Ezreal", "Jhin", "Tristana", "Ashe", "Twitch"]
mage_pool = ["Anivia", "Veigar", "Annie", "Ryze", "LeBlanc", "Lissandra"]
start_items = ["Dorans Ring", "Dorans Blade", "Dorans Shield", "Regen Potion"]
start_spells = ["Flash/Ignite", "Flash/Heal", "Flash/Exhuast", "Flash/Cleanse", "Flash/Barrier", "Flash/Ghost"]

if streamlit.button('Generate 1v1 Rules and Set Up (all champs)'):
    player_a_champ = random.choice(champ_pool)
    streamlit.write(f"Player A will be playing : {player_a_champ}")
    player_a_start_items = random.choice(start_items)
    streamlit.write(f"Player A will be using : {player_a_start_items}")
    player_a_start_spells = random.choice(start_spells)
    streamlit.write(f"Player A's spells will be : {player_a_start_spells}")
    # ------------ player B stuff below now
    streamlit.write("-"*200)
    player_b_champ = random.choice(champ_pool)
    streamlit.write(f"Player B will be playing : {player_b_champ} ")
    player_b_start_items = random.choice(start_items)
    streamlit.write(f"Player B will be starting with {player_b_start_items}")
    player_b_start_spells = random.choice(start_spells)
    streamlit.write(f"Player B's spells will be : {player_b_start_spells}")
    ###
else:
    streamlit.write("---------------------------------------------")
    streamlit.write('Created by David')

if streamlit.button("Generate ADC 1v1"):
    streamlit.write("player a will be playing ... ")
else:

    streamlit.write("")
