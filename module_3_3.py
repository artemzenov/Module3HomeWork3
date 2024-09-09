print(f'1.Функции с параметрами по умолчанию:')

def print_params(
        a=1, 
        b='string', 
        c=True
    ):
    
    print(f'a={a :<15}b={b :<15}c={c}')


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(10, 'test', False)

print(f'\n2.Распаковка параметров:')

values_list = [2, 'test', 3.5]
values_dict = dict(a='abc', b=25, c=False)

print_params(*values_list)
print_params(**values_dict)

print(f'\n3.Распаковка + отдельные параметры:')

values_list_2 = ['text', 3.14]

print_params(*values_list_2, 42)
