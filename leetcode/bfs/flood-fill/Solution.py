class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        rl: int = len(image)
        cl: int = len(image[0])
        col: int = image[sr][sc]
        
        map: List[List[bool]] = [[False for _ in range(len(image[0]))] for _ in range(len(image))]

        indices: List[List[int]] = list()
        indices.append([sr, sc])

        while len(indices) != 0:

            (i, j) = indices.pop()

            if i >= 0 and i < rl and j >= 0 and j < cl and not map[i][j] and image[i][j] == col:
                map[i][j] = True
                image[i][j] = color

                indices.append([i + 1, j])
                indices.append([i - 1, j])
                indices.append([i, j - 1])
                indices.append([i, j + 1])

        return image