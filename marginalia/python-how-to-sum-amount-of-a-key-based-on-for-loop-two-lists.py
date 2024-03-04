# https://stackoverflow.com/questions/78100608/python-how-to-sum-amount-of-a-key-based-on-for-loop-two-lists/

list1 = [
    {'user_id': 1, 'server_id': '10', 'amount': 100},
    {'user_id': 2, 'server_id': None, 'amount': 10000},
    {'user_id': 3, 'server_id': '10', 'amount': 200},
    {'user_id': 1, 'server_id': '10', 'amount': 200},
    {'user_id': 2, 'server_id': '10', 'amount': 110},
    {'user_id': 2, 'server_id': None, 'amount': 40000},
    {'user_id': 3, 'server_id': '10', 'amount': 100},
    {'user_id': 3, 'server_id': None, 'amount': 12500},
    {'user_id': 3, 'server_id': '10', 'amount': 100},
    {'user_id': 1, 'server_id': None, 'amount': 22500},
]

list2 = [
    {'id': 1},
    {'id': 4},
    {'id': 18},
    {'id': 3},
    {'id': 2},
]

list2_ids = [r['id'] for r in list2]
list2_ids.sort()

for user_id in list2_ids:
    data_for_user = [r for r in list1 if r['user_id'] == user_id]
    if len(data_for_user):
        spent = sum([r['amount'] for r in data_for_user if r['server_id'] != None])
        add_funds = sum([r['amount'] for r in data_for_user if r['server_id'] == None])
        final_balance = add_funds - spent
        print(f"User{user_id} spent {format(spent, ',d')}, add_funds {format(add_funds, ',d')}, final_balance {format(final_balance, ',d')}")
