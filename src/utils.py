import math
from trial_scores_historical import world_records, median_scores, difficulty_modifiers

def calculate_relative_score(user_score, trial_key, world_records, median_scores, difficulty_modifiers, k=10):
    """
    Calculate a normalized score using a sigmoid for relative performance,
    then squash with tanh after applying a difficulty modifier.
    Returns a value in (0, 1).
    """
    S_user = user_score
    S_median = median_scores[trial_key]
    S_wr = world_records[trial_key]
    difficulty = difficulty_modifiers.get(trial_key, 1)
    if S_wr == S_median:
        r = 0.5
    else:
        r = (S_user - S_median) / (S_wr - S_median)
    # Sigmoid for relative score
    rel_score = 1 / (1 + math.exp(-k * (r - 0.5)))
    # Apply difficulty and squash with tanh
    tanh_score = (math.tanh(rel_score * difficulty) + 1) / 2
    return round(tanh_score, 4)

