import streamlit as st
import pandas as pd
import plotly.express as px
from io import BytesIO

from modules.cleaning import clean_data
from modules.categorization import kategori_barang

# ==========================================
# CONFIG PAGE
# ==========================================
st.set_page_config(
    page_title="Toko Cahaya LKZ",
    page_icon="🏪",
    layout="wide"
)

# ==========================================
# HEADER
# ==========================================
col_logo, col_title = st.columns([1, 12])

with col_logo:
    st.image(
        "assets/bundalogo.jpeg",
        width=120
    )

with col_title:
    st.title("🏪 Sistem Cleaning Data Penjualan")
    st.caption("Toko Kelontong | Data Penjualan Mentah → Data Bersih untuk Looker Studio")

st.markdown("---")

# ==========================================
# UPLOAD
# ==========================================
st.subheader("📂 Upload File Excel")

uploaded_file = st.file_uploader(
    "Unggah file penjualan mentah",
    type=["xlsx"]
)

if uploaded_file:

    df_raw = pd.read_excel(
        uploaded_file,
        header=3
    )

    st.success("✅ File berhasil diunggah")

    if st.button("🚀 Proses Cleaning"):

        # ==================================
        # CLEANING
        # ==================================
        df_clean = clean_data(df_raw)

        df_clean["kategori_barang"] = (
            df_clean["nama_barang"]
            .apply(kategori_barang)
        )

        st.success(
            "✅ Data berhasil dibersihkan dan siap digunakan untuk Looker Studio."
        )

        # ==================================
        # STATISTIK
        # ==================================
        st.markdown("## 📈 Ringkasan Dataset")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Jumlah Transaksi",
                f"{len(df_clean):,}"
            )

        with col2:
            st.metric(
                "Produk Unik",
                f"{df_clean['nama_barang'].nunique():,}"
            )

        with col3:
            st.metric(
                "Jumlah Kategori",
                df_clean["kategori_barang"].nunique()
            )

        with col4:
            st.metric(
                "Periode",
                f"{df_clean['tahun'].min()}-{df_clean['tahun'].max()}"
            )

        st.markdown("---")

        # ==================================
        # GRAFIK
        # ==================================
        st.markdown("## 📊 Distribusi Kategori")

        kategori = (
            df_clean["kategori_barang"]
            .value_counts()
            .reset_index()
        )

        kategori.columns = [
            "Kategori",
            "Jumlah"
        ]

        fig = px.bar(
            kategori,
            x="Kategori",
            y="Jumlah",
            text="Jumlah"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.markdown("---")

        # ==================================
        # DOWNLOAD
        # ==================================
        st.markdown("## ⬇️ Download Hasil")

        csv = df_clean.to_csv(
            index=False
        )

        output = BytesIO()

        with pd.ExcelWriter(
            output,
            engine="openpyxl"
        ) as writer:

            df_clean.to_excel(
                writer,
                index=False
            )

        col_csv, col_excel = st.columns(2)

        with col_csv:

            st.download_button(
                label="📄 Download CSV",
                data=csv,
                file_name="penjualan_clean.csv",
                mime="text/csv",
                use_container_width=True
            )

        with col_excel:

            st.download_button(
                label="📊 Download Excel",
                data=output.getvalue(),
                file_name="penjualan_clean.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )

        st.markdown("---")

        # ==================================
        # TABS
        # ==================================
        tab1, tab2, tab3 = st.tabs([
            "📄 Data Mentah",
            "🧹 Data Clean",
            "⚠️ Produk Belum Terkategorikan"
        ])

        with tab1:

            st.dataframe(
                df_raw,
                use_container_width=True
            )

        with tab2:

            st.dataframe(
                df_clean,
                use_container_width=True
            )

        with tab3:

            lainnya = (
                df_clean[
                    df_clean["kategori_barang"] == "Lainnya"
                ]["nama_barang"]
                .drop_duplicates()
                .sort_values()
            )

            if len(lainnya) > 0:

                st.dataframe(
                    lainnya,
                    use_container_width=True
                )

            else:

                st.success(
                    "✅ Semua produk berhasil dikategorikan."
                )