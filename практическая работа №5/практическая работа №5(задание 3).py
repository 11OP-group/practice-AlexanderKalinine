def convert_usd_to_rub(USD):
    '''переводит долоры в рубли по курсу 1 долор к 95.50'''
    RUB = float(USD) * 95.50 
    return RUB

cash_USD = input('Ввидите сумму долоров для перевода в рубли: ')
cash_RUB = convert_usd_to_rub(cash_USD)
print(f'Сумма после перевода в рубли: {cash_RUB}')