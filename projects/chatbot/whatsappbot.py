import time
import datetime
import random
import nltk
# import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from time import sleep
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfTransformer
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.metrics import classification_report
# from sklearn.model_selection import train_test_split
# from sklearn.pipeline import Pipeline


# messages = [line.rstrip() for line in open('/Users/Aziz/Desktop/chatbot/SMSSpamCollection')]

driver = webdriver.Chrome('/Users/Aziz/Desktop/chatbot/chromedriver') # change path to chromedriver
driver.get('https://web.whatsapp.com')
sleep(10)
wait = WebDriverWait(driver, 600)
target = '"Code(ine) and Sprite"' # change name to the chat / group chat
# target = '"El chato"'
x_arg = ' //span[contains(@title, ' + target + ')]'
target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
target.click()
sleep(2)
actions = ActionChains(driver)
driver.implicitly_wait(30)
# actions.send_keys('**beep**\nAzBot initialising\nType *@Azbot !commands* for a list of the available commands'+ u'\ue007').perform()
# actions.send_keys('Hello ' + messager + ". Type *@Azbot !commands* for a list of the available commands " + u'\ue007').perform()
newsTime = ""
alive = 1

# messages = pd.read_csv('/Users/Aziz/Desktop/chatbot/SMSSpamCollection', sep='\t',names=["label", "message"])
# messages['length'] = messages['message'].apply(len)
# def text_process(mess):
#     """
#     Takes in a string of text, then performs the following:
#     1. Remove all punctuation
#     2. Remove all stopwords
#     3. Returns a list of the cleaned text
#     """
#     # Check characters to see if they are in punctuation
#     nopunc = [char for char in mess if char not in string.punctuation]

#     # Join the characters again to form the string.
#     nopunc = ''.join(nopunc)
    
#     # Now just remove any stopwords
#     return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
# bow_transformer = CountVectorizer(analyzer=text_process).fit(messages['message'])
# messages_bow = bow_transformer.transform(messages['message'])
# tfidf_transformer = TfidfTransformer().fit(messages_bow)
# messages_tfidf = tfidf_transformer.transform(messages_bow)
# spam_detect_model = MultinomialNB().fit(messages_tfidf, messages['label'])
# all_predictions = spam_detect_model.predict(messages_tfidf)
# msg_train, msg_test, label_train, label_test = train_test_split(messages['message'], messages['label'], test_size=0.2)

# pipeline = Pipeline([
#     ('bow', CountVectorizer(analyzer=text_process)),  # strings to token integer counts
#     ('tfidf', TfidfTransformer()),  # integer counts to weighted TF-IDF scores
#     ('classifier', MultinomialNB()),  # train on TF-IDF vectors w/ Naive Bayes classifier
# ])
# pipeline.fit(msg_train,label_train)
# predictions = pipeline.predict(msg_test)
# print(classification_report(predictions,label_test))

while True:

    sleep(2)
    currentTime = datetime.datetime.now().strftime("%H") + ":" + datetime.datetime.now().strftime("%M")
    currentTimeDate = datetime.datetime.now().strftime("%H") + ":" + datetime.datetime.now().strftime("%M") +', ' +datetime.datetime.now().strftime("%d") +'/' + datetime.datetime.now().strftime("%m") + '/' + datetime.datetime.now().strftime("%Y")
    mentionBubble = driver.find_elements_by_class_name("_274yw")
    element = driver.find_elements_by_class_name("_18lLQ")
    messager = mentionBubble[-1].get_attribute('innerHTML').split("] ")[1].split(":")[0]
    try:
        if alive == 1:
            if mentionBubble[-1].text.split("\n")[-1] == currentTime and messager != 'Az' :
                if any([item in ['yo','wag1','yo az','wys','whats good','oi'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    randNum = random.randrange(6)
                    if randNum == 0:
                        actions = ActionChains(driver)
                        actions.send_keys('Yo whats good' + u'\ue007').perform()
                    elif randNum == 1:
                        actions = ActionChains(driver)
                        actions.send_keys('Yo' + u'\ue007').perform()
                    elif randNum == 2:
                        actions = ActionChains(driver)
                        actions.send_keys('Wag1' + u'\ue007').perform()
                    elif randNum == 3:
                        actions = ActionChains(driver)
                        actions.send_keys('Oz boss' + u'\ue007').perform()
                    elif randNum == 4:
                        actions = ActionChains(driver)
                        actions.send_keys('o dis' + u'\ue007').perform()
                    elif randNum == 5:
                        actions = ActionChains(driver)
                        actions.send_keys('yo g' + u'\ue007').perform()
                    elif randNum == 6:
                        actions = ActionChains(driver)
                        actions.send_keys('whats good bro' + u'\ue007').perform()
                elif mentionBubble[-1].text.lower().split("\n")[-2] == '!joke':
                    randNum = random.randrange(4)
                    if randNum == 0:
                        actions = ActionChains(driver)
                        actions.send_keys("I'm just a bot and don't have any concept of jokes." + u'\ue007').perform()
                        sleep(3)
                        actions = ActionChains(driver)
                        actions.send_keys("Just kidding, you're the joke in this chat" + u'\ue007').perform()
                    elif randNum == 1:
                        actions = ActionChains(driver)
                        actions.send_keys("What did one bot say to the other bot?" + u'\ue007').perform()
                        sleep(2)
                        actions = ActionChains(driver)
                        actions.send_keys("01100110 01110101 01100011 01101011 00100000 01100001 01110010 01110011 01100101 01101110 01100001 01101100" + u'\ue007').perform()
                    elif randNum == 2:
                        actions = ActionChains(driver)
                        actions.send_keys("Imagine being so bored that you want to hear jokes from a bot" + u'\ue007').perform()
                    elif randNum == 3:
                        actions = ActionChains(driver)
                        actions.send_keys("Look at arsenal's trophy cabinet if you want a proper laugh" + u'\ue007').perform()
                    elif randNum == 4:
                        actions = ActionChains(driver)
                        actions.send_keys('A Programmer was walking out of door for work, his wife said “while you’re out, buy some milk” and he never came home.' + u'\ue007').perform()
                elif 'gym' in mentionBubble[-1].text.lower().split("\n")[-2].split():
                    randGym = random.randrange(2)
                    if randGym == 0:
                        actions = ActionChains(driver)
                        actions.send_keys("Oz on going gym" + u'\ue007').perform()
                    elif randGym == 1:
                        actions = ActionChains(driver)
                        actions.send_keys("Murked from gym ngl" + u'\ue007').perform()
                    elif randGym == 2:
                        actions = ActionChains(driver)
                        actions.send_keys("gym at 8am is so calm tho ngl" + u'\ue007').perform()
                elif any([item in ['weather','temperature','hot'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    randGym = random.randrange(2)
                    if randGym == 0:
                        actions = ActionChains(driver)
                        actions.send_keys("the weather is mad recently" + u'\ue007').perform()
                    elif randGym == 1:
                        actions = ActionChains(driver)
                        actions.send_keys("this weather is so bless" + u'\ue007').perform()
                    elif randGym == 2:
                        actions = ActionChains(driver)
                        actions.send_keys("need to move to a country that has this weather all the time ngl" + u'\ue007').perform()
                elif any([item in ['jaja','jajaja','jajajaja'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    actions = ActionChains(driver)
                    actions.send_keys("jajaja" + u'\ue007').perform()
                elif mentionBubble[-1].text.lower().split("\n")[-2] == '!commands':
                    actions = ActionChains(driver)
                    actions.send_keys("Type *!joke* for a joke" + u'\ue007')
                    actions.send_keys("Type *!date* for the todays date" + u'\ue007')
                    actions.send_keys("Type *!news* for some of the latest headlines" + u'\ue007').perform()
                elif mentionBubble[-1].text.lower().split("\n")[-2] == '!news' and newsTime != currentTime:
                    actions = ActionChains(driver)
                    actions.send_keys("Fetching the top 5 headlines..." + u'\ue007').perform()
                    mainWindow = driver.current_window_handle
                    newsObjects = []
                    driver.execute_script("window.open('https://uk.reuters.com/news/world', 'tab2');")
                    driver.switch_to.window("tab2")
                    sleep(2)
                    newsTitles = driver.find_elements_by_class_name("story-title")
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
                    actions.send_keys("The current time and date is: " + currentTimeDate + " in the UK"+ u'\ue007').perform()
                elif mentionBubble[-1].text.lower().split("\n")[-2] == 'is this aziz':
                    actions = ActionChains(driver)
                    actions.send_keys("maybe"+ u'\ue007').perform()
                elif mentionBubble[-1].text.lower().split("\n")[-2] == 'is this az':
                    actions = ActionChains(driver)
                    actions.send_keys("maybe"+ u'\ue007').perform()    
                elif mentionBubble[-1].text.lower().split("\n")[-2] == 'is this bot':
                    actions = ActionChains(driver)
                    actions.send_keys("maybe"+ u'\ue007').perform()
                elif mentionBubble[-1].text.lower().split("\n")[-2] == 'skn':
                    actions = ActionChains(driver)
                    actions.send_keys("skn" + u'\ue007').perform()
                elif any([item in ['lool','loool','looool'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    actions = ActionChains(driver)
                    actions.send_keys("loool" + u'\ue007').perform()
                elif any([item in ['swr','swear','swrr','swrrr','swearr'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    actions = ActionChains(driver)
                    actions.send_keys("say kusmeh" + u'\ue007').perform()
                elif any([item in ['thief'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    actions = ActionChains(driver)
                    actions.send_keys("ukthiefseller" + u'\ue007').perform()
                elif any([item in ['ps4','ps','playstation','cod','rl','warzone'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    actions = ActionChains(driver)
                    actions.send_keys("ooz on" + u'\ue007').perform()
                elif any([item in ['corona','coronavirus','covid'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    actions = ActionChains(driver)
                    actions.send_keys("ooz got coronavirus" + u'\ue007').perform()
                elif any([item in ['bot','bots'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    actions = ActionChains(driver)
                    actions.send_keys("no bots here g" + u'\ue007').perform()
                elif any([item in ['boris'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    actions = ActionChains(driver)
                    actions.send_keys("boris is tapped, ugly yute" + u'\ue007').perform()
                elif any([item in ['samsung','android','pixel','iphone'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    actions = ActionChains(driver)
                    actions.send_keys("androids are dead, iphone>" + u'\ue007').perform()
                elif any([item in ['nandos','dishoom','restaurant'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    actions = ActionChains(driver)
                    actions.send_keys("i swear adrian owes us nandos" + u'\ue007').perform()
                elif any([item in ['homo'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    actions = ActionChains(driver)
                    actions.send_keys("... wtf" + u'\ue007').perform()
                elif any([item in ['bmw'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    actions = ActionChains(driver)
                    actions.send_keys("oz whippin the beemer" + u'\ue007').perform()
                elif any([item in ['merc','benz','mercedes'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    actions = ActionChains(driver)
                    actions.send_keys("oz whippin in the benzo" + u'\ue007').perform()
                elif any([item in ['analysis'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    actions = ActionChains(driver)
                    actions.send_keys("my analysis shows adrian's a wasteman" + u'\ue007').perform()
                elif any([item in ['arsenal'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    actions = ActionChains(driver)
                    actions.send_keys("arsenal are fukn shit" + u'\ue007').perform()
                elif any([item in ['footie','footy','football','fifa'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    actions = ActionChains(driver)
                    actions.send_keys("roooooney" + u'\ue007').perform()
                elif any([item in ['quorn','hungry','food'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    actions = ActionChains(driver)
                    actions.send_keys("kinda hungry still, might have to back a quorn burger in a minute" + u'\ue007').perform()
                elif any([item in ['bruk'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    actions = ActionChains(driver)
                    actions.send_keys("mans active though so..." + u'\ue007').perform()
                elif mentionBubble[-1].text.lower().split("\n")[-2] == 'fuck off':
                    randNum = random.randrange(3)
                    if randNum == 0:
                        actions = ActionChains(driver)
                        actions.send_keys("skn fk u" + u'\ue007').perform()
                    elif randNum ==1:
                        actions = ActionChains(driver)
                        actions.send_keys("You fuck off " + messager + u'\ue007').perform()
                    elif randNum ==2:
                        actions = ActionChains(driver)
                        actions.send_keys("No, I dont think I will" + u'\ue007').perform()
                    elif randNum ==3:
                        actions = ActionChains(driver)
                        actions.send_keys("Fuk u m8" + u'\ue007').perform()
                elif mentionBubble[-1].text.lower().split("\n")[-2] == 'fuck off for real':
                    actions = ActionChains(driver)
                    actions.send_keys("Aite snm, im off" + u'\ue007').perform()
                    alive = 0
                # elif messager == "Adrian New":
                #     actions = ActionChains(driver)
                #     actions.send_keys("Shuttt your mout, pussiiioo" + u'\ue007').perform()
                elif any([item in ['summary','summarize'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    data = [item for item in mentionBubble]
                    print(len(data))
                    print("summary started")
                    try:
                        texts = [item.text.split('\n')[0] for item in data[:50:-1]]
                        print('showing up to 50')
                    except:
                        texts = [item.text.split('\n')[0] for item in data[:10:-1]]
                    vectorizer = CountVectorizer()
                    transformedData = vectorizer.fit_transform(texts)
                    listObject = list(zip(vectorizer.get_feature_names(), np.ravel(transformedData.sum(axis=0))))
                    sortedList = sorted(listObject,key=lambda x: x[1], reverse=True)
                    topics = [item[0] for item in sortedList if item not in stopwords.words('english')]
                    topics = [item for item in topics if item not in ['az','bot','are','in','the','fuck','fuk','you','fuckn','fuck','have','so','shit','to']]
                    topTopics = ', '.join(topics)
                    print(topTopics)
                    actions = ActionChains(driver)
                    actions.send_keys("The top words mentioned recently were: " + topTopics + "." + u'\ue007').perform()
                    print('completed')
                    
            else:
                continue
        elif alive == 0:
            if mentionBubble[-1].text.split("\n")[-1] == currentTime :
                if any([item in ['activate','resurrect','powerup','bootup'] for item in mentionBubble[-1].text.lower().split("\n")[-2].split()]):
                    actions = ActionChains(driver)
                    actions.send_keys("Bot's back bitches" + u'\ue007').perform()
                    alive = 1
                else:
                    continue
            else:
                continue

    except:
        continue


