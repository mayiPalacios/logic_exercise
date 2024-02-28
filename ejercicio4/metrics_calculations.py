def calculate_total_tran_amount(data):
    total_amount = data.groupby('customer_id')['tran_amount'].sum()
    return total_amount

def calculate_frequency(data):
    frequency = data.groupby('customer_id').size()
    return frequency

def calculate_average_spending(data):
    data['average_spend'] = data["total_amount"] / data["frequency"]
    return data

