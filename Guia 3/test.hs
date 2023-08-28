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
fog :: Integer -> Integer
fog x = f(g x)

gof :: Integer -> Integer
gof x = g(f x)

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

--E
ambosEs0 :: Integer -> Integer -> Bool
ambosEs0 x y = x == 0 && y == 0

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