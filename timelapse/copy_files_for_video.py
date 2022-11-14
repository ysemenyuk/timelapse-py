import os
import shutil


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


def copy_file(file_path, out_dir_path, count):
  output_file_name = f'img-{makeNum(count)}.jpg'
  output_file_path = os.path.join(out_dir_path, output_file_name)
  shutil.copy(file_path, output_file_path)


def copy_files_for_video(src_dir_path, out_dir_path, time=60, fps=25):
    files_paths = []

    for (dir_path, _, file_names) in os.walk(src_dir_path):
        paths = map(lambda f: os.path.join(dir_path, f), file_names)
        files_paths.extend(paths)
        
    all = len(files_paths)
    to_add = time * fps
    to_skeep = all - to_add

    print('all', all)
    print('to_add', to_add)
    print('to_skeep', to_skeep)
    
    count = 0
    
    if to_add >= all:
        print('111 - to_add > all')
        for fp in files_paths:
           count += 1 
           copy_file(fp, out_dir_path, count)

    elif to_add >= to_skeep:
        print('222 - to_add > all')
        
        skeep_step = int(all / to_skeep)
        print('skeep_step', skeep_step)
        
        skeep = 1
        for fp in files_paths:
            if skeep == skeep_step:
                skeep = 1
            else:
                skeep += 1
                count += 1
                copy_file(fp, out_dir_path, count)
        
    elif to_add < to_skeep:
        print('333 - to_add < to_skeep')

        add_step = int(all / to_add)
        print('add_step', add_step)
        
        add = 1
        for fp in files_paths:
            if add == add_step:
                add = 1
                count += 1
                copy_file(fp, out_dir_path, count)
            else:
                add += 1
