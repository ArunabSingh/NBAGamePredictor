import pandas as pd

PATH = "C:/Users/sjind/ASingh/BCIT-4th-term/PredictiveMachineLearning/Assignments/Assignment1/"
CSV_FILE = "nba_df.csv"

df = pd.read_csv(PATH + CSV_FILE)
print(df.head())

df = df.reset_index(drop=True)
len(df)

import warnings

warnings.filterwarnings("ignore")
prev_game_df = df[df['Date'] < '12/12/2020'][
    (df['Home'] == "Los Angeles Lakers") | (df['Away'] == 'Boston Celtics')].sort_values(by='Date').tail(10)
print(prev_game_df)
h_df = prev_game_df.iloc[:, range(0, 32, 31)]

h_df = h_df.loc[h_df['Home'] == 'Los Angeles Lakers']
print(h_df)


def get_avg_win_pct_last_n_games(team, game_date, df, n):
    prev_game_df = df[df['Date'] < game_date][(df['Home'] == team) | (df['Away'] == team)].sort_values(by='Date').tail(
        n)

    wins = 0

    result_df = prev_game_df.iloc[:, range(0, 32, 31)]
    h_df = result_df.loc[result_df['Home'] == team]

    h_wins = h_df.loc[h_df['Result'] == 1]

    wins += len(h_wins)

    a_df = result_df.loc[result_df['Home'] != team]
    a_wins = a_df.loc[a_df['Result'] == 0]

    wins += len(a_wins)

    return wins / n


get_avg_win_pct_last_n_games('Boston Celtics', '12/12/2020', df, 10)

for season in df['Season'].unique():

    season_stats = df[df['Season'] == season].sort_values(by='Date').reset_index(drop=True)
    for index, row in df.iterrows():
        game_id = row['Game_ID']
        game_date = row['Date']
        h_team = row['Home']
        a_team = row['Away']

        df.loc[index, 'Home_W_Pct_10'] = get_avg_win_pct_last_n_games(h_team, game_date, df, 10)

        df.loc[index, 'Away_W_Pct_10'] = get_avg_win_pct_last_n_games(a_team, game_date, df, 10)

print(df.head())
