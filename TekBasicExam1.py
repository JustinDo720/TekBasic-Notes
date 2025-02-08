"""

Python function process list of dictionaries

{
    "transaction_id": int,
    "product_name": str,
    "price":float,
    "quantity": int,
    "date" : str (Format: 'YYYY-MM-DD')
}

start_date & end_date in 'YYYY-MM-DD'
"""

# Based on the Example input
transactions = [
    {
        "transaction_id": 1,
        "product_name": "Laptop",
        "price": 1200,
        "quantity": 3,
        "date": '2025-01-05'
    },
    {
        "transaction_id": 2,
        "product_name": "Phone",
        "price": 800,
        "quantity": 5,
        "date": '2025-01-12'
    },
    {
        "transaction_id": 3,
        "product_name": "Tablet",
        "price": 300,
        "quantity": 10,
        "date": '2025-01-15'
    },
    {
        "transaction_id": 4,
        "product_name": "Laptop",
        "price": 1200,
        "quantity": 1,
        "date": '2025-01-20'
    },
]

start_date = "2025-01-01"
end_date = "2025-01-20"

# Must build a function to filter transaction based on start_date and end_date
# Calculate the total sales values (price*quantity) for each transaction
# Return some values
def filter_and_analyze_transactions(transactions, start_date, end_date):

    # Before filtering we need to find the range from start_date to end_date
    # Since every date is in YYYY-MM-DD
    end_day = int(end_date.split('-')[2])
    start_day = int(start_date.split('-')[2])

    # End day isn't included
    day_range = [day for day in range(start_day, end_day)]

    # Now let's filter the transaction based on date
    filtered_transactions = [trans for trans in transactions if int(trans['date'].split('-')[2]) in day_range]

    # Once we have our filtered transaction let's build the total sales
    # For each transaction we need to calculate the total sales
    # Let's loop through the transactions and add a new dictionary key fot that cal
    top_productsv2 = []
    for transaction in filtered_transactions:
        # Because we only have product_name and total_sales in the output
        product_desc = {
            'product_name': transaction['product_name'],
            'total_sales': transaction['price'] * transaction['quantity']
        }
        top_productsv2.append(product_desc)
        transaction['total_sales'] = transaction['price'] * transaction['quantity']

    # Return top 3 products sold
    # Total sales value
    # Average sales

    # For us to get the top 3 products we need to filter based on total sales
    top_productsv2.sort(key=lambda trans: trans['total_sales'])
    # Top 3 products
    top_products = top_productsv2[:4]
    # For total sales we could loop and add to total_sales
    total_sales = 0
    for trans in filtered_transactions:
        total_sales += float(trans['total_sales'])

    # Average sale we'll take the total divided by the num or transactions
    avg_sale = float(total_sales) / len(transactions)
    returned_dict = {
        'top_products': top_products,
        'total_sales': total_sales,
        'average_sales_per_transaction': avg_sale
    }
    return returned_dict

trans_details = filter_and_analyze_transactions(transactions, start_date, end_date)
print(trans_details)
