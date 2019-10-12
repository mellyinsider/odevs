#create hub
#java -jar selenium-server-standalone-3.9.1.jar -role hub
#create node
#java -jar selenium-server-standalone-3.9.1.jar -role node -hub

from selenium import webdriver

#bu hub'ı bir chrome driver ile koş diyoruz. (gitbashten registeration linkinin altından aldık linki.)

driver = webdriver.Remote(command_executor='http://192.168.3.216:4432/wd/hub', desired_capabilities={'browserName':'chrome'})

driver.close()

#şuan gittik bi tane driverı kaldırmış olduk. chrome driverı remote'tan kaldırmış olduk. her çalıştırdığında bir tanesini kaldırıyor.