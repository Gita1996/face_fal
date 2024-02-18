# face_fal
We gathered some persain texts and trained a model using fasttext. We got the text information of a face of person using deepface and calculated the fasttex vectors of the poems and interpretation of Hafez poems and interpretations and the text information of the face and found the most relavant peom and interpretation to the text inforamtion of face using roullete wheel selecion algorithm. Then, designed this project as a fastAPI that gets a picture and returns the most relevant poem and interpretation and dockerized the application. 
To run the fastAPI, we should run fal_Hafez2 python file:
uvicorn fal_Hafez2:app --reload
