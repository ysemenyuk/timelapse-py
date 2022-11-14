def makeNum(num):
  if num < 10:
    return f'00000{num}'
  if 10 <= num < 100:
    return f'0000{num}'
  if 100 <= num < 1000:
    return f'000{num}'
  if 1000 <= num < 10000:
    return f'00{num}'
  if 10000 <= num < 100000:
    return f'0{num}'
  return num

STORAGE_DIR = 'C:\\timelapse\\storage'
PHOTOS_DIR = 'photos'
VIDEOS_DIR = 'videos'
PHOTOS_BY_TIME_DIR = 'photosByTime'
VIDEOS_BY_TIME_DIR = 'videos'
TMP = 'tmp_dir'