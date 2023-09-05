import matplotlib.pyplot as plot

dataset = open ('Dataset.csv','r')
dataset.readline()

X = []
Y = []
line = dataset.readline()
while line != '':
    A , B = line.strip().split(',')
    A , B = float(A) , float(B)
    X.append(A)
    Y.append(B)
    line = dataset.readline()

print(X)
print(Y)

mean_x = sum(X) / len(X)
mean_y = sum(Y) / len(Y)

# Calculate the terms needed for the slope (m) and y-intercept (b)
numerator = 0
denominator = 0

for i in range(len(X)):
    numerator += (X[i] - mean_x) * (Y[i] - mean_y)
    denominator += (X[i] - mean_x) ** 2

# Calculate the slope (m) and y-intercept (b)
m = numerator / denominator
c = mean_y - (m * mean_x)

# Predict a new value
new_x =1.1
predicted_y = (m * new_x) + c

print("Slope (m):", m)
print("Y-Intercept (c):", c)
print(f"Predicted value for x={new_x}: {predicted_y:.2f}")

# Predict values for the regression line
regression_line = [(m * x) + c for x in X]

# Plot the data points
plot.scatter(X, Y, label='Data Points')

# Plot the regression line
plot.plot(X, regression_line, label='Regression Line', color='red')

# Set labels and title
plot.xlabel('X-axis')
plot.ylabel('Y-axis')
plot.legend()
plot.title('Linear Regression Example')

# Show the plot
plot.show()

# Model Accuracy

# R Squared = Submission of (Yp-Y_mean)^2 / submission of (Yi - Y_mean)^2
nume = 0
denom = 0
for x in range(len(X)):
    nume += ((((m*X[x])+c)-mean_y)**2)
for y in range(len(Y)):
    denom += ((Y[y]-mean_y)**2)
r_squared = (nume/denom)*100

print("Accuracy of the model W.R.T dataset is : ",r_squared ,"%")