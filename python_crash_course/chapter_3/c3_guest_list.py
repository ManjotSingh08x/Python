guest_list = ['Albert Einstien', 'Nicola Tesla', 
              'BR. Ambedkar', 'Eminem', 'Stan']

guest_removed = 'BR. Ambedkar'
guest_list.remove(guest_removed)
print(f"{guest_removed} couldn't make it")

print("I have found a bigger table so i a inviting 3 more guests!")
guest_list.insert(0, "George Washington")
guest_list.insert(int(len(guest_list)/2+1), "Hitler")
guest_list.append("Manjeet")

print("The table i got was not delivered in time")

while len(guest_list) > 2:
    discarded_guest = guest_list.pop()
    print(f"Sorry {discarded_guest}, I cannot invite you")

for guest in guest_list:
    print(f"Dear {guest}, you are invited for dinner with me.")
    
del guest_list[1]
del guest_list[0]
print(guest_list)