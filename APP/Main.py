from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#STEP 1: Get list of team members 
def main():
    team_members = ""
    members = []
    for i in range(5):
        team_members+=input()+"\n"

    team_members = team_members.split("\n")
    team_members.pop()
    for i in team_members:
        team_member = i.split()
        team_member.pop()
        team_member.pop()
        team_member.pop()
        member = " ".join(team_member)
        members.append(member)

    #STEP 2: Run form_input using selenium
    PATH = r"C:\Users\User\Desktop\FILES\Projects\MHChecker\chromedriver.exe"
    driver = webdriver.Chrome(PATH)


    #best to search for id > class > name 
    for i in members:
        print(i)
        driver.get("https://matchhistory.sg.leagueoflegends.com/en/#page/landing-page")
        time.sleep(1)
        search = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/input")
        search.send_keys(i)
        search.send_keys(Keys.RETURN)
        time.sleep(5)
    driver.quit()


    
main()
