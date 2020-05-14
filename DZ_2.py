transfer_clock = int(input("Введите время в секундах: "))
hours = transfer_clock // 3600
minutes = (transfer_clock % 3600) // 60
seconds = transfer_clock % 60
print(f"Введенное время: {hours:02d}:{minutes:02d}:{seconds:02d}")
