from cairosvg import svg2png
import os


for maindir, subdir, file_name_list in os.walk('../image'):
    for filename in file_name_list:
        apath = os.path.join(maindir, filename)
        if 'svg' in filename:
            f = open(apath, 'rb')
            svg2png(bytestring=f.read().decode('utf-8'),write_to=(filename.split('.')[-2] + '.png'))

