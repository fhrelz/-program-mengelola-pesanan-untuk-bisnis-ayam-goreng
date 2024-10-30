# # Perulangan
# ulang=2 
# for i in range(ulang): 
#     print("data Ke - " + str(i+1)) 
#     nama=input("Masukkan Nim anda : ") 
#     uts=int(input("Masukkan Nilai UTS anda :")) 
#     uas=int(input("Masukkan Nilai UAS : ")) 
#     cabang=input("Universitas Bina Sarana Informatika Cabang :")
#     print("NIm anda adalah %s nilai UTS anda %i nilai UTS anda %i Ubsi cabang %s" % (nama,uts,uas,cabang)) 
#     print("-------------------------------------\n")

# program pertemuan 5 dasar pemograman
# Program for GEROBAK FRIED CHICKEN
# This program manages orders for a fried chicken business

# Import necessary module
import os

# Define menu items and prices
menu = {
    'D': {'name': 'Dada', 'price': 2500},
    'P': {'name': 'Paha', 'price': 2000},
    'S': {'name': 'Sayap', 'price': 1500}
}

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    """Display the menu to the user."""
    print("GEROBAK FRIED CHICKEN MENU JOGLO")
    print("-" * 35)
    print("Kode  Jenis Potong  Harga")
    print("-" * 35)
    for code, item in menu.items():
        print(f"{code:<5} {item['name']:<12} Rp. {item['price']}")
    print("-" * 35)

def get_order():
    """Get the order details from the user."""
    orders = []
    while True:
        display_menu()
        print("\nMasukkan pesanan Anda (atau 'selesai' untuk mengakhiri):")
        
        jenis = input("Banyak Jenis Makanan Yang Dipesan: ")
        if jenis.lower() == 'selesai':
            break
        
        try:
            jenis = int(jenis)
        except ValueError:
            print("Input tidak valid. Masukkan angka.")
            continue

        for i in range(jenis):
            print(f"\nJenis Ke-{i+1}")
            kode = input("Kode Potong [D/P/S]: ").upper()
            if kode not in menu:
                print("Kode tidak valid. Silakan coba lagi.")
                continue
            
            try:
                banyak = int(input("Banyak Potong: "))
            except ValueError:
                print("Input tidak valid. Masukkan angka.")
                continue

            orders.append((kode, banyak))
        
        break
    
    return orders

def calculate_total(orders):
    """Calculate the total price including tax."""
    subtotal = sum(menu[kode]['price'] * banyak for kode, banyak in orders)
    tax = subtotal * 0.1
    total = subtotal + tax
    return subtotal, tax, total

def display_receipt(orders):
    """Display the receipt with order details."""
    clear_screen()
    print("GEROBAK FRIED CHICKEN JOGLO")
    print("-" * 50)
    print("No.  Jenis Potong  Harga Satuan  Banyak  Jumlah Harga")
    print("-" * 50)
    
    for i, (kode, banyak) in enumerate(orders, 1):
        item = menu[kode]
        subtotal = item['price'] * banyak
        print(f"{i:<4} {item['name']:<13} {item['price']:<13} {banyak:<7} Rp {subtotal}")
    
    subtotal, tax, total = calculate_total(orders)
    print("-" * 50)
    print(f"{'Jumlah Bayar':<41} Rp {subtotal}")
    print(f"{'Pajak 10%':<41} Rp {tax:.0f}")
    print(f"{'Total Bayar':<41} Rp {total:.0f}")

def main():
    """Main function to run the program."""
    while True:
        clear_screen()
        print("Selamat datang di GEROBAK FRIED CHICKEN JOGLO!")
        orders = get_order()
        if orders:
            display_receipt(orders)
        
        again = input("\nApakah Anda ingin memesan lagi? (y/n): ")
        if again.lower() != 'y':
            print("Terima kasih telah membeli makanan Gerobak Fried Chicken Kami!")
            break

if __name__ == "__main__":
    main()