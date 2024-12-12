from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Route untuk halaman utama (index)
@app.route('/')
def home():
    return render_template('index.html')  # Menampilkan halaman index.html yang berisi form

# Route untuk menangani POST request pada form sign-up
@app.route('/submit', methods=['POST'])
def submit():
    # Mendapatkan data yang dikirim dari form
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    # Validasi sederhana
    if not name or not email or not password:
        return "Error: Semua field wajib diisi!", 400

    # Menangani data yang diterima
    # Di sini Anda bisa menambahkan kode untuk menyimpan data ke database, dll.

    # Kembali ke halaman utama setelah form berhasil disubmit
    return f"Sign Up berhasil! Nama: {name}, Email: {email}"

if __name__ == '__main__':
    app.run(debug=True)
