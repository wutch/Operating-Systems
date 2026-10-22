from first_fit import first_fit
from best_fit import best_fit
from worst_fit import worst_fit


def display_results(allocation, remaining):
    print("\nAllocation Results:")

    for i, block in enumerate(allocation):
        if block == -1:
            print(f"Process {i+1}: Not Allocated")
        else:
            print(f"Process {i+1}: Block {block+1}")

    print("Remaining Memory:", remaining)


def main():
    blocks = [100, 500, 200, 300]
    processes = [180, 250, 100]

    print("MEMORY MANAGEMENT SIMULATOR")
    print("---------------------------")

    print("1. First Fit")
    print("2. Best Fit")
    print("3. Worst Fit")

    choice = input("Select Algorithm: ")

    if choice == "1":
        allocation, remaining = first_fit(blocks, processes)

    elif choice == "2":
        allocation, remaining = best_fit(blocks, processes)

    elif choice == "3":
        allocation, remaining = worst_fit(blocks, processes)

    else:
        print("Invalid Choice")
        return

    display_results(allocation, remaining)


if __name__ == "__main__":
    main()