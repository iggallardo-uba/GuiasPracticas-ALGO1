--FUNCIONES AUXILIARES PRIMOS
esPrimo :: Integer -> Bool
esPrimo x | busquedaDivisorEsPrimo x 2 == True = True
          | otherwise = False

--FA
busquedaDivisorEsPrimo :: Integer -> Integer -> Bool
busquedaDivisorEsPrimo x y | x == y = True
                           | mod x y == 0 = False
                           | otherwise = busquedaDivisorEsPrimo x (y + 1)

nEsimoPrimo :: Integer -> Integer
nEsimoPrimo x = calculoNEsimoPrimo x 1 2 

calculoNEsimoPrimo :: Integer -> Integer -> Integer -> Integer
calculoNEsimoPrimo x y p | x == y = p
                         | otherwise = calculoNEsimoPrimo x (y+1) (calculoSigPrimo p)  

calculoSigPrimo :: Integer -> Integer
calculoSigPrimo x | esPrimo (x + 1) == True = x + 1
                  | otherwise = calculoSigPrimo (x + 1)

--Ejercicio 1
--1
longitud :: [t] -> Integer
longitud [] = 0
longitud (x : xs) = 1 + longitud xs

--2
ultimo :: [t] -> t
ultimo (x : xs) | longitud xs == 0 = x
                | otherwise = ultimo xs

--3
principio :: (Num t) => [t] -> [t]
principio (x : xs) = [x, 0, ultimo xs]

--4
reverso :: (Eq t) => [t] -> [t]
reverso x = calcularReverso x []

calcularReverso :: (Eq t) => [t] -> [t] -> [t]
calcularReverso [] y = y
calcularReverso (x : xs) y = calcularReverso xs (x : y)

--Ejercicio 2
--1
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece x (y : ys) | y == x = True
                     | otherwise = pertenece x ys

--2
todosIguales :: (Eq t) => [t] -> Bool
todosIguales (x : xs) = calculoTodosIguales xs x

calculoTodosIguales :: (Eq t) => [t] -> t -> Bool
calculoTodosIguales [] _ = True
calculoTodosIguales (x : xs) y | x /= y = False
                               | otherwise = calculoTodosIguales xs y

--3
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos (x : xs) =  calculoTodosDistintos xs x

calculoTodosDistintos :: (Eq t) => [t] -> t -> Bool
calculoTodosDistintos [] _ = True
calculoTodosDistintos x y | pertenece y x == True = False
                          | otherwise = calculoTodosDistintos (tail x) (head x)
                                            
--4
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos x = calculoHayRepetidos x

calculoHayRepetidos :: (Eq t) => [t] -> Bool
calculoHayRepetidos [] = False
calculoHayRepetidos (x : xs) | pertenece x xs == True = True
                             | otherwise = calculoHayRepetidos xs

--5
quitar :: (Eq t) => t -> [t] -> [t]
quitar x y = calcularQuitar x y [] 0

calcularQuitar :: (Eq t) => t -> [t] -> [t] -> Integer -> [t]
calcularQuitar _ [] z _ = z
calcularQuitar _ y z 1 = y ++ z
calcularQuitar x (y : ys) z c | x == y = calcularQuitar x ys z 1
                              | otherwise = calcularQuitar x ys (y : z) 0

--Ejercicio 3
--1

--2

--3
maximo :: [Integer] -> Integer
maximo (x : xs) = calcularMaximo xs x

calcularMaximo :: [Integer] -> Integer -> Integer
calcularMaximo [] x = x
calcularMaximo (x : xs) y | x > y = calcularMaximo xs x
                          | otherwise = calcularMaximo xs y

--9
ordenar :: [Integer] -> [Integer]
ordenar x = calcularOrdenar x []

calcularOrdenar :: [Integer] -> [Integer] -> [Integer]
calcularOrdenar [] y  = y
calcularOrdenar x y = calcularOrdenar (quitar (maximo x) x) (maximo x : y)

--Ejercicio 5
--1

--2
descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x : xs) = descomponerEnPrimosElemento x [] 1 : descomponerEnPrimos xs

descomponerEnPrimosElemento :: Integer -> [Integer] -> Integer -> [Integer]
descomponerEnPrimosElemento 1 y _ = y
descomponerEnPrimosElemento 2 y _ = 2 : y
descomponerEnPrimosElemento x y c | esPrimo x = descomponerEnPrimosElemento 1 (x : y) c 
                                  | mod x (nEsimoPrimo c) == 0 = descomponerEnPrimosElemento (div x (nEsimoPrimo c)) ((nEsimoPrimo c) : y) 1 
                                  | otherwise = descomponerEnPrimosElemento x y (c + 1)