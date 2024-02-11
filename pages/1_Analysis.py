import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 

#st.set_page_config metode yang di gunakan untuk mengubah parameter dari page kita
st.set_page_config(
    page_title="Exploratory Data Analysis App",
    layout="wide"
)

#Persiapan parameter konfigurasi
path_dataset = st.secrets.path_configuration.path_dataset
filename = "pns_jabar.csv"

#baca data
df = pd.read_csv(f"{path_dataset}{filename}")
df.drop(['kode_provinsi','nama_provinsi','satuan'],axis=1,inplace=True)

#container title
with st.container(border=True):
    st.title("Analisa Persebaran PNS Di Lingkungan Pemerintah Provinsi Jawa Barat")
    st.text("Muhammad Okidarsyah")

#tampilkan data
st.dataframe(
    df.sample(10),
    use_container_width=True,
    hide_index=True
    )

#Container
_ = df.groupby(["tahun","jenis_kelamin"], as_index=False)["jumlah_pns"].sum()
table = pd.pivot_table(_, values='jumlah_pns', index=['tahun'], columns=['jenis_kelamin'],
                       aggfunc='sum')


with st.container():
    con2_col_1, con2_col_2 = st.columns([2,1])
    with con2_col_1:
        st.line_chart(table)
    with con2_col_2:
        st.markdown('''
                <style>
                    .analisis_1 {
                        front-side:40px;
                    }
                    </style>
                    ''',
                    unsafe_allow_html=True
                )
        st.markdown('''
                <p class="analisis_1"> melihat grafik disamping, kita dapat melihat bahwa terjadi kenaikan yang cukup signifikan pada tahun 2017 ke tahun 2018</p>''',
                    unsafe_allow_html=True
                )
        
#Container Ke-3
idx = df.groupby(["tahun"])["jumlah_pns"].transform(max) == df['jumlah_pns']
df_max = df[idx]
st.divider()

with st.container():
    con3_col_1, con3_col_2, con3_col_3, con3_col_4 = st.columns(4)
    with con3_col_1:
        temp = df_max[df_max.tahun == 2017]
        st.metric(label=f'{temp["perangkat_daerah"].values[0]} - {temp["tahun"].values[0]}', value=temp["jumlah_pns"].values[0]) 
    with con3_col_2:
        temp = df_max[df_max.tahun == 2018]
        st.metric(label=f'{temp["perangkat_daerah"].values[0]} - {temp["tahun"].values[0]}', value=temp["jumlah_pns"].values[0]) 
    with con3_col_3:
        temp = df_max[df_max.tahun == 2019]
        st.metric(label=f'{temp["perangkat_daerah"].values[0]} - {temp["tahun"].values[0]}', value=temp["jumlah_pns"].values[0]) 
    with con3_col_4:
        temp = df_max[df_max.tahun == 2020]
        st.metric(label=f'{temp["perangkat_daerah"].values[0]} - {temp["tahun"].values[0]}', value=temp["jumlah_pns"].values[0])
               
        st.markdown('''
                <style>
                    .analisis_2 {
                        front-side:20px;
                    }
                    </style>
                    ''',
                    unsafe_allow_html=True
                )
        st.markdown('''
                    <p class="analisis_2"> Dinas Pendidikan selalu menempati posisi
                    teratas jumlah PNS di pemerintahaan provinsi Jawa Barat. Kenaikan cukup 
                    signifikan terjadi di tahun 2018 </p>''',
                    unsafe_allow_html=True
                )                      

with st.container():
    con_4_col_1, con_4_col_2 = st.columns([1,10])
    try :
        tahun = con_4_col_1.text_input("Tahun", max_chars=4)
        temp = df[df['tahun']==int(tahun)]
    except Exception as e :
        st.exception(f'Terjadi Kesalahan: {e}')

    st.dataframe(temp, use_container_width=True)

    for item in df.jenis_kelamin.unique():
        item = st.checkbox(item)



