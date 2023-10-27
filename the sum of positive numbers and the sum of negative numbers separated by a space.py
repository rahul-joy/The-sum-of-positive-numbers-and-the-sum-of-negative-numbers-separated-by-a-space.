# Read the input
N = int(input())
values = list(map(int, input().split()))

# Initialize variables to store the sums of positive and negative numbers
sum_positive = 0
sum_negative = 0

# Iterate through the list of values and update the sums
for value in values:
    if value > 0:
        sum_positive += value
    elif value < 0:
        sum_negative += value

# Output the sums in the required format
print(sum_positive, sum_negative)
