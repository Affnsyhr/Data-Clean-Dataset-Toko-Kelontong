import pandas as pd

def clean_data(df):

    # Ambil kolom penting
    df = df[[
        "No. Faktur",
        "Tanggal",
        "Kode",
        "Item",
        "Harga",
        "Banyak",
        "Total"
    ]]

    # Rename
    df.columns = [
        "no_faktur",
        "tanggal",
        "kode",
        "nama_barang",
        "harga",
        "banyak",
        "total"
    ]

    # Hapus nama barang kosong
    df = df.dropna(subset=["nama_barang"])

    # Cleaning no faktur
    df["no_faktur"] = (
        df["no_faktur"]
        .astype(str)
        .str.strip()
    )

    # Cleaning kode
    df["kode"] = (
        df["kode"]
        .astype(str)
        .str.replace(".0","",regex=False)
        .str.strip()
    )

    # Cleaning angka
    for col in ["harga","banyak","total"]:

        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

        df[col] = (
            df[col]
            .fillna(0)
            .astype(int)
        )

    # Tanggal
    df["tanggal"] = pd.to_datetime(
        df["tanggal"],
        errors="coerce"
    )

    # Kolom waktu
    df["tahun"] = df["tanggal"].dt.year
    df["bulan"] = df["tanggal"].dt.month
    df["minggu"] = (
        df["tanggal"]
        .dt.isocalendar()
        .week
    )

    df["hari"] = (
        df["tanggal"]
        .dt.day_name()
    )

    return df