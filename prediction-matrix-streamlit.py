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

pid = int(st.text_input('enter your target PID'))
conscore = int(st.text_input('enter your target ConScore'))
foldscore = int(st.text_input('enter your target FoldScore'))

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
#sa_dict = {'A1a':,'A1b':,'A1c':,'A2a':,'A2b':,'A2c':,'A3a':,'A3b':,'A3c':,'B1a':,'B1b':,'B1c':,'B2a':,'B2b':,'B2c':,'B3a':,'B3b':,'B3c':,'C1a':,'C1b':,'C1c':,'C2a':,'C2b':,'C2c':,'C3a':,'C3b':,'C3c':}

#search dictionary based on matrix guide
st.write('delta Tm = ', tm_dict[matrix_guide])
st.write('delta specific activity = ' sa_dict[matrix_guide])
