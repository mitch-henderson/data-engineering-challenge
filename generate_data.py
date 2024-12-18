import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_sample_data(output_dir="./data"):
    # Create customers
    np.random.seed(42)
    n_customers = 1000
    
    customers = pd.DataFrame({
        'customer_id': range(1, n_customers + 1),
        'name': [f'Customer {i}' for i in range(1, n_customers + 1)],
        'email': [f'customer{i}@example.com' for i in range(1, n_customers + 1)],
        'country': np.random.choice(['US', 'UK', 'CA', 'AU', 'DE'], n_customers),
        'join_date': pd.date_range(start='2023-01-01', periods=n_customers)
    })
    
    # Create products
    n_products = 100
    products = pd.DataFrame({
        'product_id': range(1, n_products + 1),
        'name': [f'Product {i}' for i in range(1, n_products + 1)],
        'category': np.random.choice(['Electronics', 'Clothing', 'Books', 'Home', 'Sports'], n_products),
        'price': np.random.uniform(10, 1000, n_products).round(2),
        'inventory_count': np.random.randint(0, 1000, n_products)
    })
    
    # Create orders
    n_orders = 5000
    orders = pd.DataFrame({
        'order_id': range(1, n_orders + 1),
        'customer_id': np.random.choice(customers['customer_id'], n_orders),
        'order_date': pd.date_range(start='2023-01-01', end='2024-01-01', periods=n_orders),
        'total_amount': np.random.uniform(20, 2000, n_orders).round(2),
        'status': np.random.choice(['completed', 'pending', 'cancelled'], n_orders, p=[0.8, 0.15, 0.05])
    })
    
    # Save to CSV
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    customers.to_csv(f'{output_dir}/customers.csv', index=False)
    products.to_csv(f'{output_dir}/products.csv', index=False)
    orders.to_csv(f'{output_dir}/orders.csv', index=False)
    
    print(f"Generated files in {output_dir}:")
    print(f"- customers.csv: {len(customers)} records")
    print(f"- products.csv: {len(products)} records")
    print(f"- orders.csv: {len(orders)} records")

if __name__ == "__main__":
    generate_sample_data()
