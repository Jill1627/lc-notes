
public static int[][] rotate(int[][] matrix, int flag)
    {
        if(matrix == null || matrix.length == 0) return matrix;
        int m = matrix.length, n = matrix[0].length;
        int[][] res = new int[n][m];
        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < n; j++) res[j][i] = matrix[i][j];
        }
        if(flag == 1)
        {
            for(int i = 0; i < n; i++)
            {
                for(int j = 0; j < m / 2; j++)
                {
                    int tmp = res[i][j];
                    res[i][j] = res[i][m - 1 - j];
                    res[i][m - 1 - j] = tmp;
                }
            }
        }
        else
        {
            for(int j = 0; j < m ;j++)
            {
                for(int i = 0; i < n / 2; i++)
                {
                    int tmp = res[i][j];
                    res[i][j] = res[n - 1 - i][j];
                    res[n - 1 - i][j] = tmp;
                }
            }
        }
        return res;
    }
