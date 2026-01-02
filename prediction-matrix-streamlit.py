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
  pid_guide = A
if pid < 90 and pid >= 75:
  pid_guide = B
if pid < 75 and pid >= 25:
  pid_guide = C

if conscore <= 200:
  conscore_guide = 1
if conscore <= 1000 and conscore >= 200:
  conscore_guide = 2
if conscore > 1000:
  conscore_guide = 3

if foldscore <= 15:
  foldscore_guide = A
if foldscore <= 50 and foldscore > 15:
  foldscore_guide = B
if foldscore > 50:
  foldscore_guide = C

st.write(pid_guide, conscore_guide, foldscore_guide)
