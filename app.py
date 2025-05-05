import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

import streamlit as st
from config import trial_names, world_records, median_scores, difficulty_modifiers
from utils import calculate_relative_score, scale_with_difficulty

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

# Calculate and display the relative score if a valid trial is selected and button is pressed
if trial and trial in trial_name_to_key:
    trial_key = trial_name_to_key[trial]
    if st.button('Calculate'):
        rel_score = calculate_relative_score(
            score, trial_key, world_records, median_scores
        )
        scaled_score = scale_with_difficulty(rel_score, trial_key, difficulty_modifiers)
        st.write(f"Relative Score :: {rel_score}")
        st.write(f"After Scaling with Difficulty :: {scaled_score}")
else:
    st.write("Relative Score :: ") 