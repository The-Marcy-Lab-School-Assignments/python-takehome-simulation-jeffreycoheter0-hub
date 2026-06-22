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

# Outputs
with open('output.txt', 'w') as f:
    f.write(f"Open requests: {open_count}\n")
    f.write(f"\nMost common complaint type: {common_comp} ({complaints[common_comp]} requests)\n")
    f.write(f"\nRequests per borough: \n")
    for borough in sorted(boroughs):
        f.write(f"- {borough}: {boroughs[borough]}\n")

print("Output saved to output.txt")
