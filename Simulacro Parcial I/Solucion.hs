module Solucion where

--1
relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True
relacionesValidas ((x1, x2) : xs) 
 | x1 == x2 = False
 | pertenece (x1, x2) xs == True = False
 | otherwise = relacionesValidas xs

--FA
reverso :: (String, String) -> (String, String)
reverso (x1, x2) = (x2, x1)

pertenece :: (String, String) -> [(String, String)] -> Bool
pertenece _ [] = False
pertenece (x1, x2) ((y1, y2) : ys) 
 | (y1, y2) == (x1, x2) = True
 | reverso (x1, x2) == (y1, y2) = True
 | otherwise = pertenece (x1, x2) ys

--2
personas :: [(String, String)] -> [String]
personas x = eliminarRepetidos (listaPersonas x)

--FA
listaPersonas :: [(String, String)] -> [String]
listaPersonas [] = []
listaPersonas ((x1, x2) : xs) = x1 : x2 : listaPersonas xs

eliminarRepetidos :: [String] -> [String]
eliminarRepetidos [] = []
eliminarRepetidos (x : xs) 
 | perteneceString x xs == True = x : eliminarRepetidos (quitarTodos x xs)
 | otherwise = x : eliminarRepetidos xs

perteneceString :: String -> [String] -> Bool
perteneceString _  [] = False
perteneceString x (y : ys)
 | x == y = True
 | otherwise = perteneceString x ys

quitarTodos :: String -> [String] -> [String]
quitarTodos _ [] = []
quitarTodos x (y : ys) 
 | x == y = ys
 | otherwise = y : (quitarTodos x ys)

--3
amigosDe :: String -> [(String, String)] -> [String]
amigosDe _ [] = []
amigosDe x ((y1, y2) : ys)
 | x == y1 = y2 : amigosDe x ys
 | x == y2 = y1 : amigosDe x ys
 | otherwise = amigosDe x ys

--4
personaConMasAmigos :: [(String, String)] -> String
personaConMasAmigos rel = personaConMasAmigosAux rel (personas rel)

personaConMasAmigosAux :: [(String, String)] -> [String] -> String
personaConMasAmigosAux rel [x] = x
personaConMasAmigosAux rel (x : (y : ys))
 | 

--funcAux :: [(String, String)] -> [String] -> [Integer] -> [Integer]
--funcAux [] x y =  y --maximo x y "" 0
--funcAux ((x1, x2) : xs) y z 
-- | perteneceString x1 y == True && perteneceString x2 y == True 
--  = funcAux xs y (sumarPersonas y z x1 x2) 

-- | perteneceString x1 y == False && perteneceString x2 y == True 
--  = funcAux xs (x1 : y) (sumarPersonas (x1 : y) (0 : z) x1 x2) 

-- | perteneceString x1 y == True && perteneceString x2 y == False 
--  = funcAux xs (x2 : y) (sumarPersonas (x2 : y) (0 : z) x1 x2) 

-- | perteneceString x1 y == False && perteneceString x2 y == False 
--  = funcAux xs (x2 : x1 : y) (sumarPersonas (x2 : x1 : y) (0 : 0 : z) x1 x2) 

--sumarPersonas :: [String] -> [Integer] -> String -> String -> [Integer]
--sumarPersonas [] [] i j = []
--sumarPersonas (x: xs) (y: ys) i j 
-- | x == j = (y+1) : sumarPersonas xs ys i j
-- | x == i = (y+1) : sumarPersonas xs ys i j
-- | otherwise = (y+1) : sumarPersonas xs ys i j

--maximo :: [String] -> [Integer] -> String -> Integer -> String
--maximo [] [] i j = i
--maximo [] (x : xs) i j = "String Vacio"
--maximo (x: xs) [] i j = "Integer vacia"
--maximo (x : xs) (y : ys) "" 0 = maximo xs ys x y
--maximo (x : xs) (y : ys) i j 
-- | y > j = maximo xs ys x y
-- | y == j = maximo xs ys x y
-- | otherwise = maximo xs ys i j
