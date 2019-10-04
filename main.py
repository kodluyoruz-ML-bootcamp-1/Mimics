from data_preparer import PreProcessor, DatasetBuilder

IMAGES_DIR = 'data/images/'
PREDICTOR_PATH = 'shape_predictor_68_face_landmarks.dat'
CSV_DATASET = 'data/csvs/ds_original.csv'


def shape_to_coordinates(img_shape):
    return ','.join(['(%s-%s)' % (i[0], i[1]) for i in img_shape])


def main():
    # # Pre-process data
    # PreProcessor(data_dir=IMAGES_DIR).preprocess()

    # # Build dataset as csv
    DatasetBuilder(data_dir=IMAGES_DIR, predictor=PREDICTOR_PATH, class_feature='emotion') \
        .build(target_csv=CSV_DATASET, write_header=True)

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
