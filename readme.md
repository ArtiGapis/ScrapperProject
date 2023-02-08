# Scrapper Project

### About
This python scraper collects information from the website https://www.cvbankas.lt/. 
- You select a search keyword. 
- You choose the filtering that is most suitable for you.
- View the information or save it in CSV or XLSX files

### Introduction
Progress of the project:
"get_job_pages_url.py" takes the input and filters out all the ad pages on the site's pages based on it. 
After extracting all the information from the pages, it is placed in the "all_jobs_list" list. 
"jobs_info_cleaner.py" cleans all the necessary information and puts writer.py into a JSON file. 
"jobs_calculator" collects the JSON information according to the client's inputs and "writer.py" 
places it in the document desired by the user.
### Lounch procedure
- Lounch command line
- Type the command at the command prompt: 'git clone https://github.com/ArtiGapis/ScrapperProject.git'
- Open in your favorite editor / IDE configure virtual environment with Python v3.10
- Install the necessary libraries: 'pip install -r requirements.txt'
- Copy  'config/main.yml.example' and create 'config/main.yml' and provide your account values
- In the config file, change the lines "json_file" and "filename" depending on where your project is placed
...
### Test procedure
At the moment, only one test is placed, which checks whether the list dict groups well.