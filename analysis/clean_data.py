import pandas as pd

human_data = pd.read_csv("../data/human_data.txt", header=None)
bot_data = pd.read_csv("../data/bot_data.txt", header=None)


#adding headers
human_data = human_data.rename(columns={0: 'dateTime', 1: 'onOff', 2: 'X', 3: 'Y'})
bot_data = bot_data.rename(columns={0: 'dateTime', 1: 'onOff', 2: 'X', 3: 'Y'})

#adding identifying column
human_data['type'] = 0
bot_data['type'] = 1

#combine datasets
df = human_data._append(bot_data)
print(df)

#splitting on onOff switch
#row[2] = onOff, row[5] = session_id
df['session_id'] = 0
prev = 0
count = 0
for index, row in df.iterrows():
    if(row.iloc[1] == 1 and prev == 0):
        df.at[index, 'session_id'] = count
        # print(count)
        count += 1
    
    prev = row.iloc[1]

#removing redundant rows
df = df[df['onOff'] != 0]

#removing redundant column
df = df.drop('onOff', axis=1)

#convert to datetime variable
df['dateTime'] = pd.to_datetime(df['dateTime'], format='%Y-%m-%d %H:%M:%S.%f', errors='coerce')


df = df.sort_values('session_id')
print(df)

#create time-elapsed feature
time_delta = df.groupby('session_id')['dateTime'].agg(['min', 'max'])
time_delta['delta'] = time_delta['max'] - time_delta['min']
print(time_delta)


#x, y linearity feature


#x, y max delta feature
X_delta = df.groupby('session_id')['X'].agg(['min', 'max'])
X_delta['X_delta'] = X_delta['max'] - X_delta['min']
print(X_delta)

Y_delta = df.groupby('session_id')['Y'].agg(['min', 'max'])
Y_delta['Y_delta'] = Y_delta['max'] - Y_delta['min']
print(Y_delta)

#convert to wide format data
time_delta = time_delta.reset_index()
X_delta = X_delta.reset_index()
Y_delta = Y_delta.reset_index()

wide_df = df.groupby('session_id').agg({
    'X': lambda x: x.tolist(),
    'Y': lambda y: y.tolist(),
    'type': 'first'
}).reset_index()

#add variables
wide_df = wide_df.merge(time_delta[['session_id', 'delta']], on='session_id', how='left')
wide_df = wide_df.merge(X_delta[['session_id', 'X_delta']], on='session_id', how='left')
wide_df = wide_df.merge(Y_delta[['session_id', 'Y_delta']], on='session_id', how='left')


print(wide_df.columns)


wide_df.to_csv('data.csv')