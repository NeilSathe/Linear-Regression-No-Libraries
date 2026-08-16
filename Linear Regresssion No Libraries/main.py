# This is a Python script that demonstrates a simple linear regression model using no libraries. 
#The data set used is a sample data set comparing X (temperature) and Y (amount of ice creams sold by a street vendor). The script calculates the slope and intercept of the regression line and allows the user to input a new value of X to predict the corresponding Y value.



X = [6,12,15,27,35,42] #Temperature in Celsius
y = [2,3,5,17,28,36] #Amount of ice creams sold by the street vendor

#Calculate the average of X and Y

total_x = 0
total_y = 0

for i in X : 

    total_x += i
    

for i in y :

    total_y += i


avg_x = total_x / len(X)
avg_y = total_y / len(y)

#Calculate the numerator of the formula for the slope (m) of the regression line

numerator_sum = 0
denominator_sum = 0

for i in range(len(X)):

    current_x = X[i]
    current_y = y[i]

    numerator_sum += (current_x - avg_x) * (current_y - avg_y)
    denominator_sum += (current_x - avg_x) ** 2


m = numerator_sum / denominator_sum
c = avg_y - (m * avg_x)


def predict(new_x):

    return (m * new_x) + c

new_x = float(input("Enter the temperature to predict the amount of ice creams sold by the street vendor: "))

predicted_y = predict(new_x)
print(f"Predicted amount of ice creams sold: {round(predicted_y)}")