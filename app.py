import streamlit as st
from src.config import trial_names
from src.trial_scores_historical import world_records, median_scores, difficulty_modifiers
from src.utils import calculate_relative_score

# Map user-facing names to keys used in the scoring function
trial_name_to_key = {
    "Maw of Lorkhaj": "vMOL",
    "Halls of Fabrication": "vHOF",
    "Asylum Sanctorium": "vAS",
    "Cloudrest": "vCR",
    "Sunspire": "vSS",
    "Kyne's Aegis": "vKA",
    "Rockgrove": "vRG",
    "Dreadsail Reef": "vDSR",
    "Sanity's Edge": "vSE",
    "Lucent Citadel": "vLC"
}

st.title("ESO Trial Score App")

# Trial name dropdown
trial = st.selectbox("Choose Trial", trial_names, placeholder="Select Trial Name, eg. Kyne's Aegis")

# Current score input
score = st.number_input("Your Team's Score", min_value=0, step=1)

# Calculate and display the relative score if a valid trial is selected
if trial and trial in trial_name_to_key:
    trial_key = trial_name_to_key[trial]
    rel_score = calculate_relative_score(
        score, trial_key, world_records, median_scores, difficulty_modifiers
    )
    st.write(f"Relative Score: {rel_score}")
else:
    st.write("Relative Score: -") 