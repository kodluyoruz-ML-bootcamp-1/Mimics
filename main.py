from image_classifier import Classifier
# from data_preparer import PreProcessor, DatasetBuilder
from data_land_marker import LandMarker

IMAGES_DIR = 'data/images/'
PREDICTOR_PATH = 'shape_predictor_68_face_landmarks.dat'

INITIAL_CSV = 'data/csvs/ds_original.csv'
FINAL_CSV = 'data/csvs/ds_classes_equalized.csv'


def shape_to_coordinates(img_shape):
    return ','.join(['(%s-%s)' % (i[0], i[1]) for i in img_shape])


def main():
    land_marker = LandMarker(landmark_predictor_path=PREDICTOR_PATH)

    """
    # Pre-process data
    PreProcessor(data_dir=IMAGES_DIR).preprocess()
    """

    """
    # Build dataset as csv
    dataset_builder = DatasetBuilder(data_dir=IMAGES_DIR, class_feature='emotion', land_marker=land_marker)
    dataset_builder.build(target_csv=INITIAL_CSV, write_header=True)
    """

    rf_classifier = Classifier(csv_path=FINAL_CSV, algorithm='RandomForest', land_marker=land_marker)
    print(rf_classifier.classify('smiling_berk.png'))# 'img.png', 'img2.png'))


if __name__ == "__main__":
    main()
    print('success')
