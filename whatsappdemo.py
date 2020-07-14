from selenium import webdriver
browser = webdriver.Chrome('Chromedriver.exe')
browser.get('http://web.whatsapp.com')
input('Enter any key after QR scan')
name = input('Enter the name')

#going to find span tag title

user = browser.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()

message = 'Hai Welcome'
count = 10

msgbox = browser.find_element_by_class_name('_3uMse')#msg area


for i in range(count):
    msgbox.send_keys(message)
    button = browser.find_element_by_class_name('_1U1xa')  # send button
    button.click()


print('completed')
