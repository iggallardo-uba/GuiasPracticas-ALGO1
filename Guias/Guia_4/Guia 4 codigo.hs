--Guin N°4 - Recursion 

--Ejercicio 1
fibonacci :: Integer -> Integer
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n-1) + fibonacci (n-2)

--Ejercicio 2
parteEntera :: Float -> Integer
parteEntera x | 0 <= x && x < 1 = 0
              | otherwise = 1 + parteEntera (x-1)

--Para los negativos

parteEnteraCompleto :: Float -> Integer
parteEnteraCompleto x | 0 <= x && x < 1 = 0
                      | -1 < x && x <= 0 = -1
                      | x >= 1 = 1 + parteEntera (x-1) 
                      | otherwise = (-1) + parteEntera (x+1)
                      --Chequear no funca 

--Ejercicio 3
esDivisible :: Integer -> Integer -> Bool
esDivisible x y | x > 0 = esDivisible (x-y) y
                | x == 0 = True
                | x < 0 = False

--Ejercicio 4
sumaImpares :: Integer -> Integer
sumaImpares x | x == 1 = 1
              | otherwise = 1 + 2 * (x-1) + sumaImpares (x-1) 

--Ejercicio 5
medioFact :: Integer -> Integer
medioFact x | x == 0 = 1
            | x == 1 = 1
            | otherwise = x * medioFact (x-2)

--Ejercicio 6
sumaDigitos :: Integer -> Integer
sumaDigitos 0 = 0
sumaDigitos x = mod x 10 + sumaDigitos (div x 10)

--Ejercicio 7
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales x | x < 10 = True
                      | otherwise = (ultimoDigito x == ultimoDigito (sacarUltimoDigito x) && todosDigitosIguales (sacarUltimoDigito x))

--FA
ultimoDigito :: Integer -> Integer
ultimoDigito x = mod x 10

sacarUltimoDigito :: Integer -> Integer
sacarUltimoDigito x = div x 10

--Ejercicio 8
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito 0 _ = 1
iesimoDigito x y = ultimoDigito(div x (10^(cantDigitos x - y)))

cantDigitos :: Integer -> Integer
cantDigitos 0 = 0
cantDigitos x = 1 + cantDigitos(sacarUltimoDigito x)

--Ejercicio 9
esCapicua :: Integer -> Bool
esCapicua x | x == 0 = True
            | cantDigitos x == 1 = True
            | otherwise = (((primerDigito x) == (ultimoDigito x)) && esCapicua (sacarExtremos x))

--FA
primerDigito :: Integer -> Integer
primerDigito x = div x (10^((cantDigitos x) - 1))

sacarPrimerDigito :: Integer -> Integer
sacarPrimerDigito x = mod x (10^((cantDigitos x) - 1))

sacarExtremos :: Integer -> Integer
sacarExtremos x = sacarUltimoDigito (sacarPrimerDigito x)

--Ejercicio 10
--A
f1 :: Integer -> Integer
f1 x | x == 0 = 1 
     | otherwise = 2^x + f1 (x-1)

--B
f2 :: Integer -> Integer -> Integer
f2 0 y = 1
f2 x y = (y ^ x) + f2 (x - 1) y

--C
f3 :: Integer -> Integer -> Integer
f3 0 y = 1
f3 x y = (y ^ (2 * x)) + f2 ((2 * x)-1) y

--D
f4 :: Integer -> Integer -> Integer
f4 x y = f3 x y - f2 x y 

--Ejercicio 11
--A
eAprox :: Integer -> Float
eAprox 0 = 1
eAprox x = 1/(factorial (fromIntegral x)) + eAprox(x - 1)

factorial :: Float -> Float
factorial 0 = 1
factorial 1 = 1
factorial x = x * factorial (x - 1)

--B
--Ni idea como se define una variable jajas

--Ejercicio 12
raizDe2Aprox :: Integer -> Float
raizDe2Aprox x = (sucesionN (fromIntegral x)) - 1

sucesionN :: Float -> Float
sucesionN 1 = 2
sucesionN x = 2 + 1/(sucesionN (x - 1))

--Ejercicio 13
funcion13 :: Integer -> Integer -> Integer
funcion13 x y = sumatoriaN13 x y

sumatoriaN13 :: Integer -> Integer -> Integer
sumatoriaN13 1 _ = 1
sumatoriaN13 x y = sumatoriaM13 x y + sumatoriaN13 (x - 1) y

sumatoriaM13 :: Integer -> Integer -> Integer
sumatoriaM13 x 1 = x
sumatoriaM13 x y = x ^ y + sumatoriaM13 x (y - 1)

--Ejercicio 14
--sumaPotencias :: Integer -> Integer -> Integer -> Integer
--sumaPotencias x y z = x ^ (sumAyB y z)
--No se me ocurrio, Asi que despues veo que se hace

--Ejercicio 15
funcion15 :: Integer -> Integer -> Float
funcion15 x y = sumatoriaN15 (fromIntegral x) (fromIntegral y) 

