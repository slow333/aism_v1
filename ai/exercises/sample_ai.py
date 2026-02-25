from pprint import pprint
import pandas as pd
import requests
import matplotlib.pyplot as plt
from pathlib import Path

# api call
latitude = 48.85
longitude = 2.35
from datetime import datetime, timedelta

today = datetime.now()
td_week = timedelta(days=7)
week_ago = today - td_week
start = week_ago.strftime("%Y-%m-%d")
end = today.strftime("%Y-%m-%d")

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start}&end_date={end}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
daily_data = data["daily"]

# data frame: Pandas
df = pd.DataFrame(
    {
        "date": daily_data["time"],
        "max": daily_data["temperature_2m_max"],
        "min": daily_data["temperature_2m_min"],
    }
)
df["date"] = pd.to_datetime(df["date"])
df["avg"] = (df["max"] + df["min"]) / 2

output_path_csv = Path("data/weather.csv")
output_path_csv.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path_csv)

# graphic : Matplotlib
# print(plt.style.available)
# plt.style.use('fivethirtyeight')
# 한글 폰트 설정 (Windows: Malgun Gothic, Mac: AppleGothic, Linux: NanumGothic)
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

plt.figure(figsize=(10, 6))
plt.plot(df["date"], df["max"], "r-o", label="Max Temp")
plt.plot(df["date"], df["min"], "b-o", label="Min Temp")
plt.plot(df["date"], df["avg"], "g--", label="Average Temp")
plt.title("일주일간 온도 변화")
plt.xlabel("Temperature (°C)")
plt.ylabel("온도")
# style에서 기본적으로 가져옮
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()

output_path_img = Path("images/my_plot.png")
output_path_img.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path_img)
plt.show()
