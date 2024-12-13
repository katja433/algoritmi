import math

# Funkcija, kas aprēķina vidējo vērtību
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

# Funkcija, kas aprēķina mediānu
def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        middle1 = sorted_numbers[n // 2 - 1]
        middle2 = sorted_numbers[n // 2]
        return (middle1 + middle2) / 2

# Funkcija, kas aprēķina standarta novirzi
def calculate_standard_deviation(numbers, mean):
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)

# Funkcija, kas veic saraksta šķirošanu un statistikas aprēķinus
def analyze_numbers(numbers):
    if not numbers:
        return "Saraksts ir tukšs!"
    
    # 1. Skaitļu šķirošana
    sorted_numbers = sorted(numbers)
    
    # 2. Vidējā vērtība
    mean = calculate_mean(numbers)
    
    # 3. Mediāna
    median = calculate_median(numbers)
    
    # 4. Standarta novirze
    standard_deviation = calculate_standard_deviation(numbers, mean)
    
    # Rezultātu atgriešana
    result = {
        "Sorted Numbers": sorted_numbers,
        "Mean": mean,
        "Median": median,
        "Standard Deviation": standard_deviation
    }
    
    return result

# Galvenā funkcija, kas testē algoritmu
def main():
    # Ievadām skaitļus sarakstā
    numbers = [5, 2, 9, 1, 5, 6]
    
    print("Ievadītais saraksts: ", numbers)
    
    # Analizējam skaitļus
    result = analyze_numbers(numbers)
    
    # Izdrukājam rezultātus
    print("Rezultāti:")
    print(f"Šķirotais saraksts: {result['Sorted Numbers']}")
    print(f"Vidējā vērtība: {result['Mean']}")
    print(f"Mediāna: {result['Median']}")
    print(f"Standarta novirze: {result['Standard Deviation']}")

# Izsaucam galveno funkciju
if __name__ == "__main__":
    main()
