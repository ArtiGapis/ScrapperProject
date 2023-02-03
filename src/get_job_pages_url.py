from bs4 import BeautifulSoup as soup, SoupStrainer as strainer
import get_input
import requests
import yaml

with open('../config/main.yml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

headers = {config['headers']['name_of_header']: config['headers']['value_of_the_header']}

''' Checks how many pages the search has and takes their url'''
def url_check():
    url_list = []
    url = f'{config["url"]}{get_input.input_getter()}'
    content = requests.get(url, headers=headers)
    all_lists = strainer("ul", attrs={"class": "pages_ul_inner"})
    list_soup = soup(content.text, 'html.parser', parse_only=all_lists)
    if list_soup.text:
        for item in list_soup.findAll('a'):
            url_list.append(item.attrs['href'])
    else: url_list.append(url)
    return url_list


'''Picks the job posting url from all pages received'''
def job_pages_get():
    for url in url_check():
        job_pages_list = []
        content = requests.get(url, headers=headers)
        all_jobs_pages = strainer("div", attrs={"id": "js_id_id_job_ad_list"})
        job_soup_page = soup(content.text, 'html.parser', parse_only=all_jobs_pages)
        for job_page in job_soup_page.findAll('a', class_='list_a can_visited list_a_has_logo'):
            job_pages_list.append(job_page.attrs['href'])
        return  job_pages_list
