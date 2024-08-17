# music_popularity_prediction
This project uses Spotify data and python libraries like pandas, matplotlib, seaborn, etc to find a correlation between a soundtrack's 'Popularity' and its various features. It further uses this information to predict the Popularity score for future soundtracks.

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
![p_vs_energy](https://github.com/user-attachments/assets/186c4959-dfe6-4bb9-a57a-eefafb1f8b74)
<br></br>
![p_vs_valence](https://github.com/user-attachments/assets/73a77453-296d-43db-9127-9301292042f6)
<br></br>
![p_vs_danceability](https://github.com/user-attachments/assets/f030dadc-2126-45fe-9a5c-028ba8df359c)
<br></br>
![p_vs_loudness](https://github.com/user-attachments/assets/9eebf2ef-1ff3-49c4-ae73-a414f8204549)
<br></br>
![p_vs_acousticness](https://github.com/user-attachments/assets/a81e4bc6-0f3c-4309-b38e-2eca296ea4de)
<br></br>
4. Visually inspecting the graphs above gives us a basic idea about the relation between these features and Popularity.
- Energy and Danceability have a <b>positive relation</b> with Popularity
- Similarly, Popularity seems to <b>fade away</b> if Loudness is too low or if Acousticness is increased
- Valence has an unclear relation and hence suggests that the positivity associated with a soundtrack <b>does not impact Popularity much</b>
<br></br>
5. Now it's time to see the correlation between all the features using a heatmap.
  <br></br>
  For now, just focus on the 1st column in the heatmap. Remember that brighter colors (red) mean a strong relation with the target feature (Popularity in our case) and cooler   or   darker colors (blue) mean a weak or less effective relation.
<br></br>
![heatmap_correlation_matrix](https://github.com/user-attachments/assets/7d28a051-7f3f-4b2b-8519-6c8c71332849)
<br></br>









