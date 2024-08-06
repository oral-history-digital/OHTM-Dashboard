import base64
import copy
from copy import deepcopy
from datetime import datetime
import json
import os
import pickle
from pprint import pprint
import re
import warnings

import dash
from dash import ctx
from dash import Dash, callback, dcc, dash_table, Input, Output, State, MATCH, ALL
from dash import html
import dash_bootstrap_components as dbc
import pandas as pd
from matplotlib import pylab
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from seaborn.matrix import heatmap
import spacy

from interview_chronology_analysis import *
from interview_chronology_analysis.interview_chronology_analysis import chronology_matrix
from interview_chronology_analysis.Narrative_o_Meter import top_global_correlations_json, global_vertical_correlation_search_json, global_horizontal_correlation_search_json
from OHDdash.functions import top_words
from ohtm.topic_evaluation.bar_graph import bar_graph_corpus
from ohtm.topic_evaluation.heatmaps import heatmap_corpus


workingfolder = "C:\\Users\\phili\Dropbox\\Python\\Project\\OHDdash\\OHDdash_files\\"
#workingfolder = "C:\\Users\\bayerschmidt\Dropbox\\Python\\Project\\OHDdash\\OHDdash_files\\"



file_workingfolder = "C:\\Users\\phili\\sciebo - Bayerschmidt, Philipp (bayerschmidt@fernuni-hagen.de)@fernuni-hagen.sciebo.de\\Topic Modeling\\main test\\github_test\\"
#file_workingfolder = "C:\\Users\\bayerschmidt\\sciebo - Bayerschmidt, Philipp (bayerschmidt@fernuni-hagen.de)@fernuni-hagen.sciebo.de\\Topic Modeling\\main test\\github_test\\"


image_filename = workingfolder + "OHD_Logo.png"
