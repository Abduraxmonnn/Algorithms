# data = {
#     'BMW': 10,
#     'MERC': 8,
#     'AUDI': 6,
#     'FORD': 5,
# }

# data_2 = dict(BMW=10, MERC=8, AUDI=6, FORD=5)

# data = {}
# data_2 = dict()

# data['BMW']
# data.get('BMW')

# del data['MERC']

# data.pop('MERC')

# len(data)

# data_2 = dict.fromkeys(['FERRARI', 'NISSAN', 'BYD'], 0)

# print('BMW' in data)

# print('BMW' not in data)

# if 'BYD' in data:
#     print(data['BYD'])
# else:
#     data['BYD'] = None
#     print(data)

# print(data.get('BYD', 0))

# print(data.setdefault('BYD', 1))

# print(data.items())

# for pair in data.items():
#     print(pair[0], ':', pair[1])

# for key, value in data.items():
#     print(key, ':', value)

# print(data.values())
# print(data.keys())

# # MISOL 1

# data = {}
# data_str = "BMW GERMANY 5 10000 12000 8500 9000 15000"
# data_list = data_str.split()
#
# data['company_name'] = data_list[0]
# data['company_country'] = data_list[1]
# data['facture_numbers'] = int(data_list[2])
# data['company_workers_number'] = []
#
# for item in data_list[3:]:
#     data['company_workers_number'].append(int(item))
#
# print(data)
