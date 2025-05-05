import math
import numpy as np
from config import world_records, median_scores, difficulty_modifiers, vLC_scores, vLC_scores_HM, vSE_scores, vSE_scores_HM, vDSR_scores, vDSR_scores_HM, vRG_scores, vRG_scores_HM, vKA_scores, vKA_scores_HM, vSS_scores, vSS_scores_HM, vCR_scores, vCR_scores_HM, vAS_scores, vAS_scores_HM, vHOF_scores, vHOF_scores_HM, vMOL_scores, vMOL_scores_HM




all_scores_dict = {
    'vLC': vLC_scores + vLC_scores_HM,
    'vSE': vSE_scores + vSE_scores_HM,
    'vDSR': vDSR_scores + vDSR_scores_HM,
    'vRG': vRG_scores + vRG_scores_HM,
    'vKA': vKA_scores + vKA_scores_HM,
    'vSS': vSS_scores + vSS_scores_HM,
    'vCR': vCR_scores + vCR_scores_HM,
    'vAS': vAS_scores + vAS_scores_HM,
    'vHOF': vHOF_scores + vHOF_scores_HM,
    'vMOL': vMOL_scores + vMOL_scores_HM
}

def calculate_relative_score(user_score, trial_key, world_records, median_scores, curve='tanh', alpha=5, gamma=1):
    scores = np.array(all_scores_dict[trial_key])
    median = median_scores[trial_key]
    world_record = world_records[trial_key]

    # Calculate percentiles
    user_percentile = np.sum(scores <= user_score) / len(scores)
    median_percentile = np.sum(scores <= median) / len(scores)
    world_record_percentile = np.sum(scores <= world_record) / len(scores)

    # Scale percentile between median and world record
    if world_record_percentile == median_percentile:
        scaled = 0.0
    else:
        scaled = (user_percentile - median_percentile) / (world_record_percentile - median_percentile)
        scaled = np.clip(scaled, 0, 1)

    # Apply curve
    if curve == 'tanh':
        result = (np.tanh(alpha * (scaled - 0.5)) + 1) / 2
    elif curve == 'sigmoid':
        result = 1 / (1 + np.exp(-alpha * (scaled - 0.5)))
    elif curve == 'power':
        result = scaled ** alpha
    elif curve == 'softmax':
        result = (np.exp(gamma * scaled) - 1) / (np.exp(gamma) - 1)
    else:
        result = scaled

    # Guarantee world record maps to 1
    if user_score >= world_record:
        return 1.0
    return round(float(result), 4)

def scale_with_difficulty(relative_score, trial_key, difficulty_modifiers):
    modifier = min(difficulty_modifiers[trial_key], 1)
    scaled_score = relative_score * modifier
    return round(max(0, min(scaled_score, 1)), 4)

# if __name__ == "__main__":
#     relative_score = calculate_relative_score(121000, 'vCR', world_records, median_scores, difficulty_modifiers, curve='tanh', alpha=5, gamma=1)

#     print(f"RELATIVE SCORE :: {relative_score}")
#     print(f"SCALED WITH DIFFICULTY SCORE :: {scale_with_difficulty(relative_score, 'vCR', difficulty_modifiers)}")