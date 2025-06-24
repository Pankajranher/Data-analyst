import plotly.express as px

def line_chart_sales_trend(df):
    monthly_sales = df.groupby('Month')["Sales"].sum().reset_index()
    return px.line(monthly_sales, x='Month', y='Sales', title='Monthly Sales Trend')

def bar_chart_top_products(df):
    top_products = df.groupby('Product')["Sales"].sum().nlargest(5).reset_index()
    return px.bar(top_products, x='Product', y='Sales', title='Top 5 Products by Sales')