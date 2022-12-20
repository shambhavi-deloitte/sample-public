import os
# from ReadConfig import *

def generate_environment_file():
    try:
        file_name = "environment.properties"
        cwd = os.getcwd()
        dir_path = r"Reports\Allure-Reports"
        path = os.path.join(cwd, dir_path)
        if not os.path.exists(path):
            os.makedirs(path)
        with open(os.path.join(path, file_name), 'w') as f:
            f.write(f'{"Username"}={os.environ["USERNAME"]}\n')
            f.write(f'{"OS"}={os.environ["OS"]}\n')
            f.write(f'{"User_DNS_Domain"}={os.environ["USERDNSDOMAIN"]}\n')
            f.write(f'{"Processor_Architecture"}={os.environ["PROCESSOR_ARCHITECTURE"]}\n')
            f.write(f'{"Number_of_Processors"}={os.environ["NUMBER_OF_PROCESSORS"]}\n')
            f.write(f'{"Browser_Name"}={"browser_name"}\n')
            f.write(f'{"URL"}={"url"}\n')
    except:
        print('File already exists')


def generate_categories():
    try:
        file_name = "categories.json"
        cwd = os.getcwd()
        dir_path = r"Reports\Allure-Reports"
        path = os.path.join(cwd, dir_path)
        if not os.path.exists(path):
            os.makedirs(path)
        categories= '''[
    {
        "name": "Test passed",
        "matchedStatuses": ["passed"]
    },
    {
        "name":"Test Failed",
        "matchedStatuses":["failed"]
    }
]'''
        with open(os.path.join(path, file_name), 'w') as f:
            f.write(categories)
    except:
        print('File already exists')


def generate_executor_details():
    try:
        file_name = "executor.json"
        cwd = os.getcwd()
        dir_path = r"Reports\Allure-Reports"
        path = os.path.join(cwd, dir_path)
        if not os.path.exists(path):
            os.makedirs(path)
        executors = '''[
    {
    "name": "Abstract layer",
    "type": "test"
    }
]'''
        with open(os.path.join(path, file_name), 'w') as f:
            f.write(executors)
    except:
        print('File already exists')

# robot --listener allure_robotframework;Reports/Allure-Reports  --variable browser_name:edge Tests/.