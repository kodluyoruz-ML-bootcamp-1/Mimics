from os import listdir

import facial_landmarks
from data_preprocessor import PreProcessor

DEFAULT_PREDICTOR = 'shape_predictor_68_face_landmarks.dat'
IMAGE_DIR_PATH = './'
IMAGE_EXTENSION = '.png'


def get_image_files():
    return [IMAGE_DIR_PATH + f for f in listdir(IMAGE_DIR_PATH) if f.endswith(IMAGE_EXTENSION)]


def get_images_to_labels() -> dict:
    images_to_labels = {}
    labels = {'happy', 'sad'}
    image_files = get_image_files()
    image_files = []
    for img in image_files:
        for label in labels:
            if label in img:
                images_to_labels[img] = label
    # return images_to_labels
    return {'img.png': 'happy'}


def shape_to_coordinates(img_shape):
    return ','.join(['(%s-%s)' % (i[0], i[1]) for i in img_shape])


def main():
    images_to_labels = get_images_to_labels()
    imgs = []

    shape_list = []
    for img_path in images_to_labels.keys():
        imgs.append(img_path)
        img_shape = facial_landmarks.landmark_img(predictor=DEFAULT_PREDICTOR, img_path=img_path, label='dummy')

        print(img_shape)
        print(img_shape.ndim)
        print(type(img_shape))
        # """
        exit(22)
        img_shape_tuple = [(i[0], i[1]) for i in img_shape]
        shape_list.append(img_shape_tuple)
        # points_coordinates = shape_to_coordinates(img_shape=img_shape)
        # print(points_coordinates)

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


DATASET_DIR = 'data'

if __name__ == "__main__":
    # PreProcessor(data_dir=DATASET_DIR).execute()
    main()
