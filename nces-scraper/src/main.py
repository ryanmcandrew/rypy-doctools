from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# from html_table_parser.parser import HTMLTableParser
# import html_table_parser as table_parser
from html_table_parser.parser_functions import extract_tables

import pandas
import time
import typing
import inspect
import pprint

import model

search_scheme_2 = "https://www.bb-sd.com/protected/SearchResults.aspx?search=policies&sections=912"
brentwood_boro_policy_manager_site = "https://go.boarddocs.com/pa/bren/Board.nsf/Public"

def nces_search():
    '''
    '''
    states = [
        "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", 
        "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
        "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", 
        "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", 
        "Washington", "West Virginia", "Wisconsin", "Wyoming"
    ]
    root_url = "https://nces.ed.gov/ccd/"
    base_url = root_url + "districtsearch/"
    driver = webdriver.Chrome()

    for state in states:
        driver.get(base_url)
        time.sleep(1)
        
        #get element objects on the webpage
        state_input = driver.find_element(By.XPATH, "//select[contains(@name, 'State')]")
        submit_button = driver.find_element(By.XPATH, "//input[contains(@value, 'Search ')]")
        
        #interact with the input items
        state_input.click()
        state_input.send_keys(state)
        state_input.click()
        
        # send the search and wait for results page
        submit_button.click()
        time.sleep(1)

        search_nces_district_data(driver)
        

def search_nces_district_data(driver):
    '''
    '''

    #get all the data from district pages
    entrance_url = driver.current_url
    get_nces_district_data(driver, driver.find_elements(By.XPATH, "//a"))
    driver.get(entrance_url)
    time.sleep(1)

    #if there are next>> present, load the next page, get that data, and return
    next_page_element = driver.find_elements(By.XPATH, "//a[text()[contains(., 'Next >>')]]")
    while len(next_page_element) > 0:
        next_page_element[0].click()
        time.sleep(1)
        current_url = driver.current_url
        get_nces_district_data(driver, driver.find_elements(By.XPATH, "//a"))
        driver.get(current_url)
        time.sleep(1)
        next_page_element = driver.find_elements(By.XPATH, "//a[text()[contains(., 'Next >>')]]")

    # driver.get(entrance_url)
    # time.sleep(1)

def get_nces_district_data(driver, url_elements):
    '''
    '''
    root_url = driver.current_url
    
    scraped_data = model.NcesDistrictPage()

    school_detail_pages_to_visit = []
    # get the URLs to visit
    for school_page_url_element in url_elements:
        school_url_search_result_href_text = school_page_url_element.get_attribute('href')
        if school_url_search_result_href_text is not None:
            if school_url_search_result_href_text.find("district_detail") != -1:
                school_detail_pages_to_visit.append(school_url_search_result_href_text)

    with open("districts.csv", "a") as file:
        # visit each page and gather data
        for detail_page_link in school_detail_pages_to_visit:            
            driver.get(detail_page_link)
            time.sleep(1)

            # scrape the data off the school page
            tables = pandas.read_html(driver.page_source)
            for table in tables:
                dict_table = table.to_dict()
                for outer_key in dict_table:
                    for inner_key in dict_table[outer_key]:
                        scraped_data.load(str(dict_table[outer_key][inner_key]))
            
            file.write(",".join([str(i) for i in scraped_data.data]) + "\n")
            print(",".join([str(i) for i in scraped_data.data]) + "\n")
            
            #get the link to the school search page for this district, then call a search for district schools
            school_urls = driver.find_elements(By.XPATH, "//a[contains(@href, '/schoolsearch/school_list')]")
            if len(school_urls) > 0:
                schools_search_link = school_urls[0].get_attribute('href')
                #if we found a url, search the page
                current_url = driver.current_url
                search_nces_school_data(driver, schools_search_link)
                print('finished school search for district')
                driver.get(current_url)
                time.sleep(1)
            else:
                print('couldnt find schools in district search link')

    return scraped_data

def search_nces_school_data(driver, url):
    '''
    '''
    entrance_url = driver.current_url
    driver.get(url)
    time.sleep(1)

    current_url = driver.current_url
    get_nces_school(driver, driver.find_elements(By.XPATH, "//a"))
    print('finished school search on base page')
    driver.get(current_url)
    time.sleep(1)

    next_page_element = driver.find_elements(By.XPATH, "//a[text()[contains(., 'Next >>')]]")
    while len(next_page_element) > 0:
        next_page_element[0].click()
        time.sleep(1)

        current_url = driver.current_url
        get_nces_school(driver, driver.find_elements(By.XPATH, "//a"))
        print('finished school search on a next page')
        driver.get(current_url)
        time.sleep(1)
        
        next_page_element = driver.find_elements(By.XPATH, "//a[text()[contains(., 'Next >>')]]")

def get_nces_school(driver, url_elements):
    '''
    '''
    root_url = driver.current_url

    scraped_school_data = model.NcesSchoolPage()

    school_detail_pages_to_visit = []
    # get the URLs to visit
    for school_page_url_element in url_elements:
        school_url_search_result_href_text = school_page_url_element.get_attribute('href')
        if school_url_search_result_href_text is not None:
            if school_url_search_result_href_text.find("school_detail") != -1:
                school_detail_pages_to_visit.append(school_url_search_result_href_text)

    with open("schools.csv", "a") as file:
        # write header if it's the first line
        # file.write(",".join(data_to_scrape) + "\n")
        # visit each page and gather data
        for detail_page_link in school_detail_pages_to_visit:
            driver.get(detail_page_link)
            time.sleep(1)

            # scrape the data off the school page
            school_name = ''
            tables = pandas.read_html(driver.page_source)
            for table in tables:
                dict_table = table.to_dict()
                for outer_key in dict_table:
                    for inner_key in dict_table[outer_key]:
                        scraped_school_data.load(str(dict_table[outer_key][inner_key]))
            
            file.write(",".join([str(i) for i in scraped_school_data.data]) + "\n")
            print(",".join([str(i) for i in scraped_school_data.data]) + "\n")

def link_to_policy_search(url:str):
    '''
        General policy finding algo:
        - find the search box
        - enter "policy" into the search box
        - execute the search
        - get a list of results
        - search each result for additional query like "handbook" or some unique identifying phrase that we know is going to be included in every policy like "Gov. Order 66"
    '''
    driver = webdriver.Chrome()
    links = []
    search_input_possible_names = ['search', 's']

    # Navigate to the webpage
    driver.get(url)
    
    return links
    

def main():
    nces_search()
    # print(link_to_policy_search('https://www.bb-sd.com'))

if __name__ == '__main__':
    main()