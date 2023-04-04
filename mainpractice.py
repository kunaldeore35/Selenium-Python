from rahulshettypracticepage import Automation

# For Dynamic drop down
# auto_dd = Automation("https://rahulshettyacademy.com/dropdownsPractise/")
# For multiple checkbox,Radio, Alert
auto_mcra = Automation("https://rahulshettyacademy.com/AutomationPractice/")

# auto_dd.dynamicdrop("Ind")

auto_mcra.multicheck()
auto_mcra.multiradio()
auto_mcra.alertbox1("Kunal")
auto_mcra.alertbox2()
auto_mcra.dynamicdrops("Ind")
auto_mcra.dropd()