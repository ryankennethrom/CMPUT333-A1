import os
import hashlib

def generate_lots_keypair():

    # Use a set to store previously generated private key values for uniqueness check
    seen_private_keys = set()

    with open("private_key.lots", "wb") as priv_file, open("public_key.lots", "wb") as pub_file:
        for _ in range(512):
            while True:
                # Generate two 512-bit (64-byte) random values (private keys)
                X_i = os.urandom(64)
                Y_i = os.urandom(64)

                # Store as tuple for uniqueness check
                key_pair = (X_i, Y_i)

                # Ensure this key pair has not been generated before
                if key_pair not in seen_private_keys:
                    seen_private_keys.add(key_pair)  # Mark the pair as seen
                    break  # Exit loop once unique key pair is generated


            # Compute their SHA-512 hashes (public keys)
            A_i = hashlib.sha512(X_i).digest()
            B_i = hashlib.sha512(Y_i).digest()

            # Write the private key pair (X_i, Y_i) as raw bytes
            priv_file.write(X_i)
            priv_file.write(Y_i)

            # Write the public key pair (A_i, B_i) as raw bytes
            pub_file.write(A_i)
            pub_file.write(B_i)

    print("New unique Lamport OTS key pair generated.")

if __name__ == "__main__":
    generate_lots_keypair()
