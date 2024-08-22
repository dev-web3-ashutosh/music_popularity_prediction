# music_popularity_prediction
This project uses Spotify data and python libraries like pandas, matplotlib, seaborn, etc to find a correlation between a soundtrack's 'Popularity' and its various features. It further uses this information to create a Machine Learning model which predicts the Popularity score for future soundtracks.
<br></br>
Libraries used -
<ul><li>pandas</li><li>matplotlib.pyplot</li><li>seaborn</li><li>sklearn</li></ul>
<br></br>
1. Pandas library is used to read the csv file and a complete list of all the features associated with each track alongwith its count and data type is as shown below:
<br></br>
<img width="354" alt="data_info" src="https://github.com/user-attachments/assets/3bdfab77-d8f7-4f8a-bedf-3816370250f1">
<br></br>
2. Some of the features are explained below:
<br></br>
<img width="619" alt="data_features" src="https://github.com/user-attachments/assets/55a37a29-f79c-4b10-a170-2ed0c93ad679">
<br></br>
3. To gain initial perspective, we take 5 features and use matplotlib and seaborn libraries to visualize the relation between each of these and the target variable 'Popularity'.  The scatter plots are shown below:
<br></br>
<img width="500" alt="p_vs_energy" src="https://github.com/user-attachments/assets/49823563-e7ba-45f2-ba4b-70732a738651">
<br></br>
<img width="500" alt="p_vs_valence" src="https://github.com/user-attachments/assets/fbdade38-7975-4d45-a133-cbc30d749f18">
<br></br>
<img width="500" alt="p_vs_danceability" src="https://github.com/user-attachments/assets/f030dadc-2126-45fe-9a5c-028ba8df359c">
<br></br>
<img width="500" alt="p_vs_loudness" src="https://github.com/user-attachments/assets/9eebf2ef-1ff3-49c4-ae73-a414f8204549">
<br></br>
<img width="500" alt="p_vs_acousticness" src="https://github.com/user-attachments/assets/a81e4bc6-0f3c-4309-b38e-2eca296ea4de">
<br></br>
4. Visually inspecting the graphs above gives us a basic idea about the relation between these features and Popularity.
<ul>
<li>Energy and Danceability have a <b>positive relation</b> with Popularity</li>
<li>Similarly, Popularity seems to <b>fade away</b> if Loudness is too low or if Acousticness is increased</li>
<li>Valence has an unclear relation and hence suggests that the positivity associated with a soundtrack <b>does not impact Popularity much</b></li>
</ul>
<br></br>
5. Now it's time to see the correlation between all the features using a heatmap.
For now, just focus on the 1st column in the heatmap. Remember that brighter colors (red) mean a strong relation with the target feature (Popularity in our case) and cooler  or   darker colors (blue) mean a weak or less effective relation.
<br></br>
<img width="620" alt="heatmap_correlation_matrix" src="https://github.com/user-attachments/assets/7d28a051-7f3f-4b2b-8519-6c8c71332849">
<br></br>
6. Now let's have a look at the distribution of the sample features.
<br></br>
<img width="500" alt="[Distribution of Energy" src="https://github.com/user-attachments/assets/1fab60da-06c6-47e9-a153-f3a522d43816">
<br></br>
<img width="500" alt="[Distribution of Danceability" src="https://github.com/user-attachments/assets/86d16fa0-c428-4f76-87b7-1548aa867cf8">
<br></br>
<img width="500" alt="[Distribution of Loudness" src="https://github.com/user-attachments/assets/b4e86740-d540-4976-a7f1-e98ee4fc7d71">
<br></br>
<img width="500" alt="[Distribution of Acousticness" src="https://github.com/user-attachments/assets/01b7aecb-6f97-48f3-8765-3784760b00eb">
<br></br>
<img width="500" alt="[Distribution of Valence" src="https://github.com/user-attachments/assets/6cdc1feb-b75c-412c-87a6-3a415b894b75">
<br></br>
7. 







