def quarter(timestamp) -> str:
    return timestamp.strftime("%Y-%m-%d")

def pounds(number, units:str = "") -> str:
    return'£{:,}{}'.format(number, units)

def percent_from_ratio(number : float) -> str:
    return percent((number - 1) * 100)

def percent(number, dp : int = 1) -> str:
    return f'{round(number, dp)}%'