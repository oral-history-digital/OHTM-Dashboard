import os
import pandas as pd
import re
from matplotlib import pylab
import matplotlib.pyplot as plt
from pprint import pprint
import spacy
from seaborn.matrix import heatmap
import seaborn as sns
from datetime import datetime
import pyLDAvis
import pyLDAvis.gensim_models as gensimvis
import pickle
import plotly.express as px
import warnings
from copy import deepcopy
import dash
from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc
import base64
import json
from functions import top_words
import copy
from ohtm.topic_evaluation.balkendiagram import bar_dic
from ohtm.topic_evaluation.heatmap_corpus import heatmap_corpus

workingfolder = "C:\\Users\\phili\\FAUbox\\Oral History Digital\\Python\\Project\\OHDdash\\OHDdash_files\\"





image_filename = workingfolder + "OHD_Logo.png"


with open(workingfolder + "OHD_complete_pre_150c_80t.json") as f:
    top_dic = json.load(f)


