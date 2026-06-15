# NYC 311 Service Requests Analysis
 
## How to Run
 
1. Make sure you have Python 3 installed.
2. Navigate to this folder in your terminal.
3. Run the script:
 
python3 analysis.py
 
Output will be saved to `output.txt`. The console will confirm when the file has been written.
 
## What This Script Does
 
We receive a big stack of papers coded "nyc_311_requests" and have 3 objectives to complete. We flip through each page to find how many requests are "Open", figure out the most common complaint type, and count how many requests came from each borough. All three answers get saved to a folder called "output.txt". 
 
## Dependencies
 
This script uses only Python's built-in libraries: `csv`.
 
## Notes

I solved question 1 on my own and partially completed questions 2 and 3 without AI. I used dictionaries to store the values of `complaint_type` and `borough`, looping through the rows list to access the values. I created a `complaint` and `borough` variable in their respective loops for easy readability. I understand that when adding new values into a dictionary, I need to use `dict[key]`, and I used `get()` to grab the complaint and borough counts. I created a new variable named `common_comp` using the `max()` method to get the most common complaint, but I did not know how to retrieve the count needed to meet the requirements. I also had issues with formatting the output and received assistance from AI. 