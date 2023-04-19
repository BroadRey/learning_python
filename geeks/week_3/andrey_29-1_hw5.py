Geeks = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}

del Geeks['bag']
Geeks['address'] = 'Ibraimova 103'
Geeks['phone'] = '0507052018'
Geeks['instagram'] = 'geeks_edu'
Geeks['courses'] = set(Geeks['courses'] + ['Fullstack', 'UX/UI'])
Geeks['founding_date'] = '12.12.2018'

print('Количество курсов:', len(Geeks['courses']), '\n')

print("На данный момент словарь выглядит следующим образом:")
for k, v in Geeks.items():
    print(f'\t{k}: {v}')
