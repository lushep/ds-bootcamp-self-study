feature_columns = ['time on app', 'length of membership', 'avg. session length']
X = customers[feature_columns]
y = customers.loc[:, 'yearly amount spent']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=100, train_size=0.3)
print(f'X_train shape: {X_train.shape}', 
      f'X_test shape: {X_test.shape}', 
      f'y_train shape: {y_train.shape}', 
      f'X_test shape: {y_test.shape}',
     sep='\n')
     
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
train_pred = model.predict(X_train)

print('TEST DATA:')
print('MAE:', metrics.mean_absolute_error(y_test, y_pred))
print('MSE:', metrics.mean_squared_error(y_test, y_pred))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

print('TRAIN DATA:')
print('MAE:', metrics.mean_absolute_error(y_train, train_pred))
print('MSE:', metrics.mean_squared_error(y_train, train_pred))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_train, train_pred)))