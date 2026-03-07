import pandas as pd
import matplotlib.pyplot as plt
import kagglehub  # noqa: E402

# 한글 폰트 설정 (Windows: Malgun Gothic, Mac: AppleGothic, Linux: NanumGothic)
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# Download latest version
path = kagglehub.dataset_download("heptapod/titanic")

print("Path to dataset files:", f"{path}\\train_and_test2.csv")
titanic = pd.read_csv(f"{path}\\train_and_test2.csv")
titanic["Servived"] = titanic["2urvived"]
# print(titanic.info())
parch_counts = titanic.groupby("Parch")["Servived"].value_counts().unstack().fillna(0)
# print(parch_counts)
x = parch_counts.index.astype(str)
y1 = parch_counts[0].values
y2 = parch_counts[1].values
plt.figure(figsize=(10, 10))
plt.subplot(2, 1, 1)
plt.plot(x, y1, # type: ignore
    marker="o", linestyle="-", color="indigo",
    markersize=7, linewidth=3,
    alpha=0.7, label="Die",
)
plt.xlabel("Parch")
plt.ylabel("Not Survived Count", color="indigo")
plt.tick_params(axis="y", labelcolor="indigo")
plt.legend(loc="upper right")

plt.subplot(2, 1, 2)
plt.bar(x, y2,# type: ignore
    color="deeppink", width=0.5, alpha=0.7,
    label="Survived",
)
plt.xlabel("Parch")
plt.ylabel("Survived Count", color="deeppink")
plt.tick_params(axis="y", labelcolor="deeppink")
plt.legend(loc="upper right")

plt.suptitle("타이타닉에서 애들, 부보 수에 따른 분석")
plt.tight_layout()
plt.show()
