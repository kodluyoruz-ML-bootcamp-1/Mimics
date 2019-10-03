from os import listdir, rename, remove
from shutil import rmtree

DATASET_DIR = 'data'
FILE_SEPARATOR = '/'  # For Linux and MacOS
LABEL_POSTFIX = '_emotion.txt'


def ls(path: str):
    return sorted(listdir(path))


def merge_paths(*paths: str):
    return FILE_SEPARATOR.join(paths)


class ImageDataset:
    img_extension = '.png'
    label_extension = '_emotion.txt'
    labels = {'   0.0000000e+00': 'neutral',
              '   1.0000000e+00': 'anger',
              '   2.0000000e+00': 'contempt',
              '   3.0000000e+00': 'disgust',
              '   4.0000000e+00': 'fear',
              '   5.0000000e+00': 'happy',
              '   6.0000000e+00': 'sadness',
              '   7.0000000e+00': 'surprise'}

    def __init__(self, path: str, subject: str, emotion_num):
        self.path = path
        self.subject = subject
        self.emotion_num = emotion_num

    @property
    def imgs(self):
        img_names = [img for img in ls(self.path) if img.endswith(self.img_extension)]
        return {'names': img_names,
                'paths': [merge_paths(self.path, img_name) for img_name in img_names]}

    @property
    def label(self) -> str:
        label_file = [img for img in ls(self.path) if img.endswith(self.label_extension)][0]
        label_path = merge_paths(self.path, label_file)
        encoded_label = open(label_path, 'r').read().replace('\n', '')
        return self.labels[encoded_label]

    def regulate_names(self):
        for count, img_path in enumerate(self.imgs['paths']):
            formatted_cnt = str(count + 1).zfill(8)
            new_img_name = '%s_%s_%s.png' % (self.subject, self.emotion_num, formatted_cnt)
            rename(src=img_path, dst=merge_paths(self.path, new_img_name))

    def remove_except_first_and_last(self):
        for pic in self.imgs['paths'][1:-1]:
            remove(pic)

    def clear_img_paths_without_label(self, label_postfix: str):
        for img_path in self.imgs['paths']:
            if not any(label_postfix in pic for pic in ls(img_path)):
                rmtree(img_path)


class PreProcessor:
    def __init__(self, parent_dir):
        self.img_datasets = self.collect_img_datasets(parent_dir)

    @staticmethod
    def collect_img_datasets(dataset_parent_dir: str) -> [ImageDataset]:
        img_datasets = []
        for subject in ls(dataset_parent_dir):
            subject_dir = merge_paths(dataset_parent_dir, subject)
            for emotion_num in ls(subject_dir):
                ds = ImageDataset(path=merge_paths(subject_dir, emotion_num), subject=subject, emotion_num=emotion_num)
                img_datasets.append(ds)
        return img_datasets

    def regulate_names(self):
        return [img_ds.regulate_names() for img_ds in self.img_datasets]

    def remove_except_first_and_last(self):
        return [img_ds.remove_except_first_and_last() for img_ds in self.img_datasets]

    def clear_img_paths_without_label(self):
        return [img_ds.clear_img_paths_without_label(label_postfix=LABEL_POSTFIX) for img_ds in self.img_datasets]

    def execute(self):
        for img_ds in self.img_datasets:
            print(img_ds.path, '-->', img_ds.label['name'])

            # img_ds.regulate_names()
            # img_ds.remove_except_first_and_last()
            # img_ds.clear_img_paths_without_label(label_postfix=LABEL_POSTFIX)

        pass


def pre_process():
    img_datasets = PreProcessor(parent_dir=DATASET_DIR)

    # img_datasets.regulate_names()
    # img_datasets.remove_except_first_and_last()
    # img_datasets.clear_img_paths_without_label()

    print('yovv')


if __name__ == '__main__':
    data_preprocessor = PreProcessor(parent_dir=DATASET_DIR)
    data_preprocessor.execute()
