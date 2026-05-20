import browser
import login
import test_data
import report

#lauch_browser()
print(browser.lauch_browser())

print(login.log("admin","admin@123"))
#print(login.log("admin","admin@123"))
print(test_data.get_test_user())
users=test_data.get_test_user()
for user in users:
    login.log(user["username"],user["password"])
print(report.generate_report())