print("=" * 40)
print("    GROCERY STORE BILLING SYSTEM")
print("=" * 40)

total = 0

for i in range(1, 6):
    print(f"\nItem {i}:")
    price = float(input("  Enter price per unit (Rs.): "))  #input cost of item
    qty = int(input("  Enter quantity: "))                  #input Quantity of item
    item_cost = price * qty        #calculate overall cost of each item 
    total += item_cost                                     #calculate overall cost of each item

print("\n" + "=" * 40)
print(f"  Original Total        : Rs. {total:.2f}")       #Print original cost

if total > 100:
    discount = total * 0.10        # apply discount
    final_amount = total - discount
    print(f"  Discount (10%)     : Rs. {discount:.2f}")
    print(f"  Final Amount  : Rs. {final_amount:.2f}")
else:
    print(f"  Final Amount  : Rs. {total:.2f}")