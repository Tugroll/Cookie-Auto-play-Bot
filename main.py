from driver_mng import DriverManager
import time



driver = DriverManager()








def ana_dongu():

    last_check_time = time.time()
    count = 0
    while count<3000:
       driver.the_cookie.click()

       current_time = time.time()

    # After five second, run if
       if current_time - last_check_time >= 5:
           count += 5
           driver.find_element()
           print("5 saniyelik kontrol yapılıyor...")

           last_check_time = current_time




ana_dongu()
driver.driver.get_screenshot_as_file("screenshot.png")













#the_cookie.click()

driver.maximize_window()






