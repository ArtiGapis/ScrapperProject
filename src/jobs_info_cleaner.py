import get_job_pages_url as job_info
import jobs_class
import re

'''Unnecessary information is cleared'''
def job_clean():
    all_jobs_list = []
    for job in job_info.jobs_loader():
        position = job.find('h1', id='jobad_heading1').text
        city = job.find('span', itemprop='addressLocality').text
        company = job.find('div', id='jobad_location')
        try:
            company_fix = re.search(r'- (.*)\S', company.text).group(1).replace('„', '')
        except AttributeError: company_fix = '-'
        try:
            salary = job.find('span', class_='salary_amount').text
        except AttributeError:
            salary = '0'
        read = job.findAll('div', class_='jobad_stat')
        try:
            intrest = read[0].strong.text
            acept = read[1].strong.text
        except IndexError:
            intrest = 0
            acept = 0
        all_jobs_list.append((position, company_fix, city, salary, intrest, acept))
    return all_jobs_list

'''Clears the salary field to use as an int'''
def salary_clean():
    all_jobs_list = []
    for i in job_clean():
        job = jobs_class.Jobs(*i)
        if '-' in job.salary:
            salary_re = re.search(r'(\d*)-(\d*)', job.salary)
            salary_fix = int((int(salary_re.group(1))+int(salary_re.group(2)))/2)
        elif 'From' in job.salary:
            salary_fix = int(job.salary.replace('From ', ''))
        elif 'Up to' in job.salary:
            salary_fix = int(job.salary.replace('Up to ', ''))
        elif 'Nuo' in job.salary:
            salary_fix = int(job.salary.replace('Nuo ', ''))
        else:
            salary_fix = int(job.salary)
        all_jobs_list.append((job.company_fix, job.position, job.city, salary_fix, job.intrest, job.acept))
    return all_jobs_list

