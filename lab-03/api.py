from flask import Flask, request, jsonify
from cipher.rsa import RSACipher
from cipher.ecc import ECCCipher

app = Flask(__name__)

# RSA Cipher setup
rsa_cipher = RSACipher()

# Caesar Encrypt
@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.get_json()
    plaintext = data.get('text', '')
    shift = int(data.get('shift', 3))
    encrypted = ''.join(
        chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper()
        else chr((ord(char) - 97 + shift) % 26 + 97) if char.islower()
        else char
        for char in plaintext
    )
    return jsonify({"encrypted": encrypted})


# Caesar Decrypt
@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.get_json()
    ciphertext = data.get('text', '')
    shift = int(data.get('shift', 3))
    decrypted = ''.join(
        chr((ord(char) - 65 - shift) % 26 + 65) if char.isupper()
        else chr((ord(char) - 97 - shift) % 26 + 97) if char.islower()
        else char
        for char in ciphertext
    )
    return jsonify({"decrypted": decrypted})


# RSA Routes
@app.route('/api/rsa/generate_keys', methods=['GET'])
def generate_keys():
    rsa_cipher.generate_keys()
    return jsonify({"message": "RSA Keys generated successfully!"})


@app.route('/api/rsa/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    message = data.get("message", "")
    key_type = data.get("key_type")

    if not message or key_type not in ["public", "private"]:
        return jsonify({"error": "Missing or invalid parameters"}), 400

    key = rsa_cipher.load_keys().get(f"{key_type}_key")
    if not key:
        return jsonify({"error": "Key not found"}), 500

    encrypted_message = rsa_cipher.encrypt(message, key)
    encrypted_hex = encrypted_message.hex()
    return jsonify({"encrypted_message": encrypted_hex})


@app.route('/api/rsa/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    ciphertext_hex = data.get("ciphertext")
    key_type = data.get("key_type")

    if not ciphertext_hex or key_type not in ["public", "private"]:
        return jsonify({"error": "Missing or invalid parameters"}), 400

    key = rsa_cipher.load_keys().get(f"{key_type}_key")
    if not key:
        return jsonify({"error": "Key not found"}), 500

    try:
        ciphertext = bytes.fromhex(ciphertext_hex)
        decrypted_message = rsa_cipher.decrypt(ciphertext, key)
        return jsonify({"decrypted_message": decrypted_message})
    except Exception as e:
        return jsonify({"error": "Decryption failed", "details": str(e)}), 400


@app.route('/api/rsa/sign', methods=['POST'])
def sign():
    data = request.json
    message = data.get("message", "")
    if not message:
        return jsonify({"error": "Missing message"}), 400

    private_key = rsa_cipher.load_keys().get("private_key")
    if not private_key:
        return jsonify({"error": "Private key not found"}), 500

    signature_hex = rsa_cipher.sign(message, private_key).hex()
    return jsonify({"signature": signature_hex})


@app.route('/api/rsa/verify', methods=['POST'])
def verify():
    data = request.json 
    message = data.get("message", "")
    signature_hex = data.get("signature", "")

    if not message or not signature_hex:
        return jsonify({"error": "Missing message or signature"}), 400

    public_key = rsa_cipher.load_keys().get("public_key")
    if not public_key:
        return jsonify({"error": "Public key not found"}), 500

    try:
        signature = bytes.fromhex(signature_hex)
        is_verified = rsa_cipher.verify(message, signature, public_key)
        return jsonify({"is_verified": is_verified})
    except Exception as e:
        return jsonify({"error": "Verification failed", "details": str(e)}), 400


# ECC Cipher setup
ecc_cipher = ECCCipher()

@app.route('/api/ecc/generate_keys', methods=['GET'])
def ecc_generate_keys():
    ecc_cipher.generate_keys()
    return jsonify({'message': 'ECC Keys generated successfully'})


@app.route('/api/ecc/sign', methods=['POST'])
def ecc_sign_message():
    data = request.json
    message = data.get('message', '')
    if not message:
        return jsonify({"error": "Missing message"}), 400

    keys = ecc_cipher.load_keys()
    private_key = keys.get("private_key")
    if not private_key:
        return jsonify({"error": "Private key not found"}), 500

    signature = ecc_cipher.sign(message, private_key)
    return jsonify({'signature': signature.hex()})


@app.route('/api/ecc/verify', methods=['POST'])
def ecc_verify_signature():
    data = request.json
    message = data.get('message', '')
    signature_hex = data.get('signature', '')
    if not message or not signature_hex:
        return jsonify({"error": "Missing message or signature"}), 400

    keys = ecc_cipher.load_keys()
    public_key = keys.get("public_key")
    if not public_key:
        return jsonify({"error": "Public key not found"}), 500

    try:
        signature = bytes.fromhex(signature_hex)
        is_verified = ecc_cipher.verify(message, signature, public_key)
        return jsonify({'is_verified': is_verified})
    except Exception as e:
        return jsonify({"error": "Verification failed", "details": str(e)}), 400


# Run Flask app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
