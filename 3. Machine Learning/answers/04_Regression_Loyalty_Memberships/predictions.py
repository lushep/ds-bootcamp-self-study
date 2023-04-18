y_pred = model.predict(X_test)
np.array([y_test[:10], y_pred[:10]]).T