import hashlib
import sys

NUM_KEYS = 512

def parse_lots_key(filename):

    with open(filename, "rb") as priv_file:
        zero_keys = []
        one_keys = []

        for i in range(NUM_KEYS):
            # Read 128 bytes (64 bytes for A_i and 64 bytes for B_i)
            chunk = priv_file.read(64)
            
            # Split into two 64-byte parts
            zero_keys.append(chunk)
        
        for i in range(NUM_KEYS):
            # Read 128 bytes (64 bytes for A_i and 64 bytes for B_i)
            chunk = priv_file.read(64)
            
            # Split into two 64-byte parts
            one_keys.append(chunk)

    return zero_keys, one_keys

def verify(message_fname, signature_fname, public_key_fname):

    pub_list = parse_lots_key(public_key_fname)

    with open(signature_fname, "rb") as sig_file, open(message_fname, "rb") as msg_file:
        
        signature_list = []
        while True:
            bit_sig = sig_file.read(64)
            if not bit_sig:
                break
            signature_list.append(bit_sig)
        
        msg_file_raw = hash_file_sha512_raw(message_file)

        msg_list = []

        for byte_index, byte in enumerate(msg_file_raw):
            for bit_pos in range(7, -1, -1):  # Bit positions (7 to 0)
                bit = (byte >> bit_pos) & 1  # Extract bit (0 or 1)
                msg_list.append(bit)
        
        for index, bit in enumerate(msg_list):
            if pub_list[bit][index] != hashlib.sha512(signature_list[index]).digest():
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