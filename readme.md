# Scrapper Project

### About
This python scraper collects information from the website https://www.cvbankas.lt/. 
- You can select a keyword. 
- You can choose the filter which is the most suitable for you.
- You can view information or save it in CSV or XLSX files

### Introduction
Progress of the project:
"get_job_pages_url.py" takes the input and filters the necessary information from the pages based on it. 
All the neccesary information, from the pages, is assigned to the "all_jobs_list" list. 
"jobs_info_cleaner.py" clears all unnecessary information and puts writer.py into a JSON file. 
"jobs_calculator" collects the JSON information with user filters and "writer.py" saves the data in a xlsx or csv. 
### Startup procedure
- You should run a command line.
- You should write a 'git clone https://github.com/ArtiGapis/ScrapperProject.git' in a command line.
- Open project in your favorite editor / IDE which use a Python v3.10.
- Install the necessary libraries: 'pip install -r requirements.txt'
- Rename "config/main.yml.example" to "config/main.yml"