#import beautifulsoup and request here
from bs4 import BeautifulSoup
import requests
import json

#function to get job list from url f'https://www.talent.com/jobs?k={role}&l={location}'

def getJobList(role,location):
    url = f'https://www.talent.com/jobs?k={role}&l={location}'
    # Complete the missing part of this function here
    response = requests.get(url, params={"k": role, "l": location})
    return response.text

#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    json_file = open("Available_Jobs.json", "w")
    json.dump(jobDetails, json_file)
    json_file.close()
    print("Saving data to JSON")

#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    # Complete the missing part of this function here
    print("Enter desired location")
    location = input()

    jobDetails = getJobList(role, location) 
    saveDataInJSON(jobDetails)

if __name__ == '__main__':
    main()
