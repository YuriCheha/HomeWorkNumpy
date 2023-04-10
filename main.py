import numpy as np
data = np.random.randint(0, 100, (5, 5))
print(data)

A = np.random.randint(0, 10, size=(3, 3))
b = np.random.randint(0, 10, size=(3, 1))
x = np.linalg.solve(A, b)
print("Решение СЛАУ: ", x)
# det_A = np.linalg.det(A)
# A1 = np.hstack((b, A[:, 1:], A[:, 2:]))
# A2 = np.hstack((A[:, 0:1], b, A[:, 2:]))
# A3 = np.hstack((A[:, 0:2], b))
# x1 = np.linalg.det(A1) / det_A
# x2 = np.linalg.det(A2) / det_A
# x3 = np.linalg.det(A3) / det_A
# print(x1, x2, x3)
# x2 = np.linalg.tensorsolve(A, b)
# print(x2)
# x3 = np.linalg.lstsq(A, b)
# print(x3)


data = np.loadtxt("file2.csv")
v = np.var(data)
print("Дисперсия значений элементов массива")
print(v)
st_d = np.std(data)
print("Среднеквадратичное отклонение значений элементов массива")
print(st_d)
# x4 = np.linalg.lstsq(data)
# print("Наименьших квадратов для линейного матричного уравнения")
# print(x4)
print(np.histogram(data))