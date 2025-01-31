import hashlib
import sys


def verify(message_fname, signature_fname, public_key_fname):
    with open(signature_fname, "rb") as sig_file, open(public_key_fname, "rb") as pub_file, open(message_fname, "rb") as msg_file:
        
        signature_list = []
        while True:
            bit_sig = sig_file.read(64)
            if not bit_sig:
                break
            signature_list.append(bit_sig)
        
        pub_list = [[],[]]
        while True:
            # Read 128 bytes (64 bytes for A_i and 64 bytes for B_i)
            chunk = pub_file.read(128)
            if not chunk:
                break  # Stop when the file ends
            
            # Split into two 64-byte parts
            A_i = chunk[:64]
            pub_list[0].append(A_i)
            B_i = chunk[64:]
            pub_list[1].append(B_i)
        
        msg_file_raw = hash_file_sha512_raw(message_file)
        
        msg_list = []

        for byte_index, byte in enumerate(msg_file_raw):
            for bit_pos in range(7, -1, -1):  # Bit positions (7 to 0)
                bit = (byte >> bit_pos) & 1  # Extract bit (0 or 1)
                msg_list.append(bit)
        
        for index, bit in enumerate(msg_list):
            if pub_list[bit][index] != hashlib.sha512(signature[index]).digest():
                print("INVALID")
                return
        print("VALID")
        return

def hash_file_sha512_raw(filename):
    sha512_hash = hashlib.sha512()  # Create SHA-512 hash object
    
    with open(filename, "rb") as file:  # Open file in binary mode
        while chunk := file.read(4096):  # Read in 4KB chunks
            sha512_hash.update(chunk)  # Update hash with file content

    return sha512_hash.digest()  # Return raw bytes

if __name__ == "__main__": 
    # Ensure at least 3 arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python lots_verify.py <message_file> <pub_key_file> <sig_file>")
        sys.exit(1)

    message_file, pub_key_file, sig_file = sys.argv[1], sys.argv[2], sys.argv[3]
    verify(message_file, sig_file, pub_key_file)