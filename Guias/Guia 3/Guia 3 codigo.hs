--Ejemplo Clase

doubleMe x = x + x

--EJERCICIO 1

--A
f :: Integer -> Integer
f 1 = 8
f 4 = 131
f 16 = 16

--B
g :: Integer -> Integer
g 8 = 16
g 16 = 16
g 131 = 1

--C
h :: Integer -> Integer
h x = f(g x)

k :: Integer -> Integer
k x = g(f x)

--EJERCICIO 2

--A
absoluto :: Integer -> Integer
absoluto x | x < 0 = x*(-1)
           | otherwise = x
--B
maximoabsoluto :: Integer -> Integer -> Integer
maximoabsoluto x y | absoluto x > absoluto y = absoluto x
                   | otherwise = absoluto y
--C
maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 x y z | x > y && x > z = x
              | y > x && y > z = y
              | otherwise = z
--D
algunoEs0 :: Integer -> Integer -> Bool
algunoEs0 x y = x == 0 || y == 0

algunoEs0PM :: Integer -> Integer -> Bool --Con Pattern Maching
algunoEs0PM 0 _ = True
algunoEs0PM _ 0 = True
algunoEs0PM _ _ = False


--E
ambosEs0 :: Integer -> Integer -> Bool
ambosEs0 x y = x == 0 && y == 0

ambosEs0PM :: Integer -> Integer -> Bool --Con Pattern Maching
ambosEs0PM 0 0 = True
ambosEs0PM _ _ = False

--F
mismoIntervalo :: Integer -> Integer -> Bool
mismoIntervalo x y | x <= 3 && y <= 3 = True
                   | x > 7 && y > 7 = True
                   | x > 3 && x <= 7 && y > 3 && y <= 7 = True
                   | otherwise = False

--G
sumaDistintos :: Integer -> Integer -> Integer -> Integer 
sumaDistintos x y z | x == y && x == z = 0
                    | x == y && x /= z = x + z
                    | x /= y && x == z = x + y
                    | y == x && y /= z = y + z
                    | y /= x && y == z = y + x
                    | otherwise = x + y + z

--H
esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe x y | mod x y == 0 = True
                 | otherwise = False

--I
digitoUnidades :: Integer -> Integer
digitoUnidades x = mod x 10

--J
digitoDecenas :: Integer -> Integer
digitoDecenas x = div (mod x 100) 10

--EJERCICIO 3 
--Revisa el ejercicio y no te fijes tanto en la especificacion
estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados x y | mod x y == 0 = True
                      | otherwise = False

--EJERCICIO 4

--A
prodInt :: (Integer, Integer) -> Integer
prodInt (x,y) = x * y

--B
todoMenor :: (Integer, Integer) -> (Integer, Integer) -> Bool
todoMenor (x,y) (i,j) | x < i && y < j = True
                      | otherwise = False

--C
distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float
distanciaPuntos (x,y) (i,j) = sqrt ((i-x)*(i-x)+(j-y)*(j-y))

--D
sumaTerna :: (Integer, Integer, Integer) -> Integer
sumaTerna (x,y,z) = x+y+z

 --E
sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (x,y,z) i | esMultiploDe x i && esMultiploDe y i && esMultiploDe z i = sumaTerna(x,y,z)
                             | esMultiploDe x i && esMultiploDe y i = x + y
                             | esMultiploDe y i && esMultiploDe z i = y + z
                             | esMultiploDe x i && esMultiploDe z i = z + y
                             | esMultiploDe x i = x
                             | esMultiploDe y i = y
                             | esMultiploDe z i = z
                             | otherwise = 0

--F
posPrimerPar :: (Integer, Integer, Integer) -> Integer
posPrimerPar (x,y,z) | esPar x = 1
                     | esPar y = 2
                     | esPar z = 3
                     | otherwise = 4

--FA (Funcion Auxiliar)
esPar :: Integer -> Bool
esPar x | esMultiploDe x 2 = True
        | x == 0 = True
        | otherwise = False

--G y --H
--Como que elementos de cualquier Tipo?
--Ignoras la sintaxis de Tipos y dejas que Haskell lo opere

--G
crearPar :: a -> b -> (a,b)
crearPar x y =  (x,y)

--H
invertir :: (a,b) -> (b,a)
invertir (x,y) = (y,x)

--Ejercicio 5
todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (x, y, z) | esMayor (f1 x) (g1 x) && esMayor (f1 y) (g1 y) && esMayor (f1 z) (g1 z) = True
                     | otherwise = False

f1 :: Integer -> Integer
f1 x | x <= 7 = x * x
     | otherwise= 2 * x - 1

g1 :: Integer -> Integer
g1 x | esPar x = div x 2
     | otherwise = 3 * x + 1

--FA
esMayor :: Integer -> Integer -> Bool
esMayor x y | x > y = True
            | otherwise = False

--Ejercicio 6
bisiesto :: Integer -> Bool
bisiesto x | not(esMultiploDe x 4) || esMultiploDe x 100 && not(esMultiploDe x 400) = False   
           | otherwise = True

--Ejercicio 7
distanciaManhattan:: (Float, Float, Float) ->(Float, Float, Float) ->Float
distanciaManhattan (x,y,z) (i,j,k) = absolutoFloat (x-i) + absolutoFloat (y-j) + absolutoFloat (z-k)

--FA
absolutoFloat :: Float -> Float
absolutoFloat x | x < 0 = x*(-1)
                | otherwise = x

--Ejercicio 8
comparar :: Integer -> Integer -> Integer
comparar x y | sumaUltimosDosDigitos x < sumaUltimosDosDigitos y = 1
             | sumaUltimosDosDigitos x > sumaUltimosDosDigitos y = -1
             | sumaUltimosDosDigitos x == sumaUltimosDosDigitos y = 0

sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos x = mod x 10 + mod (div x 10) 10