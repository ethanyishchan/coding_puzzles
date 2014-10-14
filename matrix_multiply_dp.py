def MM(i,j):
	if i = k:
		return 0

	return min (  MM (i,k) + MM (k+1 , j) + Cost (a[i][k] , a[k][j]) for k in range( i+1 , j) )