data_0 = [2,3]
data_1 = [4,5]

data_2D = [data_0,data_1,9]
data_2D_copy = data_2D.copy()

print(f"data={data_2D}")
print(f"data copy={data_2D_copy}")

#cara mengambil data di nedted list

data = [data_2D[0][0]]
print(f"data={data}")

#all address

print(f"address asli = {hex(id(data_2D))}")
print(f"address copy = {hex(id(data_2D_copy))}")

print("addrees dari member ke-1")

print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address copy = {hex(id(data_2D_copy[0]))}")


data_2D[0][1] = 7
data_2D [1] = 8
print(f"data={data_2D}")
print(f"data copy={data_2D_copy}")

print("----------------batas----------------")
#menggunakan deepcopy pada nested list

from copy import deepcopy

data_2D = [data_0,data_1,9]
data_2D_deepcopy = deepcopy(data_2D)

print(f"address asli = {hex(id(data_2D))}")
print(f"address deep = {hex(id(data_2D_deepcopy))}")

print("addrees dari member ke-1")

print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address copy = {hex(id(data_2D_deepcopy[0]))}")


data_2D[0][1] = 15
print(f"data={data_2D}")
print(f"data copy={data_2D_copy}")
print(f"data deep={data_2D_deepcopy}")