users = [
    {'id': 623, 'displayName': 'Joe Smith', 'email': 'joe.smith@example.com'},
    {'id': 321, 'displayName': 'Jane Smith', 'email': 'jane.smith@example.com'},
    {'id': 420, 'displayName': 'Bob Smith', 'email': 'bob.smith@example.com'},
]

print(users)

def sorter(user):
    return user['id']


users.sort(key=sorter)
print(users)

reverseUsers = sorted(users, key=sorter, reverse=True)
print(reverseUsers)