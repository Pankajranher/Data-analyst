def get_kpis(df):
    return {
        'Total Sales': df['Sales'].sum(),
        'Total Profit': df['Profit'].sum(),
        'Total Quantity': df['Quantity'].sum(),
        'Average Discount': df['Discount'].mean()
    }

def get_sales_by_category(df):
    return df.groupby('Category')["Sales"].sum().sort_values(ascending=False)