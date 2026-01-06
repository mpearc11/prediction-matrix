import streamlit as st
from Bio import Blast
from Bio import Align
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from io import StringIO
from Bio import AlignIO
from Bio.Align.Applications import ClustalOmegaCommandline
import pandas as pd
import tempfile
import os
import numpy as np
from pandas import DataFrame

st.title('Prediction Matrix')

st.header('Input PID, ConScore, and FoldScore Values')

pid = float(st.text_input('enter your target PID'))
conscore = float(st.text_input('enter your target ConScore'))
foldscore = float(st.text_input('enter your target FoldScore'))

if pid <= 100 and pid >= 90:
  pid_guide = 'A'
if pid < 90 and pid >= 75:
  pid_guide = 'B'
if pid < 75 and pid >= 25:
  pid_guide = 'C'

if conscore <= 200:
  conscore_guide = '1'
if conscore <= 1000 and conscore >= 200:
  conscore_guide = '2'
if conscore > 1000:
  conscore_guide = '3'

if foldscore <= 15:
  foldscore_guide = 'a'
if foldscore <= 50 and foldscore > 15:
  foldscore_guide = 'b'
if foldscore > 50:
  foldscore_guide = 'c'

matrix_guide = pid_guide + conscore_guide + foldscore_guide
st.write(matrix_guide)

#make dictionary for Tm and specific activity look up
tm_dict = {'A1a':'no change','A1b':'-2.0','A1c':'no change','A2a':'-2.5','A2b':'-7.5','A2c':'+2.5','A3a':'-5.0','A3b':'-10.0','A3c':'+5.0','B1a':'-2.0','B1b':'-5.0','B1c':'-2.0','B2a':'-5.0','B2b':'-10.0','B2c':'+5.0','B3a':'-7.5','B3b':'-12.0','B3c':'+7.5','C1a':'-2.0','C1b':'-7.5','C1c':'-5.0','C2a':'+2.0','C2b':'+10.0','C2c':'+12.0','C3a':'-5.0','C3b':'-7.5','C3c':'+10.0'}
sa_dict = {'A1a':'no change','A1b':'-4.0','A1c':'no change','A2a':'-5.0','A2b':'-8.0','A2c':'-2.0','A3a':'+3.0','A3b':'+5.0','A3c':'+8.0','B1a':'-4.0','B1b':'-6.0','B1c':'no change','B2a':'+2.0','B2b':'-3.0','B2c':'-10.0','B3a':'-2.0','B3b':'no change','B3c':'+4.0','C1a':'no change','C1b':'+2.0','C1c':'+6.0','C2a':'-5.0','C2b':'-10.0','C2c':'-15.0','C3a':'-10.0','C3b':'-12.0','C3c':'-15.0'}

#search dictionary based on matrix guide
st.write('delta Tm = ', tm_dict[matrix_guide])
st.write('delta specific activity = ', sa_dict[matrix_guide])
