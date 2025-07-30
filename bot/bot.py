import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

service = Service()
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service, options=options)
driver.get('http://127.0.0.1:5000')



js_dnd = """
function DnD(sourceElement, targetElement) {
    const dragStartEvent = new DragEvent('dragstart', {
        bubbles: true,
        cancelable: true,
        dataTransfer: new DataTransfer()
    });
    
    const dropEvent = new DragEvent('drop', {
        bubbles: true,
        cancelable: true,
        dataTransfer: dragStartEvent.dataTransfer
    });
    
    const dragOverEvent = new DragEvent('dragover', {
        bubbles: true,
        cancelable: true,
        dataTransfer: dragStartEvent.dataTransfer
    });
    
    sourceElement.dispatchEvent(dragStartEvent);
    targetElement.dispatchEvent(dragOverEvent);
    targetElement.dispatchEvent(dropEvent);
    
    return true;
}
var source = arguments[0];
var target = arguments[1];
return DnD(source, target);
"""


time.sleep(1)

button = driver.find_element(By.ID, "button1")
draggable = driver.find_element(By.ID, "piece")
droppable = driver.find_element(By.ID, "puzzle")

i = 0
while(i<50):

    button = driver.find_element(By.ID, "button1")

    ActionChains(driver) \
        .click(button) \
        .perform()

    time.sleep(5)

    draggable = driver.find_element(By.ID, "piece")
    droppable = driver.find_element(By.ID, "puzzle")
    
    result = driver.execute_script(js_dnd, draggable, droppable)

    ActionChains(driver)\
        .drag_and_drop(draggable, droppable) \
        .perform()

    time.sleep(5)

    driver.get('http://127.0.0.1:5000')

    i += 1


# driver.quit()