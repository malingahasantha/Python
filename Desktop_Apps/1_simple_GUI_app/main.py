# create simple desktop gui app using Tkinter and selenium libraries

from tkinter import *
from tkinter.ttk import *
from selenium import webdriver

root = Tk()
root.geometry("600x600")
root.title("Python Desktop GUI App")

photo_goo = PhotoImage(file = "./img/google.png")
photo_you = PhotoImage(file = "./img/youtube.png")
photo_git = PhotoImage(file = "./img/github.png")

photo_google = photo_goo.subsample(10,10)
photo_youtube = photo_you.subsample(10,10)
photo_github = photo_git.subsample(10,10)

def google():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=option)

    driver.get("https://www.google.com/")

def youtube():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=option)

    driver.get("https://www.youtube.com/")

def github():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=option)

    driver.get("https://www.github.com/")

btn_goo = Button(root, image = photo_google,width=10,command=google).pack()
btn_you = Button(root, image = photo_youtube,width=10,command=youtube).pack()
btn_git = Button(root, image = photo_github,width=10,command=github).pack()

root.mainloop()