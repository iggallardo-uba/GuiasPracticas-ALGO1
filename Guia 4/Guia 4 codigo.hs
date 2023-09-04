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
f :: Integer -> Integer -> Integer
f x y = sumatoriaN x y

sumatoriaN :: Integer -> Integer -> Integer
sumatoriaN 1 _ = 1
sumatoriaN x y = sumatoriaM x y + sumatoriaN (x - 1) y

sumatoriaM :: Integer -> Integer -> Integer
sumatoriaM x 1 = x
sumatoriaM x y = x ^ y + sumatoriaM x (y - 1)

--Ejercicio 14
--sumaPotencias :: Integer -> Integer -> Integer -> Integer
--sumaPotencias x y z = x ^ (sumAyB y z)
--Ya no se me ocurrio, Asi que despues veo que se hace