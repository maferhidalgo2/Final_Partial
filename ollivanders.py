Link #
https://replit.com/join/tijltqxuaz-maria-fernan901


# Initialize an empty dictionary to store customer information
customer_records = {}

# Function to record customer entry and wand purchase
def record_customer_entry():
    while True:
        new_customer = input("Does a client come in? (Yes/No): ")
        if new_customer.lower() == 'yes':
            buy_something = input("Buy something? (Yes/No): ")
            if buy_something.lower() == 'yes':
                print("Elder Wand [1], Hawthorn Wand [2], Willow Wand [3], Holly Wand [4]")
                wand_choice = input("What wand did you buy? (Choose 1, 2, 3, or 4): ")

                # Mapping the wand choice to its name
                wand_options = {
                    '1': 'Elder Wand',
                    '2': 'Hawthorn Wand',
                    '3': 'Willow Wand',
                    '4': 'Holly Wand'
                }

                if wand_choice in wand_options:
                    wand_purchased = wand_options[wand_choice]

                    # Store customer information
                    if 'customer_name' in locals():
                        if customer_name in customer_records:
                            customer_records[customer_name]['wand'].append(wand_purchased)
                        else:
                            customer_records[customer_name] = {'wand': [wand_purchased], 'bought': True}
                    else:
                        print("Customer not recorded.")

        else:
            break

# Record customer entries
record_customer_entry()

# Display the records
print("Customer Records:")
for customer, data in customer_records.items():
    print(f"Customer: {customer}, Bought Wands: {data['wand']}")
