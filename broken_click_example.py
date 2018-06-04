import time

import tools

tool = tools.tools()

#CSS Selectors
broken_try_it_button = "body > button:nth-child(2)"
try_it_button = "#myBtn"

tool.goto_page("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_pushbutton_get")
time.sleep(2)

for x in range(10):
    tool.click_on(try_it_button)

tool.close_selenium()

