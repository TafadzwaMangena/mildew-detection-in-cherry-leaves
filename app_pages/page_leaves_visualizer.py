import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread
import itertools
import random


def page_leaves_visualizer_body():

    st.write("## Leaves Visualizer")

    st.info(
        f"The client is interested is visually differentiating a leaf "
        f"infected with powdery mildew from a healthy leaf."
        )

    version = 'v1'
    if st.checkbox("Difference between average and variability image"):
        st.info(
              f"As shown below, the average infected leaf displays white "
              f"spots concentrated at its center, whereas the average healthy "
              f"leaf appears clear."
              )

        avg_infected = plt.imread(
            f"outputs/{version}/avg_var_powdery_mildew.png"
            )
        avg_uninfected = plt.imread(f"outputs/{version}/avg_var_healthy.png")

        st.image(
            avg_infected, caption='Infected Leaf - Average and Variability'
            )
        st.image(
            avg_uninfected, caption='Healthy Leaf - Average and Variability'
            )
        st.write("---")

    if st.checkbox(
            "Differences between average infected and average healthy leaves"):
        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

        st.info(
            f"* We can observe a subtle visual difference between the "
            f"average leaves, though this distinction is not apparent")
        st.image(diff_between_avgs,
                 caption='Difference between average images')

    if st.checkbox("Image Montage"):
        st.write("* To refresh the montage, click the 'Create Montage' button")
        my_data_dir = 'inputs/cherry-leaves_dataset/cherry-leaves'
        labels = os.listdir(my_data_dir + '/validation')
        label_to_display = st.selectbox(label="Select label",
                                        options=labels, index=0)
        if st.button("Create Montage"):
            image_montage(dir_path=my_data_dir + '/validation',
                          label_to_display=label_to_display,
                          nrows=5, ncols=3, figsize=(10, 15))

        st.write("---")


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    sns.set_style("white")
    labels = os.listdir(dir_path)

    if label_to_display in labels:

        images_list = os.listdir(dir_path + '/' + label_to_display)
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(
                f"Decrease nrows or ncols to create your montage. \n"
                f"There are {len(images_list)} in your subset. "
                f"You requested a montage with {nrows * ncols} spaces")
            return

        list_rows = range(0, nrows)
        list_cols = range(0, ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))

        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for x in range(0, nrows*ncols):
            img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(
              f"Width {img_shape[1]}px x Height {img_shape[0]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()

        st.pyplot(fig=fig)

    else:
        print("The label you selected doesn't exist.")
        print(f"The existing options are: {labels}")