import os
import pandas as pd

# Set up
pd.set_option('display.max_colwidth', None)

script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, "..", "data", "news_data.json")
print(data_path)

# Đọc và chuẩn hóa lại dữ liệu
df = pd.read_json(data_path)

df = df.drop_duplicates(subset=['title', 'short_description'])

# Ghép các trường 'title', 'short_description' và 'content' thành một trường duy nhất 'text'
df['text'] = df['title'] + " " + df['short_description'] + " " + df['content']

# Kiểm tra dữ liệu sau khi ghép
df_final = df[['text', 'category']]

print(df_final['text'].head(1))


