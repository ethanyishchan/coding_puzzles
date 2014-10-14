#floyd-warshall

def floyd_warshall(M):
	n = len(M)
	for k in range (n):
		for i in range(n):
			for j in range (n):
				if M[i][k] + M[k][j] < M[i][k]:
					M[i][k] = M[i][k] + M[k][j]

	return M

#runtime is O(V^3)


def floyd_warhsall(M):

	min [for M[i][j] in ]



dij:
    0         if i = j
    w(i,j)   if (i,j) in E
    +inf     if (i,j) not in E and i != j