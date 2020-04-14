import json
import re

import streamlit as st

from coco.utils import coco_ground_truth_to_dfs
from plots import plot_with_streamlit, plot_image_shape_distribution, plot_bounding_box_distribution


st.sidebar.title("Object Detection Insights")

st.title("Ground Truth")

ground_truth_file = st.sidebar.file_uploader("COCO Ground Truth File", type="json")

if ground_truth_file is not None:

    coco_ground_truth = json.load(ground_truth_file)
    df_images, df_annotations = coco_ground_truth_to_dfs(coco_ground_truth)

    st.header("Images")
    show_image_dataframe = st.checkbox("Show Images DataFrame")
    if show_image_dataframe:
        st.write(df_images)

    plot_with_streamlit(plot_image_shape_distribution, df_images)

    st.header("Annotations")
    show_annotations_dataframe = st.checkbox("Show Annotations DataFrame")
    if show_annotations_dataframe:
        st.write(df_annotations)    

    plot_with_streamlit(plot_bounding_box_distribution, df_annotations)
