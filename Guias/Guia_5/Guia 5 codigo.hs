--FUNCIONES AUXILIARES PRIMOS
esPrimo :: Integer -> Bool
esPrimo x | busquedaDivisorEsPrimo x 2 == True = True
          | otherwise = False

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
longitud x = 1 + longitud (tail x)

--2
ultimo :: [t] -> t
ultimo (x : xs) | longitud xs == 0 = x
                | otherwise = ultimo xs

--3
principio :: (Num t) => [t] -> [t]
principio x | longitud x == 0 = [0,0,0]
            | longitud x == 1 = [head x, 0, head x]
            | otherwise = [head x, 0, ultimo x]

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
todosIguales [] = True
todosIguales (x : xs) | longitud xs == 0 = True
                      | x /= head xs = False
                      | otherwise = todosIguales xs

--3
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos (x : xs) | longitud xs == 0 = True
                        | pertenece x xs == True = False
                        | otherwise = todosDistintos xs
                                            
--4
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x : xs) | pertenece x xs == True = True
                      | otherwise = hayRepetidos xs


--5
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar x (y : ys) | x == y = ys
                  | otherwise = y : (quitar x ys)

--6
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos x (y : ys) | x == y = quitarTodos x ys
                       | otherwise = y : (quitarTodos x ys)

--7

--Ejercicio 3
--1
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x : xs) = x + sumatoria xs

--2
productoria :: [Integer] -> Integer
productoria [] = 1
productoria (x : xs) = x * productoria xs

--3
maximo :: [Integer] -> Integer
maximo (x : xs) = calcularMaximo xs x

calcularMaximo :: [Integer] -> Integer -> Integer
calcularMaximo [] x = x
calcularMaximo (x : xs) y | x > y = calcularMaximo xs x
                          | otherwise = calcularMaximo xs y

--4
sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN x (y : ys) = (y + x) : (sumarN x ys)

--5
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero [] = []
sumarElPrimero x = sumarN (head x) x

--6
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo [] = []
sumarElUltimo x = sumarN (ultimo x) x

--7
pares :: [Integer] -> [Integer]
pares [] = []
pares (x : xs) | mod x 2 == 0 = x : pares xs
               | otherwise = pares xs

--8
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN x (y : ys) | mod y x == 0 = y : multiplosDeN x ys
                        | otherwise = multiplosDeN x ys

--9
ordenar :: [Integer] -> [Integer]
ordenar x = calcularOrdenar x []

calcularOrdenar :: [Integer] -> [Integer] -> [Integer]
calcularOrdenar [] y  = y
calcularOrdenar x y = calcularOrdenar (quitar (maximo x) x) (maximo x : y)

--Ejercicio 5
--1
sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada x = calcularSumaAcumulada 0 x

calcularSumaAcumulada :: (Num t) => t -> [t] -> [t]
calcularSumaAcumulada _ [] = []
calcularSumaAcumulada x (y : ys) = calcularSumaAcumulada x + y

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