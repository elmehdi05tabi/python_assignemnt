friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud","elmehdi"]

# Needed Output
# "Ahmed", "Sayed", "Ali",
# "Ali", "Mahmoud"
print(friends[1:4])
print(friends[friends.index("Mahmoud") : friends.index("Ali") -1:-1])