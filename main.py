from os import listdir

from facial_landmarks import LandMarker
from data_preprocessor import PreProcessor

PREDICTOR_PATH = 'shape_predictor_68_face_landmarks.dat'
DATASET_DIR = 'data'


def shape_to_coordinates(img_shape):
    return ','.join(['(%s-%s)' % (i[0], i[1]) for i in img_shape])


def main():
    # PreProcessor(data_dir=DATASET_DIR).preprocess()

    land_marker = LandMarker(landmark_predictor_path=PREDICTOR_PATH)

    imgs_w_labels = PreProcessor(data_dir=DATASET_DIR).extract_imgs_with_labels()
    for img_w_label in imgs_w_labels:
        landmark_points = land_marker.img_to_landmarks(img_path=img_w_label['path'])
        instance = landmark_points + [img_w_label['label']]
        print(instance)
    exit(19)

    imgs = []

    shape_list = []
    for img_path in images_to_labels.keys():
        imgs.append(img_path)
        landmark_points = img_to_landmarks(predictor=PREDICTOR_PATH, img_path='img.png', label='dummy')

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
