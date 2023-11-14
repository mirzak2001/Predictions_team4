from sklearn.preprocessing import normalize
import numpy as np
from scipy import stats


class Combs:
    def __init__(self, L, kmax):
        self.kmax = kmax
        self.L = L - 1

    def __iter__(self):
        self.dat = [1 for i in range(self.L)]
        return self
    
    def __next__(self):
        x = self.dat[:]
        i = self.L - 1
        while (self.dat[i] >= self.kmax):
            i -= 1
            if i < 0 and x == [self.kmax for i in range(self.L)]:
                self.dat[0] += 1
                return x
            if i < 0:
                raise StopIteration
        self.dat[i] += 1
        for i in range(i+1, self.L):
            self.dat[i] = 1
        return x


def dist(a, b):
    return np.linalg.norm(a-b)


def AvgS(s):
    return np.mean(s)


def wAvg(s):


def modeS(s):
    return stats.mode(s)


def predict(Y1, h, func):
    eps = 0.01
    y = normalize(Y1)
    t = len(Y1)
    for i in range(1, h+1):
        w1 = []
        w2 = []
        S = []
        L = 4
        kmax = 10
        combs = Combs(L, kmax)
        combins = iter(combs)
        for alpha in combins:
            eta_alpha = [t for i in range(L + 1)]
            for l in range(1, L + 1):
                if l == 1:
                    eta_alpha[l] = y[t]
                else:
                    idx = t
                    for z in range(2, l + 1):
                        idx -= alpha[L - i + 1]
                    eta_alpha[l] = y[idx]
            C_alpha = eta_alpha
            C = [t + i for z in range(1, L)]
            for z in range(1, L):
                zx = 0
                for zxc in range(L-1, z-1, -1):
                    zx += alpha[zxc-1]
                C[z] -= zx
            trunc_C_alpha = C_alpha[:-1]
            if dist(C, trunc_C_alpha) < eps:
                S.append(eta_alpha[L])
                w2.append((eps - dist(C, trunc_C_alpha)) / eps)
                w1.append()
        if predictable(t+i):                ##NEED IMPLEMENTATION
            y[t+i] = func(S)





t = 100
L = 10
kmax = 10
combs = Combs(L, kmax)
combins = iter(combs)
for alpha in combins:
    eta_alpha = [0 for i in range(L)]
    for l in range(1, L + 1):
        idx = t
        for index in range(1, t):
            idx -= alpha[index]