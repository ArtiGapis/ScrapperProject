import src.get_job_pages_url as job_info
import src.jobs_class as jobs_class
import logging.config
import yaml
import re

with open('config/main.yml', 'r') as log_config:
    logging.config.dictConfig(yaml.safe_load(log_config)['logging'])

main_logger = logging.getLogger('main')
console_logger = logging.getLogger('console')

'''Unnecessary information is cleared'''
def job_clean():
    all_jobs_list = []
    for job in job_info.jobs_loader():
        position = job.find('h1', id='jobad_heading1').text
        city = job.find('span', itemprop='addressLocality').text
        company = job.find('div', id='jobad_location')
        try:
            company_fix = re.search(r'- (.*)\S', company.text).group(1).replace('„', '')
        except AttributeError:
            company_fix = '-'
        try:
            salary = job.find('span', class_='salary_amount').text
        except AttributeError:
            salary = '0'
        read = job.findAll('div', class_='jobad_stat')
        try:
            intrest = int(read[0].strong.text)
            if read[1].strong.text == '>50':
                acept = 50
            else: acept = int(read[1].strong.text)
        except IndexError:
            intrest = 0
            acept = 0
        all_jobs_list.append((position, company_fix, city, salary, intrest, acept))
    main_logger.info(f'Jobs fields is cleaned')
    console_logger.info(f'Jobs fields is cleaned')
    return all_jobs_list

'''Clears the salary field to use as an int'''
def salary_clean():
    all_jobs_list = []
    for i in job_clean():
        job = jobs_class.Jobs(*i)
        if '-' in job.salary:
            salary_re = re.search(r'(\d*)-(\d*)', job.salary)
            salary_fix = float((float(salary_re.group(1))+float(salary_re.group(2)))/2)
        elif 'From' in job.salary:
            salary_fix = float(job.salary.replace('From ', '').replace(',', '.'))
        elif 'Up to' in job.salary:
            salary_fix = float(job.salary.replace('Up to ', '').replace(',', '.'))
        elif 'Nuo ' in job.salary:
            salary_fix = float(job.salary.replace('Nuo ', '').replace(',', '.'))
        elif 'Iki ' in job.salary:
            salary_fix = float(job.salary.replace('Iki ', '').replace(',', '.'))
        else:
            salary_fix = float(job.salary.replace(',', '.'))
        all_jobs_list.append((job.position, job.company_fix, job.city, salary_fix, job.intrest, job.acept))
    main_logger.info(f'Convert salary')
    console_logger.info(f'Convert salary')
    return all_jobs_list
