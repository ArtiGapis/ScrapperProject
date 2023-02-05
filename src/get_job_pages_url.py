from bs4 import BeautifulSoup as soup, SoupStrainer as strainer
import src.get_input as get_input
import logging.config
import requests
import yaml
import sys


with open('config/main.yml', encoding='utf8') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
    head_config = config['headers']

with open('config/main.yml', 'r') as log_config:
    logging.config.dictConfig(yaml.safe_load(log_config)['logging'])

main_logger = logging.getLogger('main')
error_logger = logging.getLogger('error')
console_logger = logging.getLogger('console')

headers = {head_config['name_of_header']: head_config['value_of_the_header']}

''' Checks how many pages the search has and takes their url'''
def url_check():
    url_list = []
    url = f'{config["url"]}{get_input.input_getter()}'
    content = requests.get(url, headers=headers)
    all_lists = strainer("ul", attrs={"class": "pages_ul_inner"})
    list_soup = soup(content.text, 'html.parser', parse_only=all_lists)
    count = 1
    if list_soup.text:
        url_pages_nr = int
        for item in list_soup.findAll('a'):
            url_pages_nr = int(item.text)
        while count <= url_pages_nr:
            url_list.append(f'{url}&page={count}')
            count += 1

    else: url_list.append(url)
    main_logger.info(f'Get {count} url pages by user value')
    console_logger.info(f'Get {count} url pages by user value')
    return url_list

'''Picks the job posting url from all pages received'''
def job_pages_get():
    job_pages_list = []
    for url in url_check():
        content = requests.get(url, headers=headers)
        all_jobs_pages = strainer("div", attrs={"id": "js_id_id_job_ad_list"})
        job_soup_page = soup(content.text, 'html.parser', parse_only=all_jobs_pages)
        for job_page in job_soup_page.findAll('a', class_='list_a can_visited list_a_has_logo'):
            job_pages_list.append(job_page.attrs['href'])
    if len(job_pages_list)>0:
        main_logger.info(f'Found url pages of works')
        console_logger.info(f'Found url pages of works')
    elif len(job_pages_list)==0:
        print('No jobs were found for the specified keyword.\nEXIT the program')
        sys.exit()
    return job_pages_list

'''Scrape all jobs info from url'''
def jobs_loader():
    all_jobs_list = []
    jop_pages =job_pages_get()
    main_logger.info(f'Starting to load information')
    console_logger.info(f'Starting to load information')
    anime_count = 1
    for page in jop_pages:
        sys.stdout.write("\r" + config['animation'][anime_count % 10])
        content = requests.get(page, headers=headers)
        jobs = strainer("header", attrs={"id": "jobad_header"})
        jobs_soup = soup(content.text, 'html.parser', parse_only=jobs)
        all_jobs_list.append(jobs_soup)
        anime_count+=1
    print('\n')
    main_logger.info(f'All information of sorted works is loaded. {len(all_jobs_list)} jobs found')
    console_logger.info(f'All information of sorted works is loaded.\n{len(all_jobs_list)} jobs found')
    return all_jobs_list


