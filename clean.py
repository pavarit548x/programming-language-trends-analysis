import pandas as pd
import json

# โหลดไฟล์
df = pd.read_csv("jobthai_programming_languages.csv")

# ลบ Vacancies
df = df.drop(columns=["Vacancies"])

# แปลง Date ให้เหลือเฉพาะ Year
df["Date"] = pd.to_datetime(df["Date"]).dt.year

# ลบข้อมูลซ้ำ
df = df.drop_duplicates()

# รวม Language ของ job เดียวกัน
grouped = (
    df.groupby(["URL", "Company", "Job Title", "Date"])["Language"]
    .apply(lambda x: list(set(x)))
    .reset_index()
)

# แปลงเป็น JSON
json_data = grouped.to_dict(orient="records")

with open("cleaned_jobs.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)

print("Done!")