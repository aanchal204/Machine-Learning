from numpy import *		#reading from .csv file
import matplotlib.pyplot as plt 	#plotting the graph

def update(data,learning_rate,theta0,theta1):
	length = len(data)
	theta0_gradient = 0
	theta1_gradient = 0
	m = (float)(len(data))
	for i in range(length):
		x = data[i,0]
		y = data[i,1]
		theta0_gradient += (theta0 + theta1*x - y)
		theta1_gradient += (theta0 + theta1*x - y)*x
	theta0 = theta0 - learning_rate*1/m*theta0_gradient
	theta1 = theta1 - learning_rate*1/m*theta1_gradient
	return [theta0,theta1]

def gradient_descent(data,learning_rate,num_iterations,theta0,theta1):
	for i in range(num_iterations):
		theta0,theta1 = update(data,learning_rate,theta0,theta1)
	return [theta0,theta1]

def plot_graph(data,theta0,theta1):
	for i in range(len(data)):
		plt.scatter(data[i,0],data[i,1])		#(x,y)
	plt.plot([0,100],[theta0,theta1*80+theta0])		#[x1,x2],[y1,y2]
	plt.show()

def begin():
	#store the data
	data = genfromtxt('data.csv',delimiter=',')
	#assume the value of theta0 and theta1
	theta0 = 0
	theta1 = 0
	#initialise learning rate and number of iterations
	learning_rate = 0.00001
	num_iterations = 400
	[theta0 , theta1] = gradient_descent(data,learning_rate,num_iterations,theta0,theta1)
	print "After {0} iterations, value of theta0 = {1}, theta1 = {2}".format(num_iterations,theta0,theta1)
	plot_graph(data,theta0,theta1)

if __name__ == '__main__':
	begin()
	
	