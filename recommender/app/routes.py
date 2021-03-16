from app import app,db
from flask import render_template, request, url_for
from app.dbmodels import ImageMetadata
from sqlalchemy import distinct, func


@app.route('/')
@app.route('/home')
def home():
    title = "PWG Image Recommendation Project"
    subtitle = "Welcome to the website"
    return render_template('home.html', title=title, subtitle=subtitle)

@app.route('/about')
def about_the_project():
    return render_template('eval_metrics.html')

@app.route('/explore', methods=['GET', 'POST'])
def explore_images():
    page = request.args.get('page', 1, type=int)
    brand_query = db.session.query(ImageMetadata.brand.distinct().label("brand"))
    brand_list = [row.brand for row in brand_query.all()]
    brand_selected = request.form.get('brand_selected')
    print(brand_selected)

    # RENDERING ALL IMAGES - random selection to avoid showing the same image
    #image_list = ImageMetadata.query.all() # full list with duplicates, same as .distinct() as rows are all unique
    #image_list = ImageMetadata.query.order_by(func.random()).paginate(page, app.config['POSTS_PER_PAGE'], False) # random selection of images

    # SOME DIFFICULTY QUERYING THE DATABASE FOR DISTINCT OUTPUTS
    # image_list = db.session.query(distinct(ImageMetadata.similar_image)).all() # doesn't render
    # query = db.session.query(ImageMetadata.similar_image.distinct().label("similar_image"))
    # image_list = [row.similar_image for row in query.all()] # to get all unique images
    # paginated_list = paginate(query, page, app.config['POSTS_PER_PAGE'], False)
    # image_list = [row.similar_image for row in paginated_list.items]


    # SUCCESS QUERYING WITH SPECIFIC FILTERS. Database Model Class "ImageMetadata" may need updating as no other fields can be returned from image_list.items
    if brand_selected==None:
        image_list = ImageMetadata.query.filter(ImageMetadata.base_image==ImageMetadata.similar_image).paginate(page, app.config['POSTS_PER_PAGE'], False)
        n_images = ImageMetadata.query.filter(ImageMetadata.base_image==ImageMetadata.similar_image).count()
    else:
        image_list = ImageMetadata.query.filter(ImageMetadata.base_image==ImageMetadata.similar_image).filter(ImageMetadata.brand==brand_selected).paginate(page, app.config['POSTS_PER_PAGE'], False)
        n_images = ImageMetadata.query.filter(ImageMetadata.base_image==ImageMetadata.similar_image).filter(ImageMetadata.brand==brand_selected).count()

    next_url = url_for('explore_images', page=image_list.next_num) \
        if image_list.has_next else None
    prev_url = url_for('explore_images', page=image_list.prev_num) \
        if image_list.has_prev else None

    return render_template('explore.html', image_items=image_list.items,
                           image_list = image_list, brand_list=brand_list,
                           n_images=n_images, next_url=next_url, prev_url=prev_url)


@app.route('/recommend')
def recommend():
    selectedImage = request.args.get('selectedImage')
    selectedImage = selectedImage[1:]  # for whatever reason explore.html adds extra '/' before file name
    similar_image_query = ImageMetadata.query.filter(ImageMetadata.base_image.in_([selectedImage]))
    similar_image_list_items = [row.similar_image for row in similar_image_query.all()][1:5] # to get all similar images
    return render_template('recommend.html', selectedImage=selectedImage, recommended_images=similar_image_list_items)
