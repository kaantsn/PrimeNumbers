def is_prime(num):
    """
    Verilen sayının asal olup olmadığını kontrol eder.
    """
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(num**0.5)+1, 2):
            if num % i == 0:
                return False
        return True

# kullanıcıdan sayı girdisi alınır
num = int(input("Bir sayı girin: "))

# is_prime fonksiyonu çağrılır ve sonuç ekrana yazdırılır
if is_prime(num):
    print(num, "asal bir sayıdır.")
else:
    print(num, "asal bir sayı değildir.")
