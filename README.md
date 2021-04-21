# SADA_gcp_challenges_highest-profit
Read a CSV file containing corporate profits over the years and create JSON format data and look for highest profit values in the data.

# Output
<img src="images/output.png" alt="drawing" width="1000"/>

# Main Code
I approached this project with differnt methods and finally decide to use pandas since it's build-in DataFrame are easy and efficient to solve this challenge. By using the pandas methods, I removed the invalid data using a filter function, read the content into JSON format and print the top 20 rows with highest profit values after sorting it.
<img src="images/main_code.png" alt="drawing" width="1000"/>

# Part3 thoughts about SQL
SELECT TOP 20 FROM DataSet
ORDER BY Profit DESC
