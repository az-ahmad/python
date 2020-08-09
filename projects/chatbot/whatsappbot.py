'''
To use this bot, change the relevant strings on line 21, 25, and 49. The responses can be changed to anything of your choice!
To do: Clean the code and implement proper error handling
'''

import time
import datetime
import random
import nltk
import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

# change path to chromedriver
driver = webdriver.Chrome('/Users/Aziz/Desktop/chatbot/chromedriver')
driver.get('https://web.whatsapp.com')  # open whatsapp web
sleep(10)  # give time for user to scan QR code to sign in
wait = WebDriverWait(driver, 600)
target = '"CHAT NAME / RECIPIENT NAME"'  # change name to the chat / group chat
x_arg = ' //span[contains(@title, ' + target + ')]'  # search for chat name
target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
target.click()  # click on the chat to open it
sleep(2)  # give a few seconds for the messages in the chat to load
actions = ActionChains(driver)
driver.implicitly_wait(30)
newsTime = ""  # empty string that will later store the timestamp of most recent !news command
alive = 1  # can be 1 or 0 denoting if bot is active or not

while True:

    sleep(2)  # code only executes every two seconds, also gives a more 'human' response to messages rather than being instantaneous
    currentTime = datetime.datetime.now().strftime(
        "%H") + ":" + datetime.datetime.now().strftime("%M")
    currentTimeDate = datetime.datetime.now().strftime("%H") + ":" + datetime.datetime.now().strftime("%M") + ', ' + \
        datetime.datetime.now().strftime("%d") + '/' + datetime.datetime.now().strftime("%m") + \
        '/' + datetime.datetime.now().strftime("%Y")
    mentionBubble = driver.find_elements_by_class_name("_274yw")
    messager = mentionBubble[-1].get_attribute('innerHTML').split("] ")[
        1].split(":")[0]
    try:
        if alive == 1:
            # change name to your name on whatsapp
            if mentionBubble[-1].text.split("\n")[-1] == currentTime and messager != 'Az':
                if any([item in ['hello', 'hi', 'yo', 'hey', 'morning', 'sup'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    randNum = random.randrange(6)
                    if randNum == 0:
                        actions = ActionChains(driver)
                        actions.send_keys(
                            'Hey what\'s up' + u'\ue007').perform()
                    elif randNum == 1:
                        actions = ActionChains(driver)
                        actions.send_keys('Yo' + u'\ue007').perform()
                    elif randNum == 2:
                        actions = ActionChains(driver)
                        actions.send_keys('Hi' + u'\ue007').perform()
                    elif randNum == 3:
                        actions = ActionChains(driver)
                        actions.send_keys('Hello!' + u'\ue007').perform()
                    elif randNum == 4:
                        actions = ActionChains(driver)
                        actions.send_keys('Hi there' + u'\ue007').perform()
                    elif randNum == 5:
                        actions = ActionChains(driver)
                        actions.send_keys('Hey how you doing' + u'\ue007').perform()
                    elif randNum == 6:
                        actions = ActionChains(driver)
                        actions.send_keys(
                            'How\'s it going' + u'\ue007').perform()
                elif mentionBubble[-1].text.lower().split("\n")[-2] == '!joke':
                    randNum = random.randrange(4)
                    if randNum == 0:
                        actions = ActionChains(driver)
                        actions.send_keys(
                            "I'm just a bot and don't have any concept of jokes." + u'\ue007').perform()
                        sleep(3)
                        actions = ActionChains(driver)
                        actions.send_keys(
                            "Just kidding, I've got loads!" + u'\ue007').perform()
                    elif randNum == 1:
                        actions = ActionChains(driver)
                        actions.send_keys(
                            "What did one bot say to the other bot?" + u'\ue007').perform()
                        sleep(2)
                        actions = ActionChains(driver)
                        actions.send_keys(
                            "01000010 01101111 01110100 01110011 00100000 01110111 01101001 01101100 01101100 00100000 01110010 01110101 01101100 01100101 00100000 01110100 01101000 01100101 00100000 01110111 01101111 01110010 01101100 01100100" + u'\ue007').perform()
                    elif randNum == 2:
                        actions = ActionChains(driver)
                        actions.send_keys(
                            "Imagine being so bored that you want to hear jokes from a bot" + u'\ue007').perform()
                    elif randNum == 3:
                        actions = ActionChains(driver)
                        actions.send_keys(
                            'A Programmer was walking out of door for work, his wife said “while you’re out, buy some milk” and he never came home.' + u'\ue007').perform()
                elif any([item in ['weather', 'temperature'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    randGym = random.randrange(2)
                    if randGym == 0:
                        actions = ActionChains(driver)
                        actions.send_keys(
                            "The weather has been great recently!" + u'\ue007').perform()
                    elif randGym == 1:
                        actions = ActionChains(driver)
                        actions.send_keys(
                            "I could do with a BBQ in this weather" + u'\ue007').perform()
                    elif randGym == 2:
                        actions = ActionChains(driver)
                        actions.send_keys(
                            "This weather is fantastic" + u'\ue007').perform()
                elif mentionBubble[-1].text.lower().split("\n")[-2] == '!commands':
                    actions = ActionChains(driver)
                    actions.send_keys("Type *!joke* for a joke" + u'\ue007')
                    actions.send_keys(
                        "Type *!date* for the todays date" + u'\ue007')
                    actions.send_keys(
                        "Type *!news* for some of the latest headlines" + u'\ue007').perform()
                elif mentionBubble[-1].text.lower().split("\n")[-2] == '!news' and newsTime != currentTime:
                    actions = ActionChains(driver)
                    actions.send_keys(
                        "Fetching the top 5 headlines..." + u'\ue007').perform()
                    mainWindow = driver.current_window_handle
                    newsObjects = []
                    driver.execute_script(
                        "window.open('https://uk.reuters.com/news/world', 'tab2');")
                    driver.switch_to.window("tab2")
                    sleep(2)
                    newsTitles = driver.find_elements_by_class_name(
                        "story-title")
                    for items in newsTitles[0:5]:
                        newsObjects.append(items.text)
                        newsTime = currentTime
                    driver.switch_to.window(mainWindow)
                    for items in newsObjects:
                        actions = ActionChains(driver)
                        actions.send_keys(items + u'\ue007').perform()
                    continue
                elif mentionBubble[-1].text.lower().split("\n")[-2] == '!date':
                    actions = ActionChains(driver)
                    actions.send_keys("The current time and date is: " +
                                      currentTimeDate + " in the UK" + u'\ue007').perform()
                elif mentionBubble[-1].text.lower().split("\n")[-2] == 'is this aziz':
                    actions = ActionChains(driver)
                    actions.send_keys("maybe" + u'\ue007').perform()
                elif mentionBubble[-1].text.lower().split("\n")[-2] == 'is this a bot':
                    actions = ActionChains(driver)
                    actions.send_keys("maybe" + u'\ue007').perform()
                elif any([item in ['lol', 'haha', 'hahaha'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    actions = ActionChains(driver)
                    actions.send_keys("haha" + u'\ue007').perform()
                elif any([item in ['really?'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    actions = ActionChains(driver)
                    actions.send_keys("yes really!" + u'\ue007').perform()
                elif any([item in ['bot', 'bots'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    actions = ActionChains(driver)
                    actions.send_keys("There's no bots here..." + u'\ue007').perform()
                elif mentionBubble[-1].text.lower().split("\n")[-2] == 'bot power down':
                    actions = ActionChains(driver)
                    actions.send_keys("Bot powering down" + u'\ue007').perform()
                    alive = 0
                elif any([item in ['summary', 'summarize'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    data = [item for item in mentionBubble]
                    try:
                        texts = [item.text.split('\n')[0]
                                 for item in data[:50:-1]]
                        print('showing up to 50')
                    except:
                        texts = [item.text.split('\n')[0]
                                 for item in data[:10:-1]]
                    vectorizer = CountVectorizer()
                    transformedData = vectorizer.fit_transform(texts)
                    listObject = list(
                        zip(vectorizer.get_feature_names(), np.ravel(transformedData.sum(axis=0))))
                    sortedList = sorted(
                        listObject, key=lambda x: x[1], reverse=True)
                    topics = [
                        item[0] for item in sortedList if item not in stopwords.words('english')]
                    topTopics = ', '.join(topics)
                    actions = ActionChains(driver)
                    actions.send_keys(
                        "The top words mentioned recently were: " + topTopics + "." + u'\ue007').perform()
            else:
                continue
        elif alive == 0:
            if mentionBubble[-1].text.split("\n")[-1] == currentTime:
                if any([item in ['activate', 'resurrect', 'powerup', 'bootup'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    actions = ActionChains(driver)
                    actions.send_keys(
                        "Bot's back" + u'\ue007').perform()
                    alive = 1
                else:
                    continue
            else:
                continue

    except:
        continue
