from flask import Flask, render_template, request, redirect, url_for, flash
from DB_Operations import fetch_all_items, insert_item, fetch_item_by_id, update_item, delete_item

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route('/')
def index():
    items = fetch_all_items()
    return render_template('index.html', items=items)

@app.route('/add.html', methods=["POST", "GET"])
def add_item():
    if request.method == 'POST':
        nama = request.form['nama']
        harga = request.form['harga']
        ketersediaan = request.form['ketersediaan']
        insert_item(nama, harga, ketersediaan)
        flash('Item berhasil ditambahkan!')
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<id>', methods=["GET", "POST"])
def edit_item(id):
    item = fetch_item_by_id(id)
    
    if item is None:
        flash("Item tidak ditemukan!")
        return redirect(url_for('index'))

    if request.method == 'POST':
        nama = request.form['nama']
        harga = request.form['harga']
        ketersediaan = request.form['ketersediaan']
        # Update item di database
        update_item(id, nama, harga, ketersediaan)
        flash('Item berhasil diperbarui!')
        return redirect(url_for('index'))
    
    return render_template('edit.html', item=item)

@app.route('/delete/<id>', methods=["POST"])
def delete_item_route(id):
    delete_item(id)
    flash('Item berhasil dihapus!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
