# Cat years, Dog years   ( 8 kyu)
def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
        dog_years = 15 + 9
    else:
        cat_years = 15 + 9 + 4 * (human_years - 2)
        dog_years = 15 + 9 + 5 * (human_years - 2)
    return [human_years, cat_years , dog_years]





# Sum of array singles (7 kyu)

def repeats(arr):
    total  = 0
    for i in range(len(arr)):
        count = 0
        for _ in range(len(arr)):
            if arr[i] == arr[_] and i != _ :
                count += 1
        if count == 0:
            total += arr[i]
    return total




# Triangular Treasure  (7 kyu)


def triangular(n):
    if n <= 0:
        return 0
    else:
        triangular_sum = 0
        
        for i in range(1, n +1):
            triangular_sum += i
            
        return triangular_sum
    

# Find the Mine!  (6 kyu)

def mine_location(field):
    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col] == 1:
                return [row, col] 




# Find Nearest square number (9 kyu)

import math

def nearest_sq(n):
    
    nearest_root = round(math.sqrt(n))
    nearest_square = nearest_root ** 2
    
    if nearest_square == n:
        return n
    else:
        return nearest_square
   



# Calculate Variance (5 kyu)


def variance(numbers): 
    def calculate_variance(numbers):
        if not numbers:
            return 0.0
    
    n = len(numbers)
    mean = sum(numbers) / n
    variance = sum((x - mean) ** 2 for x in numbers) / n
    
    return variance




# Rot13  (kyu 5)
def rot13(message):
    result = ""
    
    for char in message:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            
            rotated = (ord(char) - offset + 13) % 26 + offset
            result += chr(rotated)
        else:
            result += char
    return result