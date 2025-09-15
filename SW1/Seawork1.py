while True:
    def to_ruppee(ruppe):
        converted = []
        for v in ruppe:
            converted_value = v * 88.18
            converted.append(round(converted_value, 2))
        return converted 
    
    def to_pound(pound):
        converted = []
        for v in pound:
            converted_value = v * 0.73
            converted.append(round(converted_value, 2))
        return converted 
    
    def to_yen(yen):
        converted = []
        for v in yen:
            converted_value = v * 0.73
            converted.append(round(converted_value, 2))
        return converted 
    
    dollar = input('enter dollar($)(*to exit): ')

    if dollar == "*":
        print('Bye')
        break

    x = dollar.split('@')

    values = []
    for v in x:
        values.append(float(v))
        
    print('dollar$  Indian Ruppe(R) British(P)  China(Y)')

    for v in values:
        print(v)
    print()

    x = input()
    convert_to = x.upper()
    
    print('dollar$  Indian Ruppe(R) British(P)  China(Y)')
    
    if convert_to == 'R':
        for v in to_ruppee(values):
            print(f'         {v}')

    if convert_to == 'P':
        for v in to_pound(values):
            print(f'                         {v}')

    if convert_to == 'Y':
        for v in to_yen(values):
            print(f'                                     {v}')

    

    