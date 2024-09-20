import os
import argparse


def rename_sort_files(srcpath, dstfilepath, newdirname, file_format, filename_keyword):
    """ 
    this function sort or extract the pdf files with some key string like( 'lec', 'assn', 'qz' )
     and rename them after removing the unknown extra strange string name.
     order them by lec number and assignment no and quizz numbers. in seperate given root directory of the given path.  
     usefull specially download the MIT materials the name of files are strange.

    """

    # srcpath = r'C:\Users\mrafik\Downloads\computer graphics MIt OCW\static_resources'
    # dstfilepath = r'C:\Users\mrafik\Downloads\computer graphics MIt OCW'
    # newdirname = 'computer_graphics_lecture_MIT'

    # Create the new directory once if it does not exist
    directory_name_path = os.path.join(dstfilepath, newdirname)

    if not os.path.exists(directory_name_path):
        os.mkdir(directory_name_path)

    # Get the list of files in the directory
    filelist = os.listdir(srcpath)
    # print(filelist)

    # Iterate over the files in the directory
    for file in filelist:
        if file.endswith(f'.{file_format}'):
            print(
                f' this is just to check if it is .pdf or not : {file_format}')

            # Extract the base filename without extension
            base_filename = file.split('.')[0]
            print(base_filename)

            # Search for the substring 'lec' starting from an 'l'
            print(
                f'this is just to check if it is pec,assn,final,qz or not : {filename_keyword}')
            # If the substring 'lec' is not found in the string, it will return -1.
            index_lett = base_filename.lower().find(f'{filename_keyword}')

            if index_lett != -1:
                # Extract the new filename starting from 'l'
                # new_filename = base_filename[index_lett:] + '.pdf'
                new_filename = base_filename[index_lett:] + f'.{file_format}'
                print(
                    f"Filename: {file} and index where '{filename_keyword}' starts: {index_lett}")

                # Construct full source and destination paths
                srcfile = os.path.join(srcpath, file)
                dstfile = os.path.join(directory_name_path, new_filename)
                counter = 1
                while os.path.exists(dstfile):
                    new_filename = base_filename[index_lett:] + \
                        f'_{counter}' + f'.{file_format}'
                    dstfile = os.path.join(directory_name_path, new_filename)
                    counter += 1

                # Move and rename the file
                os.rename(srcfile, dstfile)
                print(f"File renamed and moved to: {dstfile}")
                # break  # Exit the loop after processing one matching file


if __name__ == "__main__":
    # srcpath = r'C:\Users\mrafik\Downloads\computer graphics MIt OCW\static_resources'
    # dstfilepath = r'C:\Users\mrafik\Downloads\computer graphics MIt OCW'
    # newdirname = 'computer_graphics_lecture_MITassignment'
    # file_format = 'pdf'
    # filename_keyword = 'final'
    # rename_sort_files(srcpath,dstfilepath,newdirname,file_format,filename_keyword)

    parser = argparse.ArgumentParser(
        description='Sort and rename files by a keyword.')

    # Define arguments for key-value pairs
    parser.add_argument('--srcpath', type=str,
                        help='Source path where the files are located', required=True)
    parser.add_argument('--dstfilepath', type=str,
                        help='Destination path where the renamed files should be saved', required=True)
    parser.add_argument('--newdirname', type=str,
                        help='Name of the new directory to be created inside the destination path', required=True)
    parser.add_argument('--file_format', type=str,
                        help='File format to be sorted (e.g., pdf, txt)', required=True)
    parser.add_argument('--filename_keyword', type=str,
                        help='Keyword to search for in the filenames (e.g., lec, final, qz)', required=True)

    # Parse arguments
    args = parser.parse_args()
    # Call the function with parsed arguments
    rename_sort_files(args.srcpath, args.dstfilepath,
                      args.newdirname, args.file_format, args.filename_keyword)

    # **** Remove the spaces between the argument name and the equals sign. The format should be --arg=value, not --arg = value.
