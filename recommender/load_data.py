import pandas as pd
from sqlalchemy import create_engine, Float, String, Integer

# prep the data
raw_model_output = pd.read_csv("app/similar_images_predictions_2021-01-22_110931.csv")
raw_model_output = raw_model_output.rename(columns={"Unnamed: 0": "id", "image_path":"image_path_short"})
image_metadata_df = raw_model_output[['id', 'base_image', 'similar_image', 'brand', 'description', 'price',
       'image_path_short', 'clothing', 'material', 'pattern', 'fit', 'style',
       'image_path_full']]

engine = create_engine('sqlite:///C:/Users/emuiruri/OneDrive - Capgemini/Data Science Training/pwg-similar-images/recommender/app.db', echo=False)
sqlite_connection = engine.connect()

# Write raw data to the database for the application
image_metadata_df.to_sql(
    "image_metadata",
    engine,
    if_exists="replace",
    index=False,
    chunksize=500,
    dtype={
        'id':Integer,
        'base_image':String,
        'similar_image': String,
        'brand': String,
        'description': String,
        'price': Float,
        'image_path_short': String,
        'clothing': String,
        'material': String,
        'pattern': String,
        'fit': String,
        'style': String,
        'image_path_full': String
    }
)

sqlite_connection.close()