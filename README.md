# Linear Regression With No Libraries

A simple implementation of **linear regression in Python built entirely from scratch**, without using external machine learning libraries such as Scikit-Learn.

This project demonstrates the mathematical foundations behind linear regression by manually calculating the slope, intercept, and predictions.

## Overview

The program uses a small dataset containing:

* **X:** Temperature
* **y:** Number of ice creams sold

It calculates the linear regression equation:

**y = mx + c**

where:

* `m` is the slope of the regression line
* `c` is the y-intercept
* `x` is the input value
* `y` is the predicted value

The user can enter a new temperature, and the program predicts the corresponding number of ice creams sold.

## How It Works

The program follows these steps:

1. Calculates the mean of the `X` values.
2. Calculates the mean of the `y` values.
3. Calculates the numerator and denominator required to determine the slope.
4. Calculates the slope (`m`).
5. Calculates the y-intercept (`c`).
6. Defines a prediction function using the regression equation.
7. Accepts a new input from the user.
8. Produces the predicted number of ice creams sold.

The slope is calculated using:

**m = Σ((x − x̄)(y − ȳ)) / Σ((x − x̄)²)**

The y-intercept is then calculated using:

**c = ȳ − mx̄**

## Example Dataset

| Temperature (°C) | Ice Creams Sold |
| ---------------: | --------------: |
|                6 |               2 |
|               12 |               3 |
|               15 |               5 |
|               27 |              17 |
|               35 |              28 |
|               42 |              36 |

## Requirements

* Python 3.x
* No external libraries are required.

## Running the Program

Clone the repository and run the Python script:

```bash
python main.py
```

The program will prompt you to enter a temperature and will return the predicted number of ice creams sold.

### Example

```text
Enter the weather to predict the amount of ice creams sold by the street vendor: 30
Predicted amount of ice creams sold: 20
```

*The exact prediction may vary depending on the dataset and calculations used.*

## Purpose

The purpose of this project is to understand how **linear regression works mathematically and programmatically**, rather than relying on pre-built machine learning libraries.

This provides a foundation for understanding more advanced machine learning techniques and libraries such as **Scikit-Learn, PyTorch etc.**

## Future Improvements

Potential improvements include:

* Adding a graph of the dataset and regression line
* Calculating model performance metrics such as R²
* Allowing users to provide their own datasets
* Comparing the implementation with Scikit-Learn's `LinearRegression`
* Expanding the model to support multiple input variables

