import numpy as np
import pandas as pd

arr3 = np.arange(1, 19).reshape(3, 2, 3)

scores = np.random.randint(30, 101, size=(3, 2, 4), dtype="int8")

studen_mean = scores.mean(axis=2)
print(studen_mean)
subject_mean = scores.mean(axis=(0, 1))
print(subject_mean)

for cls in range(scores.shape[0]):
    print(f"{cls + 1} 반")
    for student in range(scores.shape[1]):
        kor, eng, math, music = scores[cls][student]
        average = scores[cls][student].sum() / (scores.shape[2])
        print(f"{kor}, {eng}, {math}, {music}, avg : {average}")

a = np.array([[1, 2], [5, 3]])
b = np.array([[0, 1], [1, 0]])
print(a @ b)

inputdict = {
    "c_index": [1, 2, 3],
    "name": ["kim", "woo", "doo"],
    "address": ["dae", "jeon", "se"],
}
dict = pd.DataFrame(inputdict)
dict[dict["c_index"] > 2]["name"]
cpu_data = pd.read_excel("../data/cpu_usage_list.xlsx", engine="openpyxl")
cpu_data.tail(3)
cpu_data[cpu_data["Usage(%)"] > 1][["Date Time", "IP", "Hostname", "Usage(%)"]].count()

sample1 = np.array(["ab", "cde", "d"], dtype="<U2")
sample2 = np.arange(12, dtype="i2").reshape(4, 3)
print(sample2)
print(sample2.shape, sample2.ndim, sample2.dtype, sample2.itemsize, sample2.size)
