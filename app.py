from flask import Flask, render_template, request
import pandas as pd
import io

app = Flask(__name__)

def compute_total_revenue_by_month(df):
    df['Purchase Date'] = pd.to_datetime(df['Purchase Date'])
    df['Revenue'] = df['Item Price'] * df['Amount']
    revenue_by_month = df.groupby(df['Purchase Date'].dt.to_period('M'))['Revenue'].sum().reset_index()
    revenue_by_month['Purchase Date'] = revenue_by_month['Purchase Date'].dt.strftime('%Y-%m')
    return revenue_by_month

def compute_total_revenue_by_product(df):
    df['Revenue'] = df['Item Price'] * df['Amount']
    revenue_by_product = df.groupby('Item Name')['Revenue'].sum().reset_index()
    return revenue_by_product

def compute_total_revenue_by_customer(df):
    df['Revenue'] = df['Item Price'] * df['Amount']
    revenue_by_customer = df.groupby('Client ID')['Revenue'].sum().reset_index()
    return revenue_by_customer

def identify_top_customers(df, top_n=10):
    revenue_by_customer = compute_total_revenue_by_customer(df)
    top_customers = revenue_by_customer.sort_values(by='Revenue', ascending=False).head(top_n)
    return top_customers

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if not file:
            return "No file"

        df = pd.read_csv(io.StringIO(file.stream.read().decode("UTF8")), delimiter=',')
        
        revenue_by_month = compute_total_revenue_by_month(df)
        revenue_by_product = compute_total_revenue_by_product(df)
        revenue_by_customer = compute_total_revenue_by_customer(df)
        top_customers = identify_top_customers(df)

        return render_template('index.html',
                               revenue_by_month=revenue_by_month.to_dict('records'),
                               revenue_by_product=revenue_by_product.to_dict('records'),
                               revenue_by_customer=revenue_by_customer.to_dict('records'),
                               top_customers=top_customers.to_dict('records'))
    return render_template('index.html', revenue_by_month=None, revenue_by_product=None, revenue_by_customer=None, top_customers=None)

if __name__ == '__main__':
    app.run(debug=True)
