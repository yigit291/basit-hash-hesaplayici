import hashlib
import json
from datetime import datetime

def calculate_hash(block):
    """
    Verilen bir bloğun SHA-256 hash'ini hesaplar.
    """
    # Blok verisini bir string'e dönüştürüyoruz.
    # json.dumps, Python sözlüğünü düzenli bir string'e çevirir.
    # sort_keys=True, her seferinde aynı hash'i almamızı garantiler.
    block_string = json.dumps(block, sort_keys=True).encode()
    
    # SHA-256 hash nesnesi oluşturup veriyi hash'liyoruz.
    sha = hashlib.sha256(block_string)
    
    # Hash'in hexadecimal (16'lık taban) formatını geri döndürüyoruz.
    return sha.hexdigest()

# Simüle edilmiş bir blok oluşturalım
if __name__ == "__main__":
    # Örnek bir blok yapısı
    ornek_blok = {
        'index': 1,
        'timestamp': str(datetime.now()),
        'transactions': [
            {
                'sender': 'Ali',
                'recipient': 'Veli',
                'amount': 50
            },
            {
                'sender': 'Ayşe',
                'recipient': 'Fatma',
                'amount': 25
            }
        ],
        'previous_hash': '0000000000000000000b9d9ec2b0d8b0f8b1e3b1c8c5c7b3e8a9d8a5c6b4b0d3',
        'nonce': 12345
    }

    # Bloğun hash'ini hesaplayalım
    blok_hashi = calculate_hash(ornek_blok)

    print("--- Örnek Blok Verisi ---")
    print(json.dumps(ornek_blok, indent=4, sort_keys=True))
    print("\n--- Hesaplanan Blok Hash'i ---")
    print(blok_hashi)

    # Veride küçücük bir değişiklik yapıp hash'in ne kadar değiştiğini görelim
    ornek_blok['nonce'] = 12346 # Sadece nonce'ı 1 değiştirdik
    yeni_blok_hashi = calculate_hash(ornek_blok)
    
    print("\n--- Nonce Değiştirildikten Sonraki Yeni Hash ---")
    print(yeni_blok_hashi)
    print("\nGördüğünüz gibi, verideki en ufak bir değişiklik bile hash'i tamamen değiştirdi!")