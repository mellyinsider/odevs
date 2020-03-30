from selenium.webdriver.common.by import By

class Locators:
    utm_checkbox = (By.CLASS_NAME, ".checkboxDefault.checkboxDefault")
    maven_close = (By.CLASS_NAME, ".icon-close")
    maven_check = (By.CLASS_NAME, ".icon-checked")
    journey_warning_message = (By.CLASS_NAME, ".attributeList.animationHalf")
    journey_search_bar = (By.CSS_SELECTOR, "#page > section > div > div > div > div > div.personalization > div.dataTables_wrapper.no-footer > div > label > input[type=text]")
    select_templste = (By.CLASS_NAME, ".tag.animationHalf") #0.
    stat = (By.CLASS_NAME, ".icon-stats") #1.
    message_box_close_icon = (By.CLASS_NAME, ".icon-close")
    architect_change_icon = (By.CSS_SELECTOR, "#user-attribute-changes-1 > svg > image:nth-child(2)")
    architect_remove_icon = (By.CSS_SELECTOR, "#set-user-attribute-3 > svg > image:nth-child(3)")
    alert_box = (By.CLASS_NAME, ".messageAlertBoxIcon")
    js_edit = (By.CSS_SELECTOR, "#editor-custom-javascript > div.ace_scroller > div > div.ace_layer.ace_text-layer > div > div")


    


