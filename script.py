import os
import cv2
import numpy as np
import datetime
import pillow_heif

folder_path = "image"

def convert_image(folder_path, data):
    try:
        cv2.imwrite(folder_path, data)
        print(f"Gambar berhasil dikonversi dan disimpan di {folder_path}")
    except Exception as e:
        print(f"Terjadi kesalahan saat konversi gambar: {e}")

def list_files_in_directory(directory_path):
    current_datetime = datetime.datetime.now()
    tanggal = current_datetime.day
    bulan = current_datetime.month
    tahun = current_datetime.year % 100

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            h_file = os.path.join(file)
            p_file = h_file.replace(".HEIC", ".PNG")
            f_date = f"{tanggal:02d}{bulan:02d}{tahun:02d}"

            img = pillow_heif.open_heif(f"image/{h_file}", convert_hdr_to_8bit=False, bgr_mode=True)
            np_array = np.asarray(img)

            fp = f"{f_date}\{p_file}"

            if not os.path.exists(f_date):
                os.makedirs(f_date)
            convert_image(fp, np_array)

list_files_in_directory(folder_path)