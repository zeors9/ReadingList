import streamlit as st
import pandas as pd
from dataImport import DataImporter

dataList = DataImporter("./data/dataList.csv").load()

st.set_page_config(layout="wide")

st.title("Reading List")

with st.sidebar:
    st.header("Filters")
    media_filter = st.multiselect("Media Type", options=dataList['Media'].unique())
    tag_filter = st.multiselect("Tags", options=set(tag for tags in dataList['Tags'] for tag in tags))
    author_filter = st.multiselect("Authors", options=set(author for authors in dataList['Authors'] for author in authors))
    fun_filter = st.checkbox("Fun", value=False)

filteredData = dataList[
    (dataList['Media'].isin(media_filter) if media_filter else pd.Series(True, index=dataList.index)) &
    (dataList['Tags'].apply(lambda tags: any(tag in tags for tag in tag_filter)) if tag_filter else pd.Series(True, index=dataList.index)) &
    (dataList['Authors'].apply(lambda authors: any(author in authors for author in author_filter)) if author_filter else pd.Series(True, index=dataList.index)) &
    (~dataList['Tags'].apply(lambda tags: "fun" in tags) if not fun_filter else pd.Series(True, index=dataList.index))
]


dataList = st.dataframe(filteredData, 
                        hide_index=True, 
                        column_config={"URL": st.column_config.LinkColumn(label="URL", display_text="Link",validate=True)}
                        )
