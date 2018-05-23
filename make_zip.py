import os
import zipfile


def make_zip(source_dir, output_filename):
    """打包文件夹至ZIP
    :param output_filename: zip压缩文件名称 type: str
    :param source_dir: 需要压缩的文件夹 type: str
    :return: 打过后文件所在路径及名称, output_filename type: str
    """
    zipf = zipfile.ZipFile(output_filename, 'w')
    pre_len = len(os.path.dirname(source_dir))
    for parent, dirnames, filenames in os.walk(source_dir):
        for filename in filenames:
            pathfile = os.path.join(parent, filename)
            arcname = pathfile[pre_len:].strip(os.path.sep)
            zipf.write(pathfile, arcname)
    zipf.close()
    return output_filename
