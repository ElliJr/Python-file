real = float(input('digite quanto vc tem na carteira? R$'))
dolar = real / 5.87
print('com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))