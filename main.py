from bs4 import BeautifulSoup
import requests

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Android+Development&txtLocation='
html_text = requests.get(url).text
soup = BeautifulSoup(html_text,'lxml')

jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')



for job in jobs:

    # This is additional code for this,Android and Development are defined differently
    title = job.find_all('strong', class_='blkclor')
    title = title[0].text + ' ' + title[1].text
    # additional end


    company = job.find('h3', class_='joblist-comp-name').text.strip()

    print (f'Title :  {title} \t Company : {company}')
    experienceTag = job.find('ul', class_ = 'top-jd-dtl clearfix').text
    experience = list(experienceTag)[12:]
    experience = ''.join(experience)
    newExp = experience.split()
    experience = []
    for i in range (10):
        if newExp[i] == 'yrs':
            break
        experience.append(newExp[i])

    location = newExp[-1]
    experience = ''.join(experience) + " years"
    print (f'Experience : {experience} \t Location : {location}')

    keySkills = job.find('span', class_ = 'srp-skills').text.strip()
    descTag = job.find('ul', class_='list-job-dtl clearfix')
    description = descTag.text.strip()
    print ("Key Skills : ",keySkills)

    print (("--------------------------------------")*2)