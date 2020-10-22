import numpy as np
import matplotlib.pyplot as plt

# DEL 1
def areOrthogonal(a, b):
    u = np.array(a)
    v = np.array(b)

    if np.dot(u, v) == 0:
        return True
    else:
        return False

# DEL 2
matrise = np.arange(1, 16)
matrise_reshaped = matrise.reshape(3, 5)
matrise_transposed = matrise_reshaped.transpose()
print(matrise_transposed)

# DEL 3
def EulerCromer(tmax, x0, y0, v0, u0, m, tau):
    # tmax er tiden jorden bruker rundt solen
    # x0 og y0 er startbetingelser for jordens posisjon
    # v0 og u0 er starbetingelser for farten til jorden
    # m er massen til jorden og tau er steglengden.

    N = int(round(tmax/tau))   #np.zeros(N) lager en liste bestående av bare 0ere av lengde N
    x = np.zeros(N)
    y = np.zeros(N)
    u = np.zeros(N)
    v = np.zeros(N)
    radiuser = np.zeros(N)

    # startbetingelser
    u[0] = u0
    v[0] = v0
    x[0] = x0
    y[0] = y0
    radiuser[0] = np.sqrt((x[0]) ** 2 + (y[0]) ** 2)

    for n in range(1, N):
        u[n] = u[n - 1] - 4 * np.pi ** 2 * x[n - 1] * tau / (radiuser[n - 1] ** 3)
        v[n] = v[n - 1] - 4 * np.pi ** 2 * y[n - 1] * tau / (radiuser[n - 1] ** 3)
        x[n] = x[n - 1] + u[n] * tau
        y[n] = y[n - 1] + v[n] * tau
        radiuser[n] = np.sqrt((x[n]) ** 2 + (y[n]) ** 2)


    return x, y  # posisjons- og farts-lister

# startbetingelser:
x0 = 1    # Tenk deg at solen er i origo og at jorden starter i posisjon(1,0)
y0 = 0
u0 = 0    # startfarten i x-retning er 0
v0 = 2*3.1415623   # startfarten i y-retning er 2*pi
m =  1 / 333480    # dette er massen til Jorden i forhold til massen til Solen
tmax = 1           # Omløpstiden rundt Solen er 1(år)
tau = 0.01         # denne skrittlengden er såpass liten at plottet blir fint nok

x1, y1 = EulerCromer(tmax, x0, y0, v0, u0, m, tau)

# Plotter banen til planeten rundt sola
plt.figure()
plt.plot(x1, y1)
circle = plt.Circle((0, 0), radius=0.06, fc='yellow')
plt.gca().add_patch(circle)
plt.xlabel(r'x [AU]')
plt.ylabel(r'y [AU]')
plt.show()
