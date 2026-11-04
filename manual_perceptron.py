# Start with our inputs for Student
def define_x():
    print("Please Enter how many hours did you studied:")
    x1 = input()
    print("Please Enter how many hours did you slept:")
    x2 = input()
    return [int(x1), int(x2)]

# Reusable dot product func
def dot_product(x,y):
    if len(x) != len(y):
        raise ValueError("Please enter valid vectors")
    
    dp_sum = 0
    for i in range(0,len(x)):
        prod = x[i] * y[i]
        dp_sum += prod

    return dp_sum

# Calculate our Z
def calculate_z(dp, b):
    return dp + b

# Define the piecewise function
def piecewise_func(z):
    if z >= 1:
        return True
    else:
        return False 

def main():
    print("Hi! Welcome to the perceptron sample for: Will Student Pass or Fail exam\n")
    weights = [2, 0.5]
    bias = -12

    vec_x =define_x()
    dp_res = dot_product(vec_x, weights)
    z = calculate_z(dp_res, bias)
    result = piecewise_func(z)
    print(result)

if __name__ == "__main__":
    main()