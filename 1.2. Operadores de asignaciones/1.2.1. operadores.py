## Operador =
## El operador igual a, (=), es el más simple de todos y asigna a la variable del lado izquierdo cualquier variable o resultado del lado derecho.
ejemplo = 123

## Operador +=
## El operador += suma a la variable del lado izquierdo el valor del lado derecho.
resultado = 5
resultado += 10
## En el ejemplo anterior si la variable “resultado” es igual a 5 y resultado += 10, entonces la variable “resultado” sera igual a 15. Su equivalente seria el siguiente:
resultado = 5
resultado = resultado + 10

## Operador -=
## El operador -= resta a la variable del lado izquierdo el valor del lado derecho.
resultado = 5
resultado -= 10
## En el ejemplo anterior si la variable “resultado” es igual a 5 y resultado -= 10, entonces la variable “resultado” sera igual a -5. Su equivalente seria el siguiente:
resultado = 5
resultado = resultado - 10

## Operador *=
## El operador *= multiplica a la variable del lado izquierdo el valor del lado derecho.
resultado = 5
resultado *= 10
## En el ejemplo anterior si la variable “resultado” es igual a 5 y resultado *= 10, entonces la variable “resultado” sera igual a 50. Su equivalente seria el siguiente:
resultado = 5
resultado = resultado * 10

## Operador /=
## El operador /= divide a la variable del lado izquierdo el valor del lado derecho.
resultado = 5
resultado /= 10
## En el ejemplo anterior si la variable “resultado” es igual a 5 y resultado /= 10, entonces la variable “resultado” sera igual a 0. Su equivalente seria el siguiente:
resultado = 5
resultado = resultado / 10

## Operador **=
## El operador **= calcula el exponente a la variable del lado izquierdo el valor del lado derecho.
resultado = 5
resultado **= 10
## En el ejemplo anterior si la variable “resultado” es igual a 5 y resultado **= 10, entonces la variable “resultado” sera igual a 9765625. Su equivalente seria el siguiente:
resultado = 5
resultado = resultado ** 10

## Operador //=
## El operador //= calcula la división entera a la variable del lado izquierdo el valor del lado derecho.
resultado = 5 
resultado //= 10
## En el ejemplo anterior si la variable “resultado” es igual a 5 y resultado //= 10, entonces la variable “resultado” sera igual a 0. Su equivalente seria el siguiente:
resultado = 5
resultado = resultado // 10

## Operador %=
## El operador %= devuelve el resto de la división a la variable del lado izquierdo el valor del lado derecho.
resultado = 5
resultado %= 10
## En el ejemplo anterior si la variable “resultado” es igual a 5 y resultado %= 10, entonces la variable “resultado” sera igual a 5. Su equivalente seria el siguiente:
resultado = 5
resultado = resultado % 10

## EJEMPLOS

a, b, c = 21, 10, 0

print "Valor de variable 'a':", a
print "Valor de variable 'b':", b

c = a + b
print "Operador = | El valor de variable 'c' es ", c

c += a
print "Operador += | El valor de variable 'c' es ", c

c *= a
print "Operador *= | El valor de variable 'c' es ", c

c /= a 
print "Operador /= | El valor de variable 'c' es ", c

c = 2
c %= a
print "Operador %= | El valor de variable 'c' es ", c

c **= a
print "Operador **= | El valor de variable 'c' es ", c

c //= a
print "Operador //= | El valor de variable 'c' es ", c