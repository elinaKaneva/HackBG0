import re

N = 99999
DB = {}

with open("data.csv") as f:
    temp_data = ([line.strip('\n\r').split(',') for line in f.readlines()])
    transposed_data = list(zip(*temp_data))

for col in transposed_data:
    DB[col[0]] = [int(cell) if cell.isdigit() else cell for cell in col[1:]]


def select(columns, limit=N):
    result = {}
    for col in columns:
        result[col] = DB[col][:limit]
        print(col, DB[col][:limit])


def sum_column(column):
    print(sum(DB[column]))


def show():
    print(list(DB.keys()))


def find(key):
    result = {}
    row_indexes = []

    for col in DB:
        for i, x in enumerate(DB[col]):
            result[col] = []
            if key in str(x):
                row_indexes.append(i)
                print(x)

    for col in DB:
        for i in row_indexes:
            result[col].append(DB[col][i])

    print(result)
find("oo")


def check_query(query):

    q = query.split()

    if query == "SHOW":
        show()
    elif re.search("FIND *", query):
        find(q[1])
    elif re.search("SUM *", query):
        if q[1] in DB:
            if str(DB[q[1]][0]).isdigit():
                sum_column(q[1])
            else:
                print("Unsupported query for text columns.")
    elif re.search("SELECT *", query):
        cols = q[1].split(",")
        if set(cols).issubset(DB.keys()):
            if "LIMIT" in q and q[3].isdigit() and int(q[3]) > 0:
                select(cols,int(q[3]))
            else:
                select(cols)
        else:
            print("No such column: %s." % q[1])
    else:
        print('''
-> Invalid query!

List of available queries again:
-> SELECT [columns] LIMIT X
-> SUM [column]
-> SHOW
-> FIND X
''')


def enter_query(welcome=1):
    if welcome == 1:
        print('''-> Welcome, dummy!

Hint 1: For exit "Ctr + C" or whatever floats your boat..

Hint 2: Available queries:
-> SELECT [columns] LIMIT X
-> SUM [column]
-> SHOW
-> FIND X
''')

    query_string = input("Please enter your query:")
    check_query(query_string)

    enter_query(0)

enter_query()
