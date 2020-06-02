#! /usr/bin/env python3

import os
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

def generate_report(attachment, title, paragraph):
    path = "supplier-data/descriptions/"
    text = ''
    files_list = os.listdir(path)

    for file in files_list:
        text_file_name = os.path.join(path, file)
        with open(text_file_name) as f:
            name = 'name: ' + f.readline()
            weight = 'weight: ' + f.readline()
            new = "<br />\n<br />\n{}<br />{}".format(name, weight)
            text += new
            
    report = SimpleDocTemplate(attachment)
    styles = getSampleStyleSheet()
    main_title = Paragraph(title, styles["h1"])
    report_title = Paragraph(text, styles["h3"])
    report.build([main_title, report_title])

if __name__ == '__main__':
    title = "Processed Update on May 20, 2020"
    attachment = "/tmp/processed.pdf"
    paragraph = ''
    generate_report(attachment, title, paragraph)