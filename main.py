from datetime import datetime
from Controller import *

# Database for storing parking information
parking_database = []

# Constants
PARKING_RATE = 10000  # per minute
MAX_PARKING_DURATION = 4  # in minutes
PENALTY_THRESHOLD_1 = 4  # in minutes
PENALTY_THRESHOLD_2 = 6  # in minutes
PENALTY_RATE_1 = 0.10  # 10%
PENALTY_RATE_2 = 0.25  # 25%
ADMIN_PIN = "1234"  # Admin PIN


def main():
    while True:
        print("\n1. Masuk Area Parkir\n2. Keluar Area Parkir\n3. Admin Parkir\n4. Keluar")
        choice = input("Pilih opsi: ")
        if choice == "1":
            enter_parking_area(parking_database)
        elif choice == "2":
            exit_parking_area(parking_database,PARKING_RATE,PENALTY_THRESHOLD_1,PENALTY_RATE_1, PENALTY_THRESHOLD_2, PENALTY_RATE_2)
        elif choice == "3":
            view_parking_transactions(parking_database,ADMIN_PIN)
        elif choice == "4":
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
