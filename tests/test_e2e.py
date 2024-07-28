from pageObjects.AO import AO
from pageObjects.Login import Login
from pageObjects.openNewAccount import openNewAccount
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        login = Login(self.driver)
        login.enterUserName().send_keys("Test_demo2")
        login.enterPwd().send_keys("Test_Pwd")
        login.submit().click()

        ao = AO(self.driver)
        accountDetail = ao.getTableData()
        for detail in accountDetail:
            print(detail)

        opennewaccount = openNewAccount(self.driver)
        opennewaccount.newAccountLink().click()
        opennewaccount.account().select_by_index(0)
        opennewaccount.fromAccount().select_by_index(0)
        opennewaccount.accountOpenButton().click()


