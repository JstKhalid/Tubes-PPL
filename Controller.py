from datetime import datetime

def enter_parking_area(parking_database):
    plate_number = input("Enter vehicle number plate: ")
    entry_time = datetime.now().strftime("%H:%M:%S")
    parking_record = {"noplat": plate_number, "waktu_masuk": entry_time, "waktu_keluar": None, "biaya": 0}
    parking_database.append(parking_record)
    print("Silahkan masuk")

def exit_parking_area(parking_database, PARKING_RATE, PENALTY_THRESHOLD_1, PENALTY_RATE_1, PENALTY_THRESHOLD_2, PENALTY_RATE_2):
    plate_number = input("Enter vehicle number plate: ")
    for record in parking_database:
        if record["noplat"] == plate_number and record["waktu_keluar"] is None:
            exit_time = datetime.now().strftime("%H:%M:%S")
            record["waktu_keluar"] = exit_time

            # Calculate parking duration in minutes
            fmt = "%H:%M:%S"
            masuk = datetime.strptime(record["waktu_masuk"], fmt)
            keluar = datetime.strptime(exit_time, fmt)
            parking_duration = (keluar - masuk).seconds // 60

            # Ensure parking duration is calculated correctly if it spans past midnight
            if keluar < masuk:
                parking_duration += 24 * 60  # Add 24 hours in minutes

            # Apply minimum parking duration
            parking_duration = max(1, parking_duration)

            # Calculate fees and penalties
            record["biaya"] = parking_duration * PARKING_RATE
            if parking_duration > PENALTY_THRESHOLD_1:
                penalty_rate = PENALTY_RATE_1 if parking_duration <= PENALTY_THRESHOLD_2 else PENALTY_RATE_2
                record["biaya"] += record["biaya"] * penalty_rate

            print(f"Biaya parkir: Rp {record['biaya']}")
            payment = int(input("Masukkan nominal pembayaran: "))
            if payment >= record["biaya"]:
                print("Terima Kasih")
            else:
                print("Pembayaran tidak cukup")
            return

    print("Plat kendaraan tidak ditemukan atau sudah keluar")


def view_parking_transactions(parking_database, ADMIN_PIN):
    pin = input("Enter Admin PIN: ")
    if pin == ADMIN_PIN:
        for record in parking_database:
            print(record)
    else:
        print("Invalid PIN")