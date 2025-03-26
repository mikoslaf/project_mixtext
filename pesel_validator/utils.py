from datetime import date


def pesel_get_date(pesel: str) -> str:
    year = pesel[0:2]
    month = pesel[2:4]
    day = pesel[4:6]
    
    date_to_add = [1900, 2000, 2100, 2200, 1800]

    for i in range(len(date_to_add)):
        if int(month) <= 12 + i * 20:
            year = int(year) + date_to_add[i]
            month = int(month) - i * 20
            break

    return date(int(year), int(month), int(day))

def pesel_is_vaild(pesel: str) -> bool:
    if len(pesel) != 11 or not pesel.isdigit():
        return False
    date_of_birth = None
    try:
        date_of_birth = pesel_get_date(pesel)
        print(date_of_birth)
    except ValueError:
        return False
    if date_of_birth > date.today():
        return False
    
    
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    checksum = sum(int(pesel[i]) * weights[i] for i in range(10)) % 10
    control_digit = (10 - checksum) % 10

    if control_digit != int(pesel[10]):
        return False
    return True

def pesel_get_gender(pesel: str) -> str:
    if int(pesel[9]) % 2 == 0:
        return "female"
    else:
        return "male"