#import beautifulsoup and request here
from bs4 import BeautifulSoup
import requests
import json

#function to get job list from url f'https://www.talent.com/jobs?k={role}&l={location}'

def getJobList(role,location):
    url = f'https://www.talent.com/jobs?k={role}&l={location}'
    # Complete the missing part of this function here
    response = requests.get(url, params={"k": role, "l": location})
    jobs = BeautifulSoup(response.text, 'html.parser')
    job_descriptions = []
    jobCards = jobs.find_all('div', class_='card card__job')

    # loop through jobCards
    for link in jobCards:
        # find job title
        jobTitle = link.find('h2', class_='card__job-title').string.strip()
        
        # find company name
        companyName = link.find('div', class_='card__job-empname-label').children
        # iterate through children
        for child in companyName:
            companyName = child
            break
        companyName = companyName.string
        
        # find job description
        description = link.find('p', class_='card__job-snippet').string.strip()
        # append descriptions to list
        job_descriptions.append(description)
        
        # find salary
        salary = link.find('div', class_='card__job-badge-salary')
        # not all jobs include salary
        if salary == None:
            salary = "Salary not listed"
        else:
            salary = salary.string
        
        # print out info
        print("\n\nJob Title: " + jobTitle + "\nCompany Name: " + companyName + "\nDescription: " + description + "\nSalary: " + salary)
    print("\n\n")
    return job_descriptions

#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    json_file = open("jobDetails.json", "w")
    json.dump(jobDetails, json_file)
    json_file.close()
    print("Saved job details to JSON file.")

#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    # Complete the missing part of this function here
    print("\nEnter desired location")
    location = input()
    print("\nYou entered: " + role + ", " + location + ".\n")

    jobDetails = getJobList(role, location) 
    print(jobDetails)
    saveDataInJSON(jobDetails)

if __name__ == '__main__':
    main()
