from classifier import Classifier
from data_preparer import PreProcessor, DatasetBuilder
from facial_landmarks import LandMarker

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

    # Build dataset as csv
    dataset_builder = DatasetBuilder(data_dir=IMAGES_DIR, class_feature='emotion', land_marker=land_marker)
    dataset_builder.build(target_csv=INITIAL_CSV, write_header=True)
    """

    rf_classifier = Classifier(csv_path=FINAL_CSV, algorithm='RandomForest', land_marker=land_marker)
    rf_classifier.classify('img.png', 'img2.png')

    exit(96)

    imgs = []

    shape_list = []
    for i in shape_list:
        print(i)

    list1 = shape_list[0]
    list2 = shape_list[1]

    img1 = imgs[0]
    img2 = imgs[1]

    point_dists = []
    for point_list1, point_list2 in zip(list1, list2):
        point_dist = ((point_list2[0] - point_list1[0]) ** 2 + (point_list2[1] - point_list1[1]) ** 2) ** 0.5
        point_dists.append(point_dist)

    final_dist = sum(map(lambda x: x ** 2, point_dists)) ** 0.5

    print(point_dists)
    print('IMAGES: ', img1, img2)
    print(final_dist)
    exit(95)


if __name__ == "__main__":
    main()
    print('success')
