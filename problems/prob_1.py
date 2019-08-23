"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.


Answer == 233168
"""

# define multiples
multi_1 = 3
multi_2 = 5

numbers = list(range(1000))
results = []

for number in numbers:
    if number % multi_1 == 0 or number % multi_2 == 0:
        results.append(number)

print(sum(results))
