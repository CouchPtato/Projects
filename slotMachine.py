import random

class SlotMachine:
    symbols = ["🍒", "💎", "🍑", "🍀", "🗿", "🍆"]

    def __init__(self, money=100):
        self.money = money

    def spin(self):
        return random.choices(self.symbols, k = 3)

    def evaluate_spin(self, spin_result):
        if spin_result[0] == spin_result[1] == spin_result[2]:
            if spin_result[0] == "🗿":
                return "jackpot", 100
            return "win", 50
        else:
            return "lose", -10

    def play_round(self):
        if self.money <= 0:
            print("You have no more money! Game over!")
            return False

        print(f"You have {self.money} dollars.")
        bet_amount = 10

        print(f"Spinning... ")
        spin_result = self.spin()
        print(f"{' | '.join(spin_result)}")

        result, amount = self.evaluate_spin(spin_result)
        if result == "jackpot":
            print("🎉 JACKPOT! You won 100 dollars!")
        elif result == "win":
            print("🎉 You matched all 3 symbols! You win 50 dollars!")
        else:
            print("Sorry, you lose 10 dollars.")
        
        self.money += amount
        return True

def main():
    player_name = input("Enter your name: ")
    slot_machine = SlotMachine()

    print(f"Welcome, {player_name}! You start with {slot_machine.money} dollars.")

    while True:
        if slot_machine.money <= 0:
            print("You are out of money! Game over!")
            break

        play = input("Press Enter to spin (or type 'q' to quit): ")
        if play.lower() == 'q':
            print(f"Thanks for playing! You leave with {slot_machine.money} dollars.")
            break

        slot_machine.play_round()


main()
