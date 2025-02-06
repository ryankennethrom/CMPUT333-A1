import sys
import hashlib
import os

KEY_SIZE = 64  # 512 bits 
NUM_KEYS = 512  # SHA-512 


def read_private_key(filename):

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




def sign_message(message_filename, private_key_filename):

    with open(message_filename, "rb") as message_file:
        message_contents = message_file.read()
    
    message_hash = hashlib.sha512(message_contents).digest()
    zero_keys, one_keys = read_private_key(private_key_filename)


    signature = bytearray()

    for i in range(NUM_KEYS):
       
        byte_index = i // 8  
        bit_position = 7 - (i % 8)  
        byte_value = message_hash[byte_index]  

        mask = 1 << bit_position
        masked_value = byte_value & mask

   
        if masked_value == 0: 
            bit = 0 
        
        else:
            bit = 1  


        if bit == 0:
            selected_key = zero_keys[i]  
       
        else:
            selected_key = one_keys[i]  


        signature.extend(selected_key)

    with open("signature.lots", "wb") as signature_file:
        signature_file.write(signature)


    with open("signature.lots", "wb") as signature_file:
        signature_file.write(signature)



if __name__ == "__main__":

    message_file = sys.argv[1]
    private_key_file = sys.argv[2]

    sign_message(message_file, private_key_file)

    print("success") #DEBUG --> DELRTE