sumatoriaN15 :: Float -> Float -> Float
sumatoriaN15 1 y = sumatoriaM15 1 y
sumatoriaN15 x y = sumatoriaM15 x y + sumatoriaN15 (x - 1) y

sumatoriaM15 :: Float -> Float -> Float
sumatoriaM15 x 1 = x
sumatoriaM15 x y = x/y + sumatoriaM15 x (y - 1)

--Ejercicio 16
--A
menorDivisor :: Integer -> Integer
menorDivisor x = busquedaDivisorDesde x 2

--FA
busquedaDivisorDesde :: Integer -> Integer -> Integer
busquedaDivisorDesde x y | mod x y == 0 = x
                         | otherwise = busquedaDivisorDesde x (y + 1)

--B
esPrimo :: Integer -> Bool
esPrimo x | busquedaDivisorEsPrimo x 2 == True = True
          | otherwise = False

--FA
busquedaDivisorEsPrimo :: Integer -> Integer -> Bool
busquedaDivisorEsPrimo x y | x == y = True
                           | mod x y == 0 = False
                           | otherwise = busquedaDivisorEsPrimo x (y + 1)

--C
sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos x y | divisoresCoprimosoprimos x y 2 == True = True
                | otherwise = False

--FA
divisoresCoprimosoprimos :: Integer -> Integer -> Integer -> Bool
divisoresCoprimosoprimos x y z | mod x y == 0 = False
                               | mod y x == 0 = False
                               | x == z || y == z = True
                               | mod x z == 0 && mod y z == 0 = False
                               | otherwise = divisoresCoprimosoprimos x y (z + 1) 

--D
nEsimoPrimo :: Integer -> Integer
nEsimoPrimo x = calculoNEsimoPrimo x 1 2 

--FA
calculoNEsimoPrimo :: Integer -> Integer -> Integer -> Integer
calculoNEsimoPrimo x y p | x == y = p
                         | otherwise = calculoNEsimoPrimo x (y+1) (calculoSigPrimo p)  

calculoSigPrimo :: Integer -> Integer
calculoSigPrimo x | esPrimo (x + 1) == True = x + 1
                  | otherwise = calculoSigPrimo (x + 1)

--Ejercicio 17
esFibonacci :: Integer -> Bool
esFibonacci x = calculoEsFibonacci x 1

calculoEsFibonacci :: Integer -> Integer -> Bool
calculoEsFibonacci x y | x == fibonacci y = True
                       | x < fibonacci y = False
                       | otherwise = calculoEsFibonacci x (y + 1)

--Ejercicio 18
mayorDigitoPar :: Integer -> Integer
mayorDigitoPar x = calculoMayorDigitoPar x (-1)

--FA
esPar :: Integer -> Bool
esPar x | mod x 2 == 0 = True
        | otherwise = False

calculoMayorDigitoPar :: Integer -> Integer -> Integer
calculoMayorDigitoPar x y | x == 0 = y 
                          | esPar (mod x 10) == True && mod x 10 > y = calculoMayorDigitoPar (div x 10) (mod x 10)
                          | otherwise = calculoMayorDigitoPar (div x 10) y

--Ejercicio 19
esSumaInicialDePrimos :: Integer -> Bool
esSumaInicialDePrimos x = esSumaInicialDeKPrimos x 1

--FA
esSumaInicialDeKPrimos :: Integer -> Integer -> Bool
esSumaInicialDeKPrimos x y | x == sumaKPrimos y = True
                           | x < sumaKPrimos y = False
                           | otherwise = esSumaInicialDeKPrimos x (y + 1)

sumaKPrimos :: Integer -> Integer
sumaKPrimos x | x == 1 = 2
              | otherwise = nEsimoPrimo x + sumaKPrimos (x - 1) 

--Ejercicio 20
tomaValorMax :: Integer -> Integer -> Integer
tomaValorMax x y = calculoTomaValorMax x y x 0

--FA
calculoTomaValorMax :: Integer -> Integer -> Integer -> Integer -> Integer
calculoTomaValorMax x y z c | z > y = c 
                            | sumaDivisores z z > c = calculoTomaValorMax x y (z + 1) (sumaDivisores z z)
                            | otherwise = calculoTomaValorMax x y (z + 1) c

sumaDivisores :: Integer -> Integer -> Integer
sumaDivisores x y | y == 1 = 1
                  | mod x y == 0 = y + sumaDivisores x (y - 1) 
                  | otherwise = sumaDivisores x (y - 1)

--Ejercicio 21
pitagoras :: Integer -> Integer -> Integer -> Integer
pitagoras x y z = calculoPitagoras x y z 0 0 0

calculoPitagoras :: Integer -> Integer -> Integer -> Integer -> Integer -> Integer -> Integer
calculoPitagoras x y z c k j | j > y = c
                             | k > x = calculoPitagoras x y z c 0 (j + 1)
                             | (k ^ 2) + (j ^ 2) <= (z ^ 2) = calculoPitagoras x y z (c + 1) (k + 1) j
                             | otherwise = calculoPitagoras x y z c (k + 1) j