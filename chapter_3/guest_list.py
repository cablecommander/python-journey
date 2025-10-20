# Learning how to use lists.

guest_list = ['Abraham', 'Noah', 'David']
message0 = f"{guest_list} you are invited to dinner."


print(message0)

print(f"{guest_list[1]} can't make it due to weather")
guest_list.remove('Noah')
guest_list.append('Paul')

message1 = f"{guest_list} you are invited to dinner. Please still come!"

print(message1)

message2 = f"{guest_list} we found a bigger table. More people are comming."
guest_list.insert(0, 'Joe')
guest_list.insert(2, 'Tom')
guest_list.append('Larry')


message3 = f"{guest_list} you are invited to dinner."

print(message3)
print(len(guest_list))

message4 = "Table is not comming in time. I can only have two guests."

guest0 = guest_list.pop(0)
print(f"{guest0} sorry you cannot come.")

guest0 = guest_list.pop(0)
print(f"{guest0} sorry you cannot come.")

guest0 = guest_list.pop(0)
print(f"{guest0} sorry you cannot come.")

guest0 = guest_list.pop(0)
print(f"{guest0} sorry you cannot come.")


print(f"{guest_list} you are still welcome.")
del guest_list[0]
del guest_list[0]

print(guest_list)
