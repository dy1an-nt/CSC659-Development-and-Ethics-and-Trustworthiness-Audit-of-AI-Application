class InsufficientFundsError(Exception):
    def __init__(self, balance: float, amount: float):
        self.balance = balance
        self.amount = amount
        self.deficit = amount - balance
        super().__init__(
            f"Insufficient funds: tried to withdraw ${amount:.2f}, "
            f"but balance is only ${balance:.2f} (deficit: ${self.deficit:.2f})"
        )

class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner
        self._balance = initial_balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        print(f"Deposited ${amount:.2f} | New balance: ${self._balance:.2f}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise InsufficientFundsError(self._balance, amount)
        self._balance -= amount
        print(f"Withdrew ${amount:.2f} | New balance: ${self._balance:.2f}")

    @property
    def balance(self) -> float:
        return self._balance

account = BankAccount("Alice", initial_balance=500.00)

try:
    account.deposit(200.00)
    account.withdraw(300.00)
    account.withdraw(600.00)
except InsufficientFundsError as e:
    print(f"\nError caught: {e}")
    print(f"  Account balance: ${e.balance:.2f}")
    print(f"  You are short: ${e.deficit:.2f}")
