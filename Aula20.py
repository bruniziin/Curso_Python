primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

float_primeiro_valor = float(primeiro_valor)
float_segundo_valor = float(segundo_valor)

if primeiro_valor >= segundo_valor:
    print(f'{float_primeiro_valor=:.0f} é maior ou igual o {float_segundo_valor=:.0f}')
          
else:
    print(f'{float_segundo_valor=:.0f} é maior que o {float_primeiro_valor=:.0f}')
          