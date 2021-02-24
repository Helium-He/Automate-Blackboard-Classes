from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import threading
import telepot,requests
import pyautogui
import os

def start_chrome():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 2,})
    options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')

    browser   = webdriver.Chrome(options = options)

    # University Blackboard LINK
    browser.get('http://cuchd.blackboard.com/')

    while True:
        try:
            cookies_agree = browser.find_element(by = 'id',value = 'agree_button')
            username = browser.find_element(by = 'id',value = 'user_id')
            password = browser.find_element(by = 'id',value = 'password')
            cookies_agree.click()
            username.send_keys('USERNAME')
            password.send_keys('PASSWORD')
            password.send_keys(Keys.RETURN)
            break
        except:continue
    return browser


def startclass(class_name,class_id,end_time):

    print("I'm working...: "+class_name)
    browser  = start_chrome()


    while True:
        try:
            open_subject = browser.find_element(by = 'id',value = class_id)
            open_subject.click()
            break
        except:
            try:
                searchBar = browser.find_element_by_tag_name('input')
                # searchBar = browser.find_element(by='tag',value='input')
                searchBar.send_keys(Keys.PAGE_DOWN)
                time.sleep(1)
                searchBar.send_keys(Keys.PAGE_UP)
            except Exception as e:
                continue
            continue

    while True:
        try:
            open_class  = browser.find_element(by = 'id',value = 'sessions-list-dropdown')
            open_class.click()
            break
        except:continue

    while True:
        try:
            course = browser.find_element(by = 'xpath', value ='//li[@ng-repeat=\'collabSession in courseOutline.courseSessionList\']//a[@role=\'menuitem\']')
            course.click()
            break
        except:continue

    oldwindow  = browser.current_window_handle
    newwindow = browser.window_handles

    for w in newwindow:
    #switch focus to child window
        if(w!=oldwindow):
            browser.switch_to.window(w)
    counter = 0
    while True:
        try:
            if counter<10000:
                counter =counter + 1
                denymicandcamera = browser.find_element(by = 'xpath', value ='//button[@aria-label=\'Cancel microphone and camera setup\']')
                denymicandcamera.click()
                break
            else:
                break
        except:continue

    counter  = 0
    while True:
        try:
            if counter<10000:
                counter = counter + 1
                denytutorial = browser.find_element(by = 'xpath', value ='//button[@aria-label=\'Close announcement\']')
                denytutorial.click()
                break
            else:
                break
        except:continue

    # close class
    wait_time = end_time - datetime.now()
    wait_time = wait_time.total_seconds()
    print('class ends in : '+str(wait_time))

    try:
        time.sleep(wait_time)
    except Exception as e:
        pass

    browser.quit()
    print('class closed')

def get_weekday():
    return datetime.today().strftime('%A')


