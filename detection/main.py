from detector import print_result, detect
import glob

for path in glob.glob('.\\photos\\*'):
    print(path)
    print_result(detect(path))
