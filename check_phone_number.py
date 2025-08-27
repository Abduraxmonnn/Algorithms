number = '+998 99 889 59 89'
number = number.replace(' ', '')

company_codes = ['33', '90', '93', '94', '95', '98', '99']

country_code = []
company_code = []
body = []

if '+' in number and len(number) == 13:
    country_code.append(number[1:4])
    company_code.append(number[4:6])
    body.append(number[6:])
    if country_code[0] == '998':
        if company_code[0] in company_codes:
            print(True)
        else:
            print('Company Not Found. This must be like 33, 99...')
    else:
        print('Country code must be like "998"')
else:
    print('Error Phone Number incorrect. Please Check Again. (On the Phone Number must have "+")')
