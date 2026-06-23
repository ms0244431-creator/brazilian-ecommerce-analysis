import pandas as pd

orders_df = pd.read_csv("olist_orders_dataset.csv")
payments_df = pd.read_csv("olist_order_payments_dataset.csv")
merged_df = pd.merge(orders_df, payments_df, on="order_id", how="inner")
print(merged_df.head())
print("\n--- 資料表資訊 ---")
merged_df.info()

zero_installments = merged_df[merged_df["payment_installments"] == 0]
print(f"發現 '0 期' 異常訂單共有: {len(zero_installments)} 筆")
print("\n=== 0 期異常訂單的付款方式 ===")
print(zero_installments["payment_type"].value_counts())
cleaned_df = merged_df[merged_df["payment_installments"] > 0]

print(f"\n✅ 清理完成！")
print(f"原始資料總筆數: {len(merged_df)}")
print(f"清理後乾淨筆數: {len(cleaned_df)}")
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
avg_value_by_installments = (
    cleaned_df.groupby("payment_installments")["payment_value"].mean().reset_index()
)
plt.figure(figsize=(10, 6))
sns.barplot(
    data=avg_value_by_installments,
    x="payment_installments",
    y="payment_value",
    palette="viridis",
)
plt.title(
    "Relationship between Payment Installments and Average Order Value", fontsize=15
)
plt.xlabel("Number of Installments", fontsize=12)
plt.ylabel("Average Order Value (AOV)", fontsize=12)
plt.show()
