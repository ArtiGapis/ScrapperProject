import jobs_info_cleaner as jic
import jobs_class
import json

'''All processed information is placed in .json'''
def writer():
    jobs_json = []
    for job in jic.salary_clean():
        jobs = jobs_class.Jobs(*job)
        jobs_json.append({'Company' : jobs.company_fix, 'Position': jobs.position, 'City': jobs.city, 'Salary': jobs.salary, 'Intrest' : jobs.intrest, 'Acept' : jobs.acept})
    with open("../docs/jobs.json", "w") as write_file:
        json.dump(jobs_json, write_file, indent=4, default=vars)
        print(f'Information writed from WEB')