if __name__ == '__main__':
    # YOu may need to change these acc to your requirements
    courseid_BDS_Lab_Grp_A = 'course-list-course-_23296_1'
    course_id_CL_SEC_LAB_GRP_A = 'course-list-course-_23300_1'
    courseid_OPN_ELE = 'course-list-course-_22314_1'
    courseid_CL_SEC  = 'course-list-course-_23298_1'
    course_id_CAP_PRO = 'course-list-course-_23313_1'
    course_id_BD_SEC = 'course-list-course-_23295_1'
    #This is my timetable but you can add your own time table
    if get_weekday() == 'Tuesday':
        while datetime.now()<datetime.now().replace(hour=15, minute=30):
            if datetime.now()>=datetime.now().replace(hour=9, minute=47) and datetime.now()<datetime.now().replace(hour=10, minute=45):
                startclass('CS LAB',course_id_CL_SEC_LAB_GRP_A,datetime.now().replace(hour=10, minute=45) )
            elif datetime.now()>=datetime.now().replace(hour=10, minute=47) and datetime.now()<datetime.now().replace(hour=11, minute=45):
                startclass('CS LAB',course_id_CL_SEC_LAB_GRP_A,datetime.now().replace(hour=11, minute=45) )
            elif datetime.now()>=datetime.now().replace(hour=13, minute=32) and datetime.now()<datetime.now().replace(hour=14, minute=30):
                startclass('Big Data Lab',courseid_BDS_Lab_Grp_A,datetime.now().replace(hour=14, minute=30) )
            elif datetime.now()>=datetime.now().replace(hour=14, minute=32) and datetime.now()<datetime.now().replace(hour=15, minute=30):
                startclass('Big Data Lab',courseid_BDS_Lab_Grp_A,datetime.now().replace(hour=15, minute=30) )
                break
            else:
                print('waiting for class')
                time.sleep(30)
                continue
    if get_weekday() == 'Wednesday':
        while datetime.now()<datetime.now().replace(hour=16, minute=30):
            if datetime.now()>=datetime.now().replace(hour=10, minute=47) and datetime.now()<datetime.now().replace(hour=11, minute=45):
                startclass('Big Data',course_id_BD_SEC,datetime.now().replace(hour=11, minute=45) )
            elif datetime.now()>=datetime.now().replace(hour=13, minute=32) and datetime.now()<datetime.now().replace(hour=14, minute=30):
                startclass('Big Data',course_id_BD_SEC,datetime.now().replace(hour=14, minute=30) )
            elif datetime.now()>=datetime.now().replace(hour=14, minute=32) and datetime.now()<datetime.now().replace(hour=15, minute=30):
                startclass('OE',courseid_CL_SEC,datetime.now().replace(hour=15, minute=30) )
            elif datetime.now()>=datetime.now().replace(hour=15, minute=32) and datetime.now()<datetime.now().replace(hour=16, minute=30):
                startclass('Cloud Sec',courseid_CL_SEC,datetime.now().replace(hour=16, minute=30) )
                break
            else:
                print('waiting for class')
                time.sleep(30)
                continue
    elif get_weekday() == 'Thursday':
        while datetime.now()<datetime.now().replace(hour=16, minute=30):
            if datetime.now()>=datetime.now().replace(hour=9, minute=47) and datetime.now()<datetime.now().replace(hour=10, minute=45):
                startclass('Capstone project',course_id_CAP_PRO,datetime.now().replace(hour=10, minute=45) )
            elif datetime.now()>=datetime.now().replace(hour=11, minute=47) and datetime.now()<datetime.now().replace(hour=12, minute=45):
                startclass('Cloud Security',courseid_CL_SEC,datetime.now().replace(hour=12, minute=45) )
            elif datetime.now()>=datetime.now().replace(hour=13, minute=32) and datetime.now()<datetime.now().replace(hour=14, minute=30):
                startclass('Cloud Security',courseid_CL_SEC,datetime.now().replace(hour=14, minute=30) )
            elif datetime.now()>=datetime.now().replace(hour=14, minute=32) and datetime.now()<datetime.now().replace(hour=15, minute=30):
                startclass('OE',courseid_OPN_ELE,datetime.now().replace(hour=15, minute=30) )
            elif datetime.now()>=datetime.now().replace(hour=15, minute=32) and datetime.now()<datetime.now().replace(hour=16, minute=30):
                startclass('Big Data Security',course_id_BD_SEC,datetime.now().replace(hour=16, minute=30) )
                break
            else:
                print('waiting for class')
                time.sleep(30)
                continue

    elif get_weekday() == 'Friday':
        while datetime.now()<=datetime.now().replace(hour=15, minute=30):
            if datetime.now()>=datetime.now().replace(hour=14, minute=32) and datetime.now()<datetime.now().replace(hour=15, minute=30):
                startclass('OE',courseid_OPN_ELE,datetime.now().replace(hour=15, minute=30) )
                break
            else:
                print('waiting for class')
                time.sleep(30)
                continue
    print('class Finished')
