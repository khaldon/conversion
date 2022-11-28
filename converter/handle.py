import os
import pdfkit
import mammoth
import ffmpy


def main_handle_file(f, type_convert_from, type_convert_to):
    path_file = os.getcwd() + "/media/" + f.name
    out_path = (
        os.getcwd() + "/media/" + f.name.replace(type_convert_from, type_convert_to)
    )
    with open(path_file, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return path_file, out_path


def handle_html2pdf(f, type_convert_from, type_convert_to):
    """
    Parameters:

    (f): is a file paramter that pass request.FILES["file"]
    (type_convert_from): is a type of file that you will convert from
    (type_convert_to): is a type of file that you will convert to (the output file)

    """
    handle_file = main_handle_file(f, type_convert_from, type_convert_to)
    file_pdf_path = handle_file[0]
    file_out_path = handle_file[1]
    pdfkit.from_file(
        file_pdf_path, file_out_path, options={"enable-local-file-access": ""}
    )
    return file_pdf_path, file_out_path


def handle_docx2html(f, type_convert_from, type_convert_to):
    handle_file = main_handle_file(f, type_convert_from, type_convert_to)
    file_docx_path = handle_file[0]
    file_out_path = handle_file[1]
    with open(file_docx_path, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        html = result.value
        out_file = open(file_out_path, "w")
        out_file.write(html)
        out_file.close()
    return file_docx_path, file_out_path


def handle_video2video(f, type_convert_from, type_convert_to):
    handle_file = main_handle_file(f, type_convert_from, type_convert_to)
    file_video_path = handle_file[0]
    file_out_path = handle_file[1]
    ff = ffmpy.FFmpeg(
        inputs={file_video_path: None},
        outputs={file_out_path: None},
        global_options="-y",
    )
    ff.run()
    return file_video_path, file_out_path
