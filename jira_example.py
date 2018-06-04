import time
import tools

#urls
atlassian_login_url = "https://id.atlassian.com/login"
jira_login_url = "https://spotterrf.atlassian.net/secure/Dashboard.jspa"

#login info
USERNAME = "brody.prestwich@spotterrf.com"
PASSWORD = "77maditw77"


# CSS Selectors
username_login_input = "#username"
password_login_input = "#password"
login_button = "#login-submit"
plus_sign_button = "button[class='sc-ghsgMZ jJfqRs']:nth-last-of-type(1)"
summary_input = "#summary"
due_date_input = "#duedate"
assign_to_me_link = "#assign-to-me-trigger"
issue_input = "#issuelinks-issues-textarea"
original_estimate_input = "#timetracking_originalestimate"
sprint_input = "#customfield_10103-field"
create_another_check_box = "#qf-create-another"
create_button = "#create-issue-submit"

#TODO yolo
tool = tools.tools()

tool.goto_page(atlassian_login_url)
time.sleep(3)
tool.clear_and_enter_text(username_login_input, USERNAME)
tool.click_on(login_button)
tool.clear_and_enter_text(password_login_input, PASSWORD)
tool.click_on(login_button)
time.sleep(2)
tool.goto_page(jira_login_url)
time.sleep(3)
# click_on(plus_sign_button)
tool.press_key('c')
tool.clear_and_enter_text(summary_input, "Show off selenium skills")
tool.clear_and_enter_text(due_date_input, "4/Jun/18")
tool.click_on(assign_to_me_link)
tool.clear_and_enter_text(issue_input, "NIO-279")
tool.clear_and_enter_text(original_estimate_input, "3h")
tool.clear_and_enter_text(sprint_input, "NIO Quality")
tool.click_on(create_another_check_box)
time.sleep(5)
tool.close_selenium()
