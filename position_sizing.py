def calculate_position_size(account_balance, risk_percent, entry_price, stop_loss_price):
    risk_amount = account_balance * (risk_percent / 100)
    stop_distance = abs(entry_price - stop_loss_price)

    if stop_distance == 0:
        return 0

    position_size = risk_amount / stop_distance
    return position_size


# Example
account_balance = 1000
risk_percent = 1
entry_price = 46000
stop_loss_price = 46100

size = calculate_position_size(account_balance, risk_percent, entry_price, stop_loss_price)

print(f"Position Size: {size:.4f}")
