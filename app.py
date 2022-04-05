import streamlit as st
import pandas as pd
from utils import *
df = init_table()

st.dataframe(df)