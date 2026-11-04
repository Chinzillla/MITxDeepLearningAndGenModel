# Perceptron

A Perceptron is the simplest building block of a neural network

## Math behind Perceptron

Example: student passes an exam based on two factors and the following weights
```
x1: hours spent studying
x2: hours spent sleeping
w1: 2
w2: 0.5
b: -12
```

Explanation of each variable:
- x is the hours spent towards preparing for the exam
- x1 is subset of x and is provided as an input for hours spent studying
- x2 is a subset of x and is provided as an input for hours spent sleeping
- w1 is the impact of hours spent studing towards the final result
- w2 is the impact of hours spent sleeping towards the final result
- b is the bias used to increase the passing requirement threshold. This is typically learned from training data.

Case 1: Lets assume we have a student that studied 5 hours and slept for 8 hours
```
1. Start by defining our x.
x is the hours spent towards the exam preparation

2. Label our input x1, x2
x1 = 5
x2 = 8

3. Label our weights w1, w2
w1 = 2
w2 = 0.5

4. Perform dot product on vector x and vector w
x = [5, 8]
w = [2, 0.5]

Dot_Product(x, w) = x1 * w1 + x2 * w2
Dot_Product(x, w) = 5 * 2 + 8 * 0.5
Dot_Product(x, w) = 14

5. z = Add the dot product by the bias
z = 14 + b
z = 14 + -12
z = 2

6. Now we will input z into our piecewise function (step function)
This is our activation step, and is the condition our neuron needs in order to activate.

f(x) = {
    1, if x >= 0
    0, if x < 0
}

Piecewise function Outputs:
f(x) == 1: Student passes test
f(x) == 0: Student fails test

```

### Manual Perceptron Example
Python Implementation: [Manual Perceptron Project](manual_perceptron.py)
1. Added Inputs for x1 and x2
2. Calculates if student will pass or fail
3. Output: pass or fail, hours of sleep or study needed to pass

## Perceptron Learning