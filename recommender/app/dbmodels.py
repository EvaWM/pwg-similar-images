from app import db

class ImageMetadata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    base_image = db.Column(db.String(120), unique=True)
    similar_image = db.Column(db.String(120), unique=True)
    brand = db.Column(db.String(120), unique=False)
    description = db.Column(db.String(120), unique=False)
    price = db.Column(db.Float(64), unique=False)
    image_path_short = db.Column(db.String(120), unique=False)
    clothing = db.Column(db.String(120), unique=False)
    material = db.Column(db.String(120), unique=False)
    pattern = db.Column(db.String(120), unique=False)
    fit = db.Column(db.String(120), unique=False)
    style = db.Column(db.String(120), unique=False)
    image_path_full = db.Column(db.String(120), unique=True)

    #def __repr__(self):
    #    return '<Image {}>'.format(self.similar_image)

    def __repr__(self):
        return '{}/{}'.format('', self.similar_image)

# unique_image_qry = session.query(ImageMetadata.similar_image.distinct().label("similarimages"))
# unique_image_paths = [row.similar_image for row in unique_image_qry.all()]
# Class.query.with_entities(Class.title).distinct()
# titles = [r.title for r in session.query(Class.title).distinct()]

# # t = ImageMetadata(id=4, image="hello world", brand="gucci", description="myshoes",price=25.1, image_path_short="listicle", clothing="denim", material="denim", pattern="", fit="", style="", image_path_full='''looooooooo
# # ooooooooooooooooooooooong image path''')
#
# class SimilarImages(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     similar_image_path_short = db.Column(db.String(120), unique=True)
#     similar_image_path_full = db.Column(db.String(120), unique=True)
#     base_image_id = db.Column(db.Integer, db.ForeignKey(ImageMetadata.id))
#
#     def __repr__(self):
#         return 'Similar Image {}'.format(self.similar_image_path_full)
#
# # u=ImageMetadata.query.get(4)
# # s = SimilarImages(id=23, similar_image_path_short="hello", similar_image_path_full="full path", base_image_id=u)
