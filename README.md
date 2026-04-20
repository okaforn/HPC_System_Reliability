The 'find_lost_communication' function checks a jobtrace file for ping failures:

1. The function loops through multi-day job files

2. Looks for the jobtrace file, opens it and check if the string'lost communication with' is present

3. If the string is found, print:
    i. the name of the date folder (date), 
    ii. the name of the job folder (jobid),
    iii. the timestamp present on the 'lost communication with' line (timestamp)
    iv. the node lost communication with (lost_communication_with)

4. Keep only rows where 3(iv)is unique for each jobid and save the result as csv file

Next, the ping_failure_plots.ipynb notebook loads the resulting csv files and generates multiple plots including:
i. The elapsed time from the last ping failure reported by a node running a job untill the end of the job life
ii. Number of Jobs with Ping Failures per Week
iii. Jobs with ping failures < 5 mins before the job endtime ( per Week)
