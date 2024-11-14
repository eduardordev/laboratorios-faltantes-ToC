import Data.List (sortBy)
import Data.Ord (comparing)

d :: [ [(String, Either String Int)] ]
d = [ [("make", Left "Nokia"), ("model", Right 216), ("color", Left "Black")],
      [("make", Left "Apple"), ("model", Right 2), ("color", Left "Silver")],
      [("make", Left "Huawei"), ("model", Right 50), ("color", Left "Gold")],
      [("make", Left "Samsung"), ("model", Right 7), ("color", Left "Blue")] ]

sortD :: [ [(String, Either String Int)] ] -> [ [(String, Either String Int)] ]
sortD = sortBy (comparing (\x -> lookup "model" x))

nums :: [Int]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

powerList :: Int -> [Int] -> [Int]
powerList n = map (\x -> x ^ n)

x :: [[Int]]    
x = [[1, 2, 3, 1],
     [4, 5, 6, 0],
     [7, 8, 9, -1]]

transpose :: [[a]] -> [[a]]
transpose ([]:_) = []
transpose matrix = map head matrix : transpose (map tail matrix)

initialList :: [String]
initialList = ["rojo", "verde", "azul", "amarillo", "gris", "blanco", "negro"]

elementsToRemove :: [String]
elementsToRemove = ["amarillo", "café", "blanco"]

removeElements :: [String] -> [String] -> [String]
removeElements toRemove = filter (`notElem` toRemove)

import Data.Char (isPrint)

filterPrintable :: String -> String
filterPrintable = filter isPrint

main :: IO ()
main = do
    putStrLn "Ejercicio 1 - Lista ordenada:"
    putStrLn (filterPrintable (show (sortD d)))

    putStrLn "\nEjercicio 2 - Potencia n-ésima de la lista:"
    putStrLn (filterPrintable (show (powerList 3 nums)))

    putStrLn "\nEjercicio 3 - Matriz transpuesta:"
    putStrLn (filterPrintable (show (transpose x)))

    putStrLn "\nEjercicio 4 - Lista después de eliminar elementos:"
    putStrLn (filterPrintable (show (removeElements elementsToRemove initialList)))