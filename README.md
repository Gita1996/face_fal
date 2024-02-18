# face_fal
We gathered some persain texts and trained a model using fasttext. We got the text information of a face of person using deepface and calculated the fasttex vectors of the poems and interpretation of Hafez poems and interpretations and the text information of the face and found the most relavant peom and interpretation to the text inforamtion of face using roullete wheel selecion algorithm. Then, designed this project as a fastAPI that gets a picture and returns the most relevant poem and interpretation and dockerized the application. 
To run the fastAPI, we should run fal_Hafez2 python file:
uvicorn fal_Hafez2:app --reload
We can choose whether the similarity of fasttext vector of text information from face should be checked with fasttext vectors of interpretation or peoms in roullete wheel selection algorithm. We can also enter n, the number of top relevant poems or interpretations in roullete wheel selection algorithm that one of them will be selected.
A sample output can be as the following:
{
  "poem": "روشنی طلعت تو ماه ندارد   پیش تو گل رونق گیاه ندارد   گوشه ابروی توست منزل جانم   خوشتر از این گوشه پادشاه ندارد   تا چه کند با رخ تو دود دل من   آینه دانی که تاب آه ندارد   شوخی نرگس نگر که پیش تو بشکفت   چشم دریده ادب نگاه ندارد   دیدم و آن چشم دل سیه که تو داری   جانب هیچ آشنا نگاه ندارد   رطل گرانم ده ای مرید خرابات   شادی شیخی که خانقاه ندارد   خون خور و خامش نشین که آن دل نازک   طاقت فریاد دادخواه ندارد   گو برو و آستین به خون جگر شوی   هر که در این آستانه راه ندارد   نی من تنها کشم تطاول زلفت   کیست که او داغ آن سیاه ندارد   حافظ اگر سجده تو کرد مکن عیب   کافر عشق ای صنم گناه ندارد",
  "interpretation": "بسیار انسان خوش شانسی هستید. هر کجا می روید بقیه کنار می کشند چون موفقیتتان در آنجا حتمی است. کاری را که انجام می دهید از دست هیچکس بر نمی آید و این به خاطر ذوق و سایقه ی خودتان می باشد. مواظب باشید راه خطا نروید چون دشمنان می خواهند شما را خراب کنند."
}
