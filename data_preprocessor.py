import enum
from os import listdir, rename, remove
from shutil import rmtree

FILE_SEPARATOR = '/'  # For Linux and MacOS
LABEL_POSTFIX = '_emotion.txt'


def ls(path: str):
    return sorted(listdir(path))


def merge_paths(*paths: str):
    return FILE_SEPARATOR.join(paths)


class EmotionLabels(enum.Enum):
    neutral = {'code': '   0.0000000e+00', 'name': 'neutral'}
    anger = {'code': '   1.0000000e+00', 'name': 'anger'}
    contempt = {'code': '   2.0000000e+00', 'name': 'contempt'}
    disgust = {'code': '   3.0000000e+00', 'name': 'disgust'}
    fear = {'code': '   4.0000000e+00', 'name': 'fear'}
    happy = {'code': '   5.0000000e+00', 'name': 'happy'}
    sadness = {'code': '   6.0000000e+00', 'name': 'sadness'}
    surprise = {'code': '   7.0000000e+00', 'name': 'surprise'}

    @staticmethod
    def code_to_name(input_label_code: str):
        matched_labels = [label for label in EmotionLabels if label.value['code'] == input_label_code]
        return matched_labels[0].value['name']


class ImageDataset:
    img_extension = '.png'
    label_extension = '_emotion.txt'

    def __init__(self, path: str, subject: str, emotion_num):
        self.path = path
        self.subject = subject
        self.emotion_num = emotion_num

    @property
    def imgs(self) -> dict:
        img_names = [img for img in ls(self.path) if img.endswith(self.img_extension)]
        return {
            'name': img_names,  # type: list
            'path': [merge_paths(self.path, img_name) for img_name in img_names]  # type: list
        }

    @property
    def imgs_with_labels(self) -> [dict]:
        return [
            {'path': self.imgs['path'][0], 'label': EmotionLabels.neutral.name},
            {'path': self.imgs['path'][1], 'label': self.emotion_label}
        ]

    @property
    def emotion_label(self) -> str:
        label_file = [img for img in ls(self.path) if img.endswith(self.label_extension)][0]
        label_path = merge_paths(self.path, label_file)
        encoded_label = open(label_path, 'r').read().replace('\n', '')
        return EmotionLabels.code_to_name(input_label_code=encoded_label)

    def regulate_names(self):
        for count, img_path in enumerate(self.imgs['path']):
            formatted_cnt = str(count + 1).zfill(8)
            new_img_name = '%s_%s_%s.png' % (self.subject, self.emotion_num, formatted_cnt)
            rename(src=img_path, dst=merge_paths(self.path, new_img_name))

    def remove_except_first_and_last(self):
        for pic in self.imgs['path'][1:-1]:
            remove(pic)

    def clear_img_paths_without_label(self, label_postfix: str):
        for img_path in self.imgs['path']:
            if not any(label_postfix in pic for pic in ls(img_path)):
                rmtree(img_path)

    @staticmethod
    def collect_img_datasets(dataset_parent_dir: str) -> ['ImageDataset']:
        image_datasets = []
        for subject in ls(dataset_parent_dir):
            subject_dir = merge_paths(dataset_parent_dir, subject)
            for emotion_num in ls(subject_dir):
                path = merge_paths(subject_dir, emotion_num)
                image_datasets.append(ImageDataset(path=path, subject=subject, emotion_num=emotion_num))
        return image_datasets


class PreProcessor:
    def __init__(self, data_dir):
        self.img_datasets = ImageDataset.collect_img_datasets(data_dir)

    def preprocess(self):
        for img_ds in self.img_datasets:
            img_ds.regulate_names()
            img_ds.remove_except_first_and_last()
            img_ds.clear_img_paths_without_label(label_postfix=LABEL_POSTFIX)

    def extract_imgs_with_labels(self) -> [dict]:
        all_imgs_with_labels = []
        for img_ds in self.img_datasets:
            all_imgs_with_labels.extend(img_ds.imgs_with_labels)
        return all_imgs_with_labels


