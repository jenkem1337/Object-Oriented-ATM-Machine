import time
from data_transfer_objects.SessionManeger.SessionManager import SessionManager
from view.MainATMView.ATMView import ATMView
from view.MainATMView.state.BaseATMViewState import BaseAtmViewState
from view.MainATMView.state.LogoutATMViewState import ATMLogoutViewState
from view.MainATMView.state.MoneyWasTakenState import MoneyWasTakenState
from view.view_components.ATMHomeViewComponent import ATMHomeViewComponent
from view.view_components.AccountBalanceViewComponent import AccountBalanceViewComponent
from view.view_components.DepositViewComponent import DepositViewComponent
from view.view_components.ATMViewErrorViewComponent import ATMViewErrorViewComponent
from view.view_components.MoneyTransferDeniedViewComponent import MoneyTransferDeniedViewComponent
from view.view_components.MoneyTransferViewComponent import MoneyTransferViewComponent
from view.view_components.WithdrawViewComponent import WithdrawViewComponent


class CardInsertedState(BaseAtmViewState):
    def run(self, atmView:ATMView):
        try:
            atmView.printViewComponent(ATMHomeViewComponent(SessionManager().getValue("customer_fullname")))
            selectedIndex = int(input("Yapacağınız İşlemi Seçiniz: "))
            #i feel to lazy refactoring below code :P
            #i may refactor with command design pattern
            if selectedIndex == 1: self.__withdrawHandler(atmView)

            if selectedIndex == 2: self.__depositHandler(atmView)
            
            if selectedIndex == 3: self.__moneyTransferHandler(atmView)
            
            if selectedIndex == 4: self.__getAccountBalace(atmView)
            
            if selectedIndex == 5: self.__lastFiveTransactionHandler(atmView)
            
            if selectedIndex == 6: self.__exitHandler(atmView)
        except Exception as err:
            atmView.printViewComponent(ATMViewErrorViewComponent(err))
            time.sleep(1)

    def __withdrawHandler(self, atmView:ATMView):
                atmView.printViewComponent(WithdrawViewComponent(SessionManager().getValue("balance")))
                input1 = str(input("Bakiyeyi Giriniz Veya Geri Dönmek İçin G Tuşuna Basınız: "))
                if input1 == "G":
                    return
                commandData = {
                    "BANK_ACCOUNT_UUID":SessionManager().getValue("bank_account_uuid"),
                    "AMOUNT": int(input1)
                }
                atmView.executeCommand("WITHDRAW_COMMAND", commandData)
                time.sleep(1)
                atmView.setState(MoneyWasTakenState())
                return
    
    def __depositHandler(self, atmView:ATMView):
                atmView.printViewComponent(DepositViewComponent(SessionManager().getValue("balance")))
                input2 = str(input("Bakiyeyi Giriniz Veya Geri Dönmek İçin G Tuşuna Basınız: "))
                if input2 == "G":
                    return
                commandData = {
                    "BANK_ACCOUNT_UUID":SessionManager().getValue("bank_account_uuid"),
                    "AMOUNT": int(input2)
                }
                atmView.executeCommand("DEPOSIT_COMMAND", commandData)
                time.sleep(1)
                return

    def __lastFiveTransactionHandler(self, atmView: ATMView):
        commandData = {
                "BANK_ACCOUNT_UUID":SessionManager().getValue("bank_account_uuid"),
        }
        atmView.executeCommand("LAST_FIVE_TRANSACTION_COMMAND", commandData)
        return

    def __getAccountBalace(self, atmView: ATMView):
        atmView.printViewComponent(AccountBalanceViewComponent(SessionManager().getValue("balance")))
        return
    
    def __exitHandler(self, atmView:ATMView):
        atmView.setState(ATMLogoutViewState())

    def __moneyTransferHandler(self, atmView:ATMView):
        atmView.printViewComponent(MoneyTransferViewComponent())
        anotherBankAccountNumber = str(input("Para Transfer Etmek İstediğiniz Hesabın Numarasını Giriniz: "))
        amount = int(input("Miktarı Giriniz: "))
        areYouSure = str(input("Parayı Transfer Etmek İçin Emin Misiniz ? (e/y): "))
        
        if areYouSure.strip().upper() == "Y":
            atmView.printViewComponent(MoneyTransferDeniedViewComponent())
            time.sleep(1)
            return
        elif areYouSure.strip().upper() == "E":
            commandData = {
                 "BANK_ACCOUNT_UUID": SessionManager().getValue("bank_account_uuid"),
                 "AMOUNT":amount,
                 "ANOTHER_ACCOUNT_UUID":anotherBankAccountNumber
            }
            atmView.executeCommand("MONEY_TRANSFER_COMMAND", commandData)
        else:
             raise Exception("Hatalı Tuşlama")
        