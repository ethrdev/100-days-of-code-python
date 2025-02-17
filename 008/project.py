## =====================================================
##             Demo: Caesar Cipher
## =====================================================

# Dieser Code demonstriert die Erstellung eines Programms zur Verschlüsselung (encryption) 
# und Entschlüsselung (decryption) mittels des Caesar Cipher.
# Beim Caesar Cipher wird jeder Buchstabe im Text um eine feste Anzahl (shift amount) im Alphabet verschoben.
# Beispiel: Bei einer Verschiebung von 1 wird aus 'a' 'b', aus 'b' 'c', usw.
# Zum Entschlüsseln wird derselbe shift-Wert benötigt, der zur Verschlüsselung verwendet wurde.

## =====================================================
##             Initialisierung und Setup
## =====================================================

# Importiert das Logo aus der Datei art.py und gibt es aus. Dies dient als visuelle Begrüßung des Programms.
from art import logo
print(logo)

## =====================================================
##             Alphabet Definition
## =====================================================

# Definiert eine Liste, die das Alphabet enthält. Diese Liste wird für die Verschiebung der Buchstaben verwendet.
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

## =====================================================
##             Programmsteuerung
## =====================================================

# Initialisiert eine Variable, die bestimmt, ob der Cipher weitergeführt werden soll.
continue_cipher = True

## =====================================================
##             Hauptprogramm-Loop
## =====================================================

# Der Loop läuft, solange der Benutzer das Programm fortsetzen möchte.
while continue_cipher is True:
    
    ## =====================================================
    ##             Benutzereingaben
    ## =====================================================
    # Fragt den Benutzer nach der gewünschten Aktion: 'encode' für Verschlüsselung oder 'decode' für Entschlüsselung.
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    # Fragt den Benutzer nach der Nachricht, die verarbeitet werden soll.
    text = input("Type your message:\n").lower()
    # Fragt den Benutzer nach der Verschiebungszahl (shift number).
    shift = int(input("Type the shift number:\n"))

    ## =====================================================
    ##             Beispiel: Einzelne Funktionsdefinitionen (Auskommentiert)
    ## =====================================================
    # Im Folgenden werden Beispiel-Funktionen zur Verschlüsselung (encrypt) und Entschlüsselung (decrypt) gezeigt.
    # Diese Funktionen sind auskommentiert, da die kombinierte Funktion 'caesar' verwendet wird.
    '''
    def encrypt(original_text, shift_amount):
        output_text = ""
        
        for letter in original_text:
            # Berechnet die neue Position des Buchstabens durch Addition des shift_amount.
            shifted_position = alphabet.index(letter) + shift_amount
            # Verwendet den Modulo-Operator, um bei �berschreitung des Alphabets wieder zum Anfang zu springen.
            shifted_position %= len(alphabet) # 0-25
            output_text += alphabet[shifted_position]

        print(output_text)
    '''
    '''
    def decrypt(original_text, shift_amount):
        output_text = ""
        
        # Iteriert �ber jeden Buchstaben des Textes und berechnet dessen neue Position.
        for letter in original_text:
            # Berechnet die neue Position durch Subtraktion des shift_amount.
            shifted_position = alphabet.index(letter) - shift_amount
            # Setzt die Position mit Hilfe des Modulo-Operators innerhalb der Grenzen des Alphabets.
            shifted_position %= len(alphabet) # 0-25
            output_text += alphabet[shifted_position]

        print(output_text)

    # Aufruf der decrypt-Funktion mit den Benutzereingaben.
    decrypt(original_text=text, shift_amount=shift)
    '''

    ## =====================================================
    ##             Kombinierte Caesar-Funktion
    ## =====================================================
    
    # Diese Funktion kombiniert die Funktionalitäten von Verschlüsselung und Entschlüsselung.
    # Abh�ngig vom Parameter 'encode_or_decode' wird der shift_amount entweder positiv (für encoding) 
    # oder negativ (für decoding) angewendet. Sonderzeichen werden nicht verändert.
    def caesar(encode_or_decode, original_text, shift_amount, continue_cipher):
        
        output_text = ""  
                    
        for letter in original_text:
            # Überprüft, ob der Buchstabe im definierten Alphabet enthalten ist.
            # Falls nicht (z.B. Sonderzeichen wie !, ?, etc.), wird der Buchstabe unverändert übernommen.
            if letter not in alphabet:
                output_text += letter
                
            else:
                # Falls die Entschlüsselung gewünscht ist, wird der shift_amount negiert.
                if encode_or_decode == "decode":
                    shift_amount *= -1
                        
                # Ermittelt die Position des Buchstabens im Alphabet und wendet die Verschiebung an.
                shifted_position = alphabet.index(letter) + shift_amount
                # Stellt sicher, dass die Position innerhalb der Grenzen des Alphabets bleibt.
                shifted_position %= len(alphabet) # 0-25
                output_text += alphabet[shifted_position]

            # Gibt das aktuelle Ergebnis (Teilstring) der Verschlüsselung bzw. Entschlüsselung aus.
            print(f"Here is the {encode_or_decode}d result: {output_text}")
                
    # Aufruf der kombinierten Caesar-Funktion mit den vom Benutzer eingegebenen Werten.
    caesar(encode_or_decode=direction, original_text=text, shift_amount=shift, continue_cipher=continue_cipher)
    
    ## =====================================================
    ##             Programmfortsetzung
    ## =====================================================
    
    # Fragt den Benutzer, ob er eine weitere Verschlüsselung/Entschlüsselung durchführen möchte.
    continue_input = input("Type 'yes' if you want to go again. Otherwise, type 'no'.")
    if continue_input == "no":
        continue_cipher = False
        print("Goodbye")
    else:
        continue_cipher = True