from stegano import lsb
from IPython.display import display, Image

# Menyembunyikan pesan pada gambar
secret = lsb.hide("pinguin.png", "universitas pelita bangsa")
secret.save("pinguin-sec.png")

# Menampilkan gambar yang sudah disisipkan pesan
display(Image(filename='pinguin-sec.png'))

# Mengungkap pesan dari gambar yang telah disisipkan
revealed_message = lsb.reveal("pinguin-sec.png")
print(revealed_message)