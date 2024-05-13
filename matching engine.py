import pandas as pd
client = pd.read_csv('DataSets/test-set/input_clients.csv')
instrument = pd.read_csv('DataSets/test-set/input_instruments.csv')
order = pd.read_csv('DataSets/example-set/input_orders.csv')

import csv

def matching_policies(orders, instruments, clients):
    with open('Datasets/test-set/input_orders.csv', 'w', newline='') as csvfile:
        fieldnames = ['Result']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for order_id, order in orders.items():
            for client_id, client in clients.items():
                for instrument_id, instrument in instruments.items():
                    rejection_reasons = []
                    rejected = False  # Initialize rejected flag

                    if order.instrument not in instrument.instruments:
                        rejection_reasons.append('REJECTED - INSTRUMENT NOT FOUND')

                    if instrument.currencies not in client.currencies:
                        rejection_reasons.append('REJECTED - MISMATCH CURRENCY')

                    if order.quantity % instrument.LotSize != 0:
                        rejection_reasons.append('REJECTED - INVALID LOT SIZE')
                    
                    if client.PositionCheck == 'Y':
                        if order.Side == 'Sell':
                            previous_orders = {}  # Dictionary to store previous orders and their quantities
                            for index, row in df.iterrows():
                                order_id = row['OrderID']
                                price = row['Price']
                                quantity = row['Quantity']

                                if price == 'Market':
                                    break
                                else:
                                    try:
                                        price = float(price)
                                        quantity = int(quantity)
                                        for prev_order_id, prev_price in previous_orders.items():
                                            if quantity > prev_price:
                                                rejection_reasons.append('REJECTED - POSITION CHECK FAILED')
                                                rejected = True  
                                                break  
                                    except ValueError:
                                        pass  
                     
                    if rejection_reasons:
                        for reason in rejection_reasons:
                            writer.writerow({'Result': reason})
                        break   
                    
                    if not rejected:
                        writer.writerow({'Result': 'Accept'})