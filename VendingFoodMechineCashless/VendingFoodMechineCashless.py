class NFAFoodVendingMachine:
    def __init__(self):
        self.state = 'q0'
        self.balance = 0
        self.food_prices = {
            'lays': 9000,
            'chitato': 8000,
            'cheetos': 10000
        }
        self.selected_food = None

    def select_food(self, food):
        if self.state == 'q0':
            if food in self.food_prices:
                self.selected_food = food
                self.state = 'q1'
                print(f"Makanan {food} dipilih.")
            else:
                print("Makanan tidak ada.")
        else:
            print("Tidak bisa memilih makanan di state ini.")

    def confirm_selection(self):
        if self.state == 'q1':
            self.state = 'q4'
            print("Pilih pembayaran: qris.")
        else:
            print("Tidak bisa mengkonfirmasi pada state ini.")

    def select_payment_method(self, method):
        if self.state == 'q4':
            if method == 'qris':
                self.state = 'q8'
                print(f"Metode pembayaran {method} dipilih.")
            else:
                print("Hanya pembayaran qris yang diterima.")
        else:
            print("Tidak bisa mengkonfirmasi pada state ini.")

    def scan_qr_code(self, balance):
        if self.state == 'q8':
            if balance >= self.food_prices[self.selected_food]:
                self.state = 'q10'
                print("Pembayaran qris berhasil.")
            else:
                self.state = 'q12'
                print("Saldo tidak cukup. Pembayaran gagal.")
        else:
            print("Tidak bisa memindai QR code pada state ini.")

    def verify_payment(self):
        if self.state in ['q10']:
            self.state = 'q11'
            print("Makanan dikeluarkan.")
        else:
            print("Tidak bisa memverifikasi pembayaran pada state ini.")

    def reset(self):
        if self.state in ['q11', 'q12']:
            self.state = 'q0'
            self.balance = 0
            self.selected_food = None
            print("Mesin direset.")
        else:
            print("Tidak bisa mereset mesin pada state ini.")

def run_food_vending_machine():
    vending_machine = NFAFoodVendingMachine()

    # Memilih makanan
    print("Select a food (lays Rp9000 / chitato Rp8000 / cheetos Rp10000):")
    selection = input().strip().lower()
    vending_machine.select_food(selection)
    vending_machine.confirm_selection()

    # Memilih metode pembayaran
    print("Select payment method (qris):")
    payment_method = input().strip().lower()
    vending_machine.select_payment_method(payment_method)

    # Memindai QR code
    print("Scan QR code (masukkan saldo):")
    balance = int(input().strip())
    vending_machine.scan_qr_code(balance)

    # Verifikasi pembayaran dan keluarkan makanan
    vending_machine.verify_payment()

    # Reset mesin
    vending_machine.reset()

if __name__ == "__main__":
    run_food_vending_machine()
