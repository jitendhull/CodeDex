virat = {'name': 'Virat Kohli', 'position': 3, 'jersey': 18, 'runs': 1500}

dhoni = {'name': 'Mahendra Singh Dhoni', 'position': 5, 'jersey': 7, 'runs': 2000}

rohit = {'name': 'Rohit Sharma', 'position': 1, 'jersey': 45, 'runs': 1700}

hardik = {'name': 'Hardik Pandya', 'position': 6, 'jersey': 33, 'runs': 1000}

jadeja = {'name': 'Ravindra Jadeja', 'position': 7, 'jersey': 8, 'runs': 800}

bumrah = {'name': 'Jasprit Bumrah', 'position': 11, 'jersey': 93, 'runs': 400}

print('Virat Position:', virat['position'])
print('Dhoni Position:', dhoni['position'])
print('Rohit Position:', rohit['position'])
print('Hardik Postion:', hardik['position'])
print('Jadeja Postion:', jadeja['position'])
print('Bumrah Postion:', bumrah['position'])

dhoni['position'] = 7

total_runs = virat['runs'] + dhoni['runs'] + rohit['runs'] + hardik['runs'] + jadeja['runs'] + bumrah['runs']

average_runs = total_runs/6

print('Average Runs: ', average_runs)

print('New Dhoni Dict:', dhoni)