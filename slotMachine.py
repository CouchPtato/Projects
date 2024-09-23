import random
import time

class SlotMachine:
    symbols = ["🍒", "🔔", "🍑", "🗿", "🍆"]

    def __init__(self, money=100):
        self.money = money

    def spin(self):
        return random.choices(self.symbols, k = 3)

    def evaluate_spin(self, spin_result):
        if spin_result[0] == spin_result[1] == spin_result[2]:
            if spin_result[0] == "🗿":
                return "jackpot", 50
            return "win", 20
        else:
            return "lose", -10

    def play_round(self):
        if self.money <= 0:
            print("You have no more money! Game over!")
            return False

        print(f"You have {self.money} dollars.")
        bet_amount = 10

        print(f"Spinning... ")
        time.sleep(2)

        spin_result = self.spin()
        print(f"{' | '.join(spin_result)}")

        result, amount = self.evaluate_spin(spin_result)
        if result == "jackpot":
            print("🎉 JACKPOT! You won 50 dollars!")
        elif result == "win":
            print("🎉 You matched all 3 symbols! You win 20 dollars!")
        else:
            print("You lose 10 dollars🤣🤣🤣")
        
        self.money += amount
        return True
    
class HighRiskSlotMachine(SlotMachine):
    
    def evaluate_spin(self, spin_result):
        if spin_result[0] == spin_result[1] == spin_result[2]:
            if spin_result[0] == "🗿":
                return "jackpot", 100
            return "win", 50
        else:
            return "lose", -30

    def play_round(self):
        if self.money <= 0:
            print("You have no more money! Game over!")
            return False

        print(f"You have {self.money} dollars.")
        bet_amount = 20

        print(f"Spinning... ")
        time.sleep(2)

        spin_result = self.spin()
        print(f"{' | '.join(spin_result)}")

        result, amount = self.evaluate_spin(spin_result)
        if result == "jackpot":
            print("🎉 JACKPOT! You won 100 dollars!")
        elif result == "win":
            print("🎉 You matched all 3 symbols! You win 50 dollars!")
        else:
            print("You lose 30 dollars🤣🤣🤣")
        
        self.money += amount
        return True

def main():
  player_name = input("Enter your name: ")
  print(f"Welcome, {player_name}! You start with 100 dollars.")
  
  slot_machine = SlotMachine()

  while True:
      if slot_machine.money <= 0:
          print("You are out of money! Game over!")
          break

      print("\nChoose a mode:")
      print("1. Standard Mode (Lower Risk, Lower Reward)")
      print("2. High Risk Mode (Higher Risk, Higher Reward)")
      print("3. Quit")
      choice = input("Enter your choice (1/2/3): ")

      if choice == '1':
          if slot_machine.money >= 10:
              slot_machine.play_round()
          else:
              print("Not enough money for Standard Mode.")
      elif choice == '2':
          if slot_machine.money >= 20:
              high_risk_machine = HighRiskSlotMachine(slot_machine.money)
              high_risk_machine.play_round()
              slot_machine.money = high_risk_machine.money  
          else:
              print("Not enough money for High Risk Mode.")
      elif choice == '3':
          print(f"Thanks for playing! You leave with {slot_machine.money} dollars.")
          break
      else:
          print("Invalid choice. Please select 1, 2, or 3.")

main()
