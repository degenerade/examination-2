import dice


def main():
    die = dice.Dice()
    die.set_sides(int(input("How many faces will the dice have?\n>>> ")))
    num_rolls = int(input("How many rolls do you want to make?\n>>> "))
    for i in range(1, num_rolls+1):
        print(f"Roll {i}: {die.roll_die()}")
    print(f"\nTotal rolls made: {die.get_rolls_made()}")
    print(f"Sum of all rolls made: {die.get_sum_of_all_rolls()}")


if __name__ == '__main__':
    main()
