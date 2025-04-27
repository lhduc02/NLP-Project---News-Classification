from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
df_final['label'] = label_encoder.fit_transform(df_final['category'])
