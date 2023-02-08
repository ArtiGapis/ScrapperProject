from src.classes_wrapper import configs_class
import logging.config
import yaml
import sys

path = sys.path

def class_getter(yml):
    with open(yml, 'r') as log_config:
        logging.config.dictConfig(yaml.safe_load(log_config)['logging'])

    with open(yml, encoding='utf8') as f:
        my_config = yaml.load(f, Loader=yaml.FullLoader)
    head_config = my_config['headers']
    conf_animation = my_config['animation']
    url = my_config["url"]
    main_logger = logging.getLogger('main')
    console_logger = logging.getLogger('console')
    headers = {head_config['name_of_header']: head_config['value_of_the_header']}
    json_file = my_config['json_file']
    return configs_class(headers, conf_animation, url, main_logger, console_logger, json_file)


all_configs = class_getter(f'{path[1]}/config/main.yml')
