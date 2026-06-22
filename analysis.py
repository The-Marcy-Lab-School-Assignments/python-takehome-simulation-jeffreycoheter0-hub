import csv

rows = []

with open('nyc_311_requests.csv') as f:
    reader = csv.DictReader(f)
    
    # Question 1: How many "Open" requests are active 
    open_count = 0

    for row in reader:
        rows.append(row)
        if row["resolution_status"] == "Open":
            open_count += 1

# Question 2: Most common complaint type
complaints = {}
for row in rows:
    complaint = row["complaint_type"]
    complaints[complaint] = complaints.get(complaint, 0) + 1

common_comp = max(complaints, key=complaints.get)

# Question 3: Requests for each borough
boroughs = {}
for row in rows:
    borough = row["borough"]
    boroughs[borough] = boroughs.get(borough, 0) + 1

# Question 5: Open requests for each borough
open_by_borough = {}
for row in rows:
    if row["resolution_status"] == "Open":
        borough = row["borough"]
        open_by_borough[borough] = open_by_borough.get(borough, 0) + 1

top_open_borough = max(open_by_borough, key=open_by_borough.get)

# Question 6: Closed requests per borough
borough_closed = {}
for row in rows:
    borough = row["borough"]
    if row["resolution_status"] == "Closed":
        borough_closed[borough] = borough_closed.get(borough, 0) + 1

# Outputs
with open('output.txt', 'w') as f:
    # Q1
    f.write(f"Open requests: {open_count}\n")

    # Q2
    f.write(f"\nMost common complaint type: {common_comp} ({complaints[common_comp]} requests)\n")

    # Q3
    f.write(f"\nRequests per borough: \n")
    for borough in sorted(boroughs):
        f.write(f"- {borough}: {boroughs[borough]}\n")
    
    # Q4
    f.write(f"\nRequests by complaint type:\n")
    for complaint, count in sorted(complaints.items(), key=lambda x: x[1], reverse=True):
        f.write(f"- {complaint}: {count}\n")

    # Q5
    f.write(f"\nBorough with most open requests: {top_open_borough} ({open_by_borough[top_open_borough]} open)\n")

    # Q6
    f.write(f"\nClosure rate by borough:\n")
    for borough in sorted(boroughs):
        rate = (borough_closed[borough] / boroughs[borough]) * 100
        f.write(f"- {borough}: {round(rate, 1)}%\n")

    # Q7
    f.write(f"\nTop 3 boroughs by total requests:\n")
    top_3 = sorted(boroughs.items(), key=lambda x: (-x[1], x[0]))[:3]
    for i, (borough, count) in enumerate(top_3, start=1):
        f.write(f"{i}. {borough} ({count} requests)\n")
    
print("Output saved to output.txt")
