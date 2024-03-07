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
from dash import ctx
import dash_bootstrap_components as dbc
import base64
import json
from functions import top_words
import copy
from ohtm.topic_evaluation.balkendiagram import bar_dic
from ohtm.topic_evaluation.heatmap_corpus import heatmap_corpus
from interview_chronology_analysis import *
from interview_chronology_analysis.interview_chronology_analysis import chronology_matrix


workingfolder = "C:\\Users\\phili\Dropbox\\Python\\Project\\OHDdash\\OHDdash_files\\"
#workingfolder = "C:\\Users\\bayerschmidt\Dropbox\\Python\\Project\\OHDdash\\OHDdash_files\\"



file_workingfolder = "C:\\Users\\phili\\sciebo - Bayerschmidt, Philipp (bayerschmidt@fernuni-hagen.de)@fernuni-hagen.sciebo.de\\Topic Modeling\\main test\\github_test\\"
#file_workingfolder = "C:\\Users\\bayerschmidt\\sciebo - Bayerschmidt, Philipp (bayerschmidt@fernuni-hagen.de)@fernuni-hagen.sciebo.de\\Topic Modeling\\main test\\github_test\\"


image_filename = workingfolder + "OHD_Logo.png"


