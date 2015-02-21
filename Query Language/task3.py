db = {}

with open("data.csv") as f:
    temp_data = ([line.strip('\n\r').split(',') for line in f.readlines()])
    db_data = list(zip(*temp_data))

print(db_data)

print("Welcome, dummy!")
query = input("Please enter your quiery:")
print(query)

#print(db.keys())
