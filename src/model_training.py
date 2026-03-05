from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from preprocessing import preprocessing

df, X, y = preprocessing()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

lr_model = LogisticRegression()  
lr_model.fit(X_train, y_train)

X_test_scaled = scaler.transform(X_test) 
y_pred = lr_model.predict(X_test_scaled)

