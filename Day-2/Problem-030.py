# Q what is the difference between continue , break, and pass ?
# break=stop the loop and exit the loop
# Example of break
for num in range(1, 6):
    if num == 3:
        print("Breaking the loop at", num)
        break
    print(num)
# Example of continue
for num in range(1, 6):
    if num == 3:
        print("Skipping", num)
        continue
    print(num)
# Example of pass
for num in range(1, 6):
    if num == 3:
        pass  # Do nothing for 3
        print("Just passing through", num)
    else:
        print(num)
