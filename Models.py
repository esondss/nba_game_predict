import joblib
from keras.models import load_model

class RandomForest():

    def __init__(self,path='/models/clf_1_rf.pkl'):

        self.model=joblib.load(path)

    def predict(self,X):

        y_hat=self.model.predict(X)

        return y_hat


class NeuralNetwork():

    def __init__(self,path='/models/clf_1_nn.h5'):

        model=load_model(path)
        
        self.model=model.compile(

        loss='binary_crossentropy',
        optimizer='rmsprop',
        metrics=['accuracy']

        )

    def predict(self,X):

        y_hat=self.model.predict_classes(X)

        return y_hat
