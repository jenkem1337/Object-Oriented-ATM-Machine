from view.Commands.CommandContext import CommandContext
from view.Commands.DepositCommand import DepositCommand
from view.Commands.LastFiveTransactionCommand import LastFiveTransactionCommand
from view.Commands.LoginCommand import LoginCommand
from view.Commands.TransferMoneyCommand import TransferMoneyCommand
from view.Commands.WithdrawCommand import WithdrawCommand
from view.MainATMView.ATMView import ATMView
from view.MainATMView.state.CardNotInsertedState import CardNotInsertedState
from view.abstract.IViewFactory import IViewFactory
from view.factory.DepositViewFactory import DepositViewFactory
from view.factory.LoginViewFactory import LoginViewFactory
from view.factory.MoneyTransferViewFactory import MoneyTransferViewFactory
from view.factory.TransactionViewFactory import TransactionViewFactory
from view.factory.WithdrawViewFactory import WithdrawViewFactory


class ATMViewFactory(IViewFactory[ATMView]):
    def create(self) -> ATMView:
        loginView   = LoginViewFactory().create()
        depositView = DepositViewFactory().create()
        withdrawView = WithdrawViewFactory().create()
        transactionView = TransactionViewFactory().create()
        moneyTransferView = MoneyTransferViewFactory().create()

        depositCommand = DepositCommand(depositView)
        loginCommand = LoginCommand(loginView)
        withdrawCommand = WithdrawCommand(withdrawView)
        lastFiveTransactionCommand = LastFiveTransactionCommand(transactionView)
        moneyTransferCommand = TransferMoneyCommand(moneyTransferView)
        
        commandContext = CommandContext()
        commandContext.setCommand("LOGIN_COMMAND", loginCommand) \
                    .setCommand("DEPOSIT_COMMAND", depositCommand) \
                    .setCommand("WITHDRAW_COMMAND", withdrawCommand)\
                    .setCommand("LAST_FIVE_TRANSACTION_COMMAND", lastFiveTransactionCommand)\
                    .setCommand("MONEY_TRANSFER_COMMAND", moneyTransferCommand)
        

        atmView = ATMView(CardNotInsertedState(), commandContext)
        
        loginView.setMainView(atmView)
        depositView.setMainView(atmView)
        withdrawView.setMainView(atmView)
        transactionView.setMainView(atmView)
        moneyTransferView.setMainView(atmView)
        return atmView