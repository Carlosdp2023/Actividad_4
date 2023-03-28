#Conversión de temperaturas.
c = float(input('Ingrese la temperatura en grados Celcius: '))
f = ((9/5)*c) + 32
r = ((c*1.8) + 491.67)
k = c + 273.15

print(c, 'es equuivalente a',f,'grados fahrenheit')
print(c, 'es equuivalente a',r,'grados Rankine')
print(c, 'es equuivalente a',k,'grados Kelvin')