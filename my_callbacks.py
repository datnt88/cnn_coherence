from __future__ import division
import keras

class Histories(keras.callbacks.Callback):
	def on_train_begin(self, logs={}):
		self.accs = []
		self.losses = []

	def on_train_end(self, logs={}):
		return

	def on_epoch_begin(self, epoch, logs={}):
		return

	def on_epoch_end(self, epoch, logs={}):
		self.losses.append(logs.get('loss'))
		
                y_pred = self.model.predict([self.model.validation_data[0],self.model.validation_data[1]])
                count = 0
                n = len(y_pred)
                print ("\n")
                print (y_pred)
                for i in range(0,n):
                    if y_pred[i][0] > y_pred[i][1]:
                        count = count +1
		print(count/n)
		self.accs.append(count/n)

		return

	def on_batch_begin(self, batch, logs={}):
		return

	def on_batch_end(self, batch, logs={}):
		return
