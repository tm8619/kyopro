def floor_sum(N, M, A, B):
    ans = 0
    while True:
        ans += (A//M)*(N-1)*N//2 + (B//M)*N
        A, B = A%M, B%M
        if A*N+B < M:
            return ans
        ymax = (N*A+B)//M
        xmax = -((B-M*ymax)//A)
        ans += (N-xmax)*ymax
        A, B, N, M = M, A*xmax-M*ymax+B, ymax, A
