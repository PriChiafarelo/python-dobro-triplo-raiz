"""Crie um algorítmo que leia um número e mostre o seu dobro, o seu triplo e raiz quadrada"""
numero = float(input('Digite um número: '));
print('O dobro de {} é {}'.format(numero,numero * 2), 'o triplo {}'.format(numero * 3), 'e a raiz quadrada é {:.2f}'.format(numero **(1/2)))