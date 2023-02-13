from bs4 import BeautifulSoup as soup, SoupStrainer as strainer
import requests
import sys

''' Checks how many pages have a URL'''
def url_check(url, input, config):
    url_list = []
    full_url = f'{url}{input}'
    content = requests.get(full_url, headers=config.headers)
    all_lists = strainer("ul", attrs={"class": "pages_ul_inner"})
    list_soup = soup(content.text, 'html.parser', parse_only=all_lists)
    count = 1
    if list_soup.text:
        url_pages_nr = int
        for item in list_soup.findAll('a'):
            url_pages_nr = int(item.text)
        while count <= url_pages_nr:
            url_list.append(f'{full_url}&page={count}')
            count += 1
    else: url_list.append(full_url)
    config.main_logger.info(f'Gets {count} url pages by user value')
    config.console_logger.info(f'Gets {count} url pages by user value')
    return url_list


'''Takes the job advertisements URL from all pages received'''
def job_pages_get(url_list, config):
    job_pages_list = []
    for url_page in url_list:
        content = requests.get(url_page, headers=config.headers)
        all_jobs_pages = strainer("div", attrs={"id": "js_id_id_job_ad_list"})
        job_soup_page = soup(content.text, 'html.parser', parse_only=all_jobs_pages)
        for job_page in job_soup_page.findAll('a', class_='list_a can_visited list_a_has_logo'):
            job_pages_list.append(job_page.attrs['href'])
    if len(job_pages_list) > 0:
        config.main_logger.info(f'Founds URL pages of works')
        config.console_logger.info(f'Founds URL pages of works')
    elif len(job_pages_list) == 0:
        print('No job advertisements found for the specific keyword.\nEXIT the program')
        sys.exit()
    return job_pages_list


'''Scrapes all job advertisements from URL'''
def jobs_loader(job_pages, config):
    all_jobs_list = []
    config.main_logger.info(f'Starting to load information')
    config.console_logger.info(f'Starting to load information')
    anime_count = 1
    for page in job_pages:
        sys.stdout.write("\r" + config.conf_animation[anime_count % 10])
        content = requests.get(page, headers=config.headers)
        jobs = strainer("header", attrs={"id": "jobad_header"})
        jobs_soup = soup(content.text, 'html.parser', parse_only=jobs)
        all_jobs_list.append(jobs_soup)
        anime_count += 1
    config.main_logger.info(f'All information of sorted works is loaded. {len(all_jobs_list)} jobs found')
    config.console_logger.info(f'All information of sorted works is loaded.\n{len(all_jobs_list)} jobs found')
    return all_jobs_list



