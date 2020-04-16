"""Script for decrypting .vdata files."""

import sys
import os
import glob
import io
import filetype


def explain_usage():
    """Explain usage method"""
    print('vdata_decrypt_tool.py "src" "dest"')
    sys.exit()


def check_args(args):
    """Check if script is called with correct arguments."""
    args_ok = False
    if len(args) == 3:
        source_dir_ok = os.path.isdir(args[1])
        dest_dir_ok = os.path.isdir(args[2])

        if source_dir_ok and dest_dir_ok:
            args_ok = True

    if not args_ok:
        print("Error: Please provide a valid source and dest directories.")
        explain_usage()


def decrypt_all(args):
    """Decrypt all .vdata files in source directory.

    Arguments:
        args {Array} -- Arguments passed on script execution.

    """
    print(args)
    check_args(args)

    vdata_dir = args[1]
    vdata_result_dir = args[2]
    vdata_files = glob.glob(os.path.join(vdata_dir, '*.vdata'))

    for vdata_file in vdata_files:
        with io.open(vdata_file, 'rb') as reader:
            # Vaulty adds string "obscured" at the begginign of the image file.
            # They just change the extesnsion for video files.
            # This will read first 8 bytes and if the file is tempered with
            # tempered part will not be read.
            first_eight = reader.read(8)
            if first_eight != b'obscured':
                reader.seek(0)
            good_bytes = reader.read()

            # This will provide original file extension.
            extension = filetype.guess_extension(good_bytes)
            if extension is None:
                print(vdata_file + " is unknown file type.")
                continue

            # Create destination path.
            base_file_name = os.path.basename(vdata_file).split('.')[0]
            new_file_name = 'decrypted_' + base_file_name + '.' + extension
            dest_path = os.path.join(vdata_result_dir, new_file_name)

            with io.open(dest_path, 'wb') as writer:
                writer.write(good_bytes)

            print(vdata_file + " decrypted.")


if __name__ == '__main__':
    decrypt_all(sys.argv)
