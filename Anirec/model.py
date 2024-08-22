import pandas as pd
import numpy as np
import pickle

# Load data
df = pd.read_csv(r"C:\Users\HP\Desktop\Projects\Anirec (Cli)\Anirec\data\preprocessed_ani_data.csv")

with open(r'C:\Users\HP\Desktop\Projects\Anirec (Cli)\Anirec\data\similarity_matrix.pkl', 'rb') as f:
    similarity_matrix = pickle.load(f)

# Initialize parameters
round_no = 0

user_history_dict = {
    'already_recommended' : [],
    'arm1' : {'anime':[], 'rating':[], 't': 1},
    'arm2' : {'anime':[], 'rating':[], 't': 1},
    'arm3' : {'anime':[], 'rating':[], 't': 1}
}

def user_history(temp_dict, arm):
    global user_history_dict, round_no
    round_no += 1
    if 'anime' in temp_dict:
        user_history_dict['already_recommended'].extend(temp_dict['anime'])
        user_history_dict[f'arm{arm}']['anime'].extend(temp_dict['anime'])
        user_history_dict[f'arm{arm}']['rating'].extend(temp_dict['rating'])
    else:
        for i in range(3):
            user_history_dict['already_recommended'].extend(temp_dict[f'arm{i+1}']['anime'])
            user_history_dict[f'arm{i+1}']['anime'].extend(temp_dict[f'arm{i+1}']['anime'])
            user_history_dict[f'arm{i+1}']['rating'].extend(temp_dict[f'arm{i+1}']['rating'])
    print('Your history: ', user_history_dict)
    print('Round:', round_no)

def UCB() -> int:
    global user_history_dict, round_no
    ucb_values: list[tuple[int, float]] = []
    for i in range(3):
        t = user_history_dict[f'arm{i+1}']['t']
        ratings = user_history_dict[f'arm{i+1}']['rating']
        average_rating = sum(ratings) / len(ratings) if ratings else 0
        exploration_term = np.sqrt(2 * np.log(round_no) / t)
        ucb_values.append((i+1, average_rating + exploration_term))
    
    print('UCB Values:', dict(ucb_values))
    
    return max(ucb_values, key=lambda x: x[1])[0]

def recommend(arm):
    global user_history_dict
    similar_anime = []
    anime_list = []

    for shown in user_history_dict[f'arm{arm}']['anime']:
        distances = similarity_matrix[shown]
        anime_list.extend(sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:10])

    similar_anime.extend(sorted(anime_list, reverse=True, key=lambda x:x[1]))
    anime_list = []
    anime_list.extend([i[0] for i in similar_anime])
    recommendations = [i for i in anime_list if i not in user_history_dict['already_recommended']][:3]
    
    return recommendations

while True:
    temp_dict = {
        'anime': [],
        'rating': []
    }
    user_input = {
        'arm1' : {'anime':[20], 'rating':[2],},
        'arm2' : {'anime':[224], 'rating':[4],},
        'arm3' : {'anime':[1], 'rating':[5],}
    }

    if round_no == 0:
        user_history(user_input, 0)
    else:
        arm = UCB()

        user_history_dict[f'arm{arm}']['t'] += 1

        recommendations = recommend(arm)
        recommendations = [i for i in recommendations if i in range(len(df))]
        
        # Display anime names instead of IDs
        print('Recommendations:')
        for idx, rec_id in enumerate(recommendations):
            print(f"{idx + 1}) {df.iloc[rec_id].name_english}")

        # Ask the user which anime they want to rate
        selected_anime_index = int(input(f"Select the anime to rate (1-{len(recommendations)}): ")) - 1
        selected_anime_id = recommendations[selected_anime_index]

        # Get the rating from the user
        rating = int(input(f"Rate anime '{df.iloc[selected_anime_id].name_english}': "))
        
        temp_dict['anime'].append(selected_anime_id)
        temp_dict['rating'].append(rating)

        user_history(temp_dict, arm)

    i = input('Want to continue (y/n): ')
    if i == 'n':
        break
