import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("FER_PeakEmotionsWithNeutral.csv")
df = pd.DataFrame(data)
x,y = data.loc[:,data.columns != 'emotion'], data.loc[:,'emotion']
#df.drop(['emotion'])
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 42)

model=RandomForestClassifier()
model.fit(x_train, y_train)
model.score(x_test,y_test)
print(model.score(x_test,y_test)*100)