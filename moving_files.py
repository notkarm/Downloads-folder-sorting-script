import glob
import os
import shutil

src_folder = r"C:\Users\karmp\Downloads"
img_folder = r"D:\Downloads Organized\image_files\\"
txt_folder = r"D:\Downloads Organized\word_processor_and_text_files\\"
pres_folder = r"D:\Downloads Organized\presentation_files\\"
prog_folder = r"D:\Downloads Organized\programming_files\\"
spr_folder = r"D:\Downloads Organized\spreadsheet_files\\"
sys_folder = r"D:\Downloads Organized\system_files\\"
vid_folder = r"D:\Downloads Organized\video_files\\"
fnt_folder = r"D:\Downloads Organized\font_files\\"
exc_folder = r"D:\Downloads Organized\executable_files\\"
dtb_folder = r"D:\Downloads Organized\database_files\\"
dsc_folder = r"D:\Downloads Organized\disc_files\\"
cmp_folder = r"D:\Downloads Organized\compressed_files\\"
aud_folder = r"D:\Downloads Organized\audio_files\\"

#𝕨𝕠𝕣𝕕_𝕡𝕣𝕠𝕔𝕖𝕤𝕤𝕠𝕣_𝕒𝕟𝕕_𝕥𝕖𝕩𝕥_𝕗𝕚𝕝𝕖𝕤
#*******************************************************************************

# Search files with .txt extension in source directory
pattern = "\*.txt"
txtfiles = glob.glob(src_folder + pattern)
#Move all files with a txt extension
for file in txtfiles:
    file_name = os.path.basename(file)
    shutil.move(file, txt_folder + file_name)
    print('Moved:', file)

# Search files with .doc extension in source directory
pattern = "\*.doc"
docfiles = glob.glob(src_folder + pattern)
#Move all files with a doc extension
for file in docfiles:
    file_name = os.path.basename(file)
    shutil.move(file, txt_folder + file_name)
    print('Moved:', file)

# Search files with .docx extension in source directory
pattern = "\*.docx"
docxfiles = glob.glob(src_folder + pattern)
#Move all files with a docx extension
for file in docxfiles:
    file_name = os.path.basename(file)
    shutil.move(file, txt_folder + file_name)
    print('Moved:', file)

# Search files with .odt extension in source directory
pattern = "\*.odt"
odtfiles = glob.glob(src_folder + pattern)
#Move all files with a odt extension
for file in odtfiles:
    file_name = os.path.basename(file)
    shutil.move(file, txt_folder + file_name)
    print('Moved:', file)

# Search files with .pdf extension in source directory
pattern = "\*.pdf"
pdffiles = glob.glob(src_folder + pattern)
#Move all files with a pdf extension
for file in pdffiles:
    file_name = os.path.basename(file)
    shutil.move(file, txt_folder + file_name)
    print('Moved:', file)

# Search files with .rtf extension in source directory
pattern = "\*.rtf"
rtffiles = glob.glob(src_folder + pattern)
#Move all files with a rtf extension
for file in rtffiles:
    file_name = os.path.basename(file)
    shutil.move(file, txt_folder + file_name)
    print('Moved:', file)

# Search files with .tex extension in source directory
pattern = "\*.tex"
texfiles = glob.glob(src_folder + pattern)
#Move all files with a tex extension
for file in texfiles:
    file_name = os.path.basename(file)
    shutil.move(file, txt_folder + file_name)
    print('Moved:', file)

# Search files with .wpd extension in source directory
pattern = "\*.wpd"
wpdfiles = glob.glob(src_folder + pattern)
#Move all files with a wpd extension
for file in wpdfiles:
    file_name = os.path.basename(file)
    shutil.move(file, txt_folder + file_name)
    print('Moved:', file)

#𝕚𝕞𝕒𝕘𝕖_𝕗𝕚𝕝𝕖𝕤
#*******************************************************************************

# Search files with .ai extension in source directory
pattern = "\*.ai"
aifiles = glob.glob(src_folder + pattern)
#Move all files with a ai extension
for file in aifiles:
    file_name = os.path.basename(file)
    shutil.move(file, img_folder + file_name)
    print('Moved:', file)

# Search files with .bmp extension in source directory
pattern = "\*.bmp"
bmpfiles = glob.glob(src_folder + pattern)
#Move all files with a bmp extension
for file in bmpfiles:
    file_name = os.path.basename(file)
    shutil.move(file, img_folder + file_name)
    print('Moved:', file)

# Search files with .gif extension in source directory
pattern = "\*.gif"
giffiles = glob.glob(src_folder + pattern)
#Move all files with a gif extension
for file in giffiles:
    file_name = os.path.basename(file)
    shutil.move(file, img_folder + file_name)
    print('Moved:', file)

# Search files with .ico extension in source directory
pattern = "\*.ico"
icofiles = glob.glob(src_folder + pattern)
#Move all files with a ico extension
for file in icofiles:
    file_name = os.path.basename(file)
    shutil.move(file, img_folder + file_name)
    print('Moved:', file)

# Search files with .jpeg extension in source directory
pattern = "\*.jpeg"
jpegfiles = glob.glob(src_folder + pattern)
#Move all files with a jpeg extension
for file in jpegfiles:
    file_name = os.path.basename(file)
    shutil.move(file, img_folder + file_name)
    print('Moved:', file)

# Search files with .jpg extension in source directory
pattern = "\*.jpg"
jpgfiles = glob.glob(src_folder + pattern)
#Move all files with a jpg extension
for file in jpgfiles:
    file_name = os.path.basename(file)
    shutil.move(file, img_folder + file_name)
    print('Moved:', file)

# Search files with .png extension in source directory
pattern = "\*.png"
pngfiles = glob.glob(src_folder + pattern)
#Move all files with a png extension
for file in pngfiles:
    file_name = os.path.basename(file)
    shutil.move(file, img_folder + file_name)
    print('Moved:', file)

# Search files with .ps extension in source directory
pattern = "\*.ps"
psfiles = glob.glob(src_folder + pattern)
#Move all files with a ps extension
for file in psfiles:
    file_name = os.path.basename(file)
    shutil.move(file, img_folder + file_name)
    print('Moved:', file)

# Search files with .psd extension in source directory
pattern = "\*.psd"
psdfiles = glob.glob(src_folder + pattern)
#Move all files with a psd extension
for file in psdfiles:
    file_name = os.path.basename(file)
    shutil.move(file, img_folder + file_name)
    print('Moved:', file)

# Search files with .svg extension in source directory
pattern = "\*.svg"
svgfiles = glob.glob(src_folder + pattern)
#Move all files with a svg extension
for file in svgfiles:
    file_name = os.path.basename(file)
    shutil.move(file, img_folder + file_name)
    print('Moved:', file)

# Search files with .tif extension in source directory
pattern = "\*.tif"
tiffiles = glob.glob(src_folder + pattern)
#Move all files with a tif extension
for file in tiffiles:
    file_name = os.path.basename(file)
    shutil.move(file, img_folder + file_name)
    print('Moved:', file)

# Search files with .tiff extension in source directory
pattern = "\*.tiff"
tifffiles = glob.glob(src_folder + pattern)
#Move all files with a tiff extension
for file in tifffiles:
    file_name = os.path.basename(file)
    shutil.move(file, img_folder + file_name)
    print('Moved:', file)

#𝕡𝕣𝕖𝕤𝕖𝕟𝕥𝕒𝕥𝕚𝕠𝕟_𝕗𝕚𝕝𝕖𝕤
#*******************************************************************************

# Search files with .key extension in source directory
pattern = "\*.key"
keyfiles = glob.glob(src_folder + pattern)
#Move all files with a key extension
for file in keyfiles:
    file_name = os.path.basename(file)
    shutil.move(file, pres_folder + file_name)
    print('Moved:', file)

# Search files with .odp extension in source directory
pattern = "\*.odp"
odpfiles = glob.glob(src_folder + pattern)
#Move all files with a odp extension
for file in odpfiles:
    file_name = os.path.basename(file)
    shutil.move(file, pres_folder + file_name)
    print('Moved:', file)

# Search files with .pps extension in source directory
pattern = "\*.pps"
ppsfiles = glob.glob(src_folder + pattern)
#Move all files with a pps extension
for file in ppsfiles:
    file_name = os.path.basename(file)
    shutil.move(file, pres_folder + file_name)
    print('Moved:', file)

# Search files with .ppt extension in source directory
pattern = "\*.ppt"
pptfiles = glob.glob(src_folder + pattern)
#Move all files with a ppt extension
for file in pptfiles:
    file_name = os.path.basename(file)
    shutil.move(file, pres_folder + file_name)
    print('Moved:', file)

# Search files with .pptx extension in source directory
pattern = "\*.pptx"
pptxfiles = glob.glob(src_folder + pattern)
#Move all files with a pptx extension
for file in pptxfiles:
    file_name = os.path.basename(file)
    shutil.move(file, pres_folder + file_name)
    print('Moved:', file)

#𝕡𝕣𝕠𝕘𝕣𝕒𝕞𝕞𝕚𝕟𝕘_𝕗𝕚𝕝𝕖𝕤
#*******************************************************************************

# Search files with .c extension in source directory
pattern = "\*.c"
cfiles = glob.glob(src_folder + pattern)
#Move all files with a c extension
for file in cfiles:
    file_name = os.path.basename(file)
    shutil.move(file, prog_folder + file_name)
    print('Moved:', file)

# Search files with .cgi extension in source directory
pattern = "\*.cgi"
cgifiles = glob.glob(src_folder + pattern)
#Move all files with a cgi extension
for file in cgifiles:
    file_name = os.path.basename(file)
    shutil.move(file, prog_folder + file_name)
    print('Moved:', file)

# Search files with .pl extension in source directory
pattern = "\*.pl"
plfiles = glob.glob(src_folder + pattern)
#Move all files with a pl extension
for file in plfiles:
    file_name = os.path.basename(file)
    shutil.move(file, prog_folder + file_name)
    print('Moved:', file)

# Search files with .class extension in source directory
pattern = "\*.class"
classfiles = glob.glob(src_folder + pattern)
#Move all files with a class extension
for file in classfiles:
    file_name = os.path.basename(file)
    shutil.move(file, prog_folder + file_name)
    print('Moved:', file)

# Search files with .cpp extension in source directory
pattern = "\*.cpp"
cppfiles = glob.glob(src_folder + pattern)
#Move all files with a cpp extension
for file in cppfiles:
    file_name = os.path.basename(file)
    shutil.move(file, prog_folder + file_name)
    print('Moved:', file)

# Search files with .cs extension in source directory
pattern = "\*.cs"
csfiles = glob.glob(src_folder + pattern)
#Move all files with a cs extension
for file in csfiles:
    file_name = os.path.basename(file)
    shutil.move(file, prog_folder + file_name)
    print('Moved:', file)

# Search files with .h extension in source directory
pattern = "\*.h"
hfiles = glob.glob(src_folder + pattern)
#Move all files with a h extension
for file in hfiles:
    file_name = os.path.basename(file)
    shutil.move(file, prog_folder + file_name)
    print('Moved:', file)

# Search files with .java extension in source directory
pattern = "\*.java"
javafiles = glob.glob(src_folder + pattern)
#Move all files with a java extension
for file in javafiles:
    file_name = os.path.basename(file)
    shutil.move(file, prog_folder + file_name)
    print('Moved:', file)

# Search files with .php extension in source directory
pattern = "\*.php"
phpfiles = glob.glob(src_folder + pattern)
#Move all files with a php extension
for file in phpfiles:
    file_name = os.path.basename(file)
    shutil.move(file, prog_folder + file_name)
    print('Moved:', file)

# Search files with .py extension in source directory
pattern = "\*.py"
pyfiles = glob.glob(src_folder + pattern)
#Move all files with a py extension
for file in pyfiles:
    file_name = os.path.basename(file)
    shutil.move(file, prog_folder + file_name)
    print('Moved:', file)

# Search files with .sh extension in source directory
pattern = "\*.sh"
shfiles = glob.glob(src_folder + pattern)
#Move all files with a sh extension
for file in shfiles:
    file_name = os.path.basename(file)
    shutil.move(file, prog_folder + file_name)
    print('Moved:', file)

# Search files with .swift extension in source directory
pattern = "\*.swift"
swiftfiles = glob.glob(src_folder + pattern)
#Move all files with a swift extension
for file in swiftfiles:
    file_name = os.path.basename(file)
    shutil.move(file, prog_folder + file_name)
    print('Moved:', file)

# Search files with .vb extension in source directory
pattern = "\*.vb"
vbfiles = glob.glob(src_folder + pattern)
#Move all files with a vb extension
for file in vbfiles:
    file_name = os.path.basename(file)
    shutil.move(file, prog_folder + file_name)
    print('Moved:', file)

# Search files with .asp extension in source directory
pattern = "\*.asp"
aspfiles = glob.glob(src_folder + pattern)
#Move all files with a asp extension
for file in aspfiles:
    file_name = os.path.basename(file)
    shutil.move(file, prog_folder + file_name)
    print('Moved:', file)

# Search files with .aspx extension in source directory
pattern = "\*.aspx"
aspxfiles = glob.glob(src_folder + pattern)
#Move all files with a aspx extension
for file in aspxfiles:
    file_name = os.path.basename(file)
    shutil.move(file, prog_folder + file_name)
    print('Moved:', file)

# Search files with .cer extension in source directory
pattern = "\*.cer"
cerfiles = glob.glob(src_folder + pattern)
#Move all files with a cer extension
for file in cerfiles:
    file_name = os.path.basename(file)
    shutil.move(file, prog_folder + file_name)
    print('Moved:', file)

# Search files with .cfm extension in source directory
pattern = "\*.cfm"
cfmfiles = glob.glob(src_folder + pattern)
#Move all files with a cfm extension
for file in cfmfiles:
    file_name = os.path.basename(file)
    shutil.move(file, prog_folder + file_name)
    print('Moved:', file)

# Search files with .css extension in source directory
pattern = "\*.css"
cssfiles = glob.glob(src_folder + pattern)
#Move all files with a css extension
for file in cssfiles:
    file_name = os.path.basename(file)
    shutil.move(file, prog_folder + file_name)
    print('Moved:', file)

# Search files with .htm extension in source directory
pattern = "\*.htm"
htmfiles = glob.glob(src_folder + pattern)
#Move all files with a htm extension
for file in htmfiles:
    file_name = os.path.basename(file)
    shutil.move(file, prog_folder + file_name)
    print('Moved:', file)

# Search files with .html extension in source directory
pattern = "\*.html"
htmlfiles = glob.glob(src_folder + pattern)
#Move all files with a html extension
for file in htmlfiles:
    file_name = os.path.basename(file)
    shutil.move(file, prog_folder + file_name)
    print('Moved:', file)

# Search files with .js extension in source directory
pattern = "\*.js"
jsfiles = glob.glob(src_folder + pattern)
#Move all files with a js extension
for file in jsfiles:
    file_name = os.path.basename(file)
    shutil.move(file, prog_folder + file_name)
    print('Moved:', file)

# Search files with .jsp extension in source directory
pattern = "\*.jsp"
jspfiles = glob.glob(src_folder + pattern)
#Move all files with a jsp extension
for file in jspfiles:
    file_name = os.path.basename(file)
    shutil.move(file, prog_folder + file_name)
    print('Moved:', file)

# Search files with .rss extension in source directory
pattern = "\*.rss"
rssfiles = glob.glob(src_folder + pattern)
#Move all files with a rss extension
for file in rssfiles:
    file_name = os.path.basename(file)
    shutil.move(file, prog_folder + file_name)
    print('Moved:', file)

# Search files with .xhtml extension in source directory
pattern = "\*.xhtml"
xhtmlfiles = glob.glob(src_folder + pattern)
#Move all files with a xhtml extension
for file in xhtmlfiles:
    file_name = os.path.basename(file)
    shutil.move(file, prog_folder + file_name)
    print('Moved:', file)

#𝕤𝕡𝕣𝕖𝕒𝕕𝕤𝕙𝕖𝕖𝕥_𝕗𝕚𝕝𝕖𝕤
#*******************************************************************************

# Search files with .ods extension in source directory
pattern = "\*.ods"
odsfiles = glob.glob(src_folder + pattern)
#Move all files with a ods extension
for file in odsfiles:
    file_name = os.path.basename(file)
    shutil.move(file, spr_folder + file_name)
    print('Moved:', file)

# Search files with .xls extension in source directory
pattern = "\*.xls"
xlsfiles = glob.glob(src_folder + pattern)
#Move all files with a xls extension
for file in xlsfiles:
    file_name = os.path.basename(file)
    shutil.move(file, spr_folder + file_name)
    print('Moved:', file)

# Search files with .xlsm extension in source directory
pattern = "\*.xlsm"
xlsmfiles = glob.glob(src_folder + pattern)
#Move all files with a xlsm extension
for file in xlsmfiles:
    file_name = os.path.basename(file)
    shutil.move(file, spr_folder + file_name)
    print('Moved:', file)

# Search files with .xlsx extension in source directory
pattern = "\*.xlsx"
xlsxfiles = glob.glob(src_folder + pattern)
#Move all files with a xlsx extension
for file in xlsxfiles:
    file_name = os.path.basename(file)
    shutil.move(file, spr_folder + file_name)
    print('Moved:', file)

#𝕤𝕪𝕤𝕥𝕖𝕞_𝕗𝕚𝕝𝕖𝕤
#*******************************************************************************

# Search files with .bak extension in source directory
pattern = "\*.bak"
bakfiles = glob.glob(src_folder + pattern)
#Move all files with a bak extension
for file in bakfiles:
    file_name = os.path.basename(file)
    shutil.move(file, sys_folder + file_name)
    print('Moved:', file)

# Search files with .cab extension in source directory
pattern = "\*.cab"
cabfiles = glob.glob(src_folder + pattern)
#Move all files with a cab extension
for file in cabfiles:
    file_name = os.path.basename(file)
    shutil.move(file, sys_folder + file_name)
    print('Moved:', file)

# Search files with .cfg extension in source directory
pattern = "\*.cfg"
cfgfiles = glob.glob(src_folder + pattern)
#Move all files with a cfg extension
for file in cfgfiles:
    file_name = os.path.basename(file)
    shutil.move(file, sys_folder + file_name)
    print('Moved:', file)

# Search files with .cpl extension in source directory
pattern = "\*.cpl"
cplfiles = glob.glob(src_folder + pattern)
#Move all files with a cpl extension
for file in cplfiles:
    file_name = os.path.basename(file)
    shutil.move(file, sys_folder + file_name)
    print('Moved:', file)

# Search files with .cur extension in source directory
pattern = "\*.cur"
curfiles = glob.glob(src_folder + pattern)
#Move all files with a cur extension
for file in curfiles:
    file_name = os.path.basename(file)
    shutil.move(file, sys_folder + file_name)
    print('Moved:', file)

# Search files with .dll extension in source directory
pattern = "\*.dll"
dllfiles = glob.glob(src_folder + pattern)
#Move all files with a dll extension
for file in dllfiles:
    file_name = os.path.basename(file)
    shutil.move(file, sys_folder + file_name)
    print('Moved:', file)

# Search files with .dmp extension in source directory
pattern = "\*.dmp"
dmpfiles = glob.glob(src_folder + pattern)
#Move all files with a dmp extension
for file in dmpfiles:
    file_name = os.path.basename(file)
    shutil.move(file, sys_folder + file_name)
    print('Moved:', file)

# Search files with .drv extension in source directory
pattern = "\*.drv"
drvfiles = glob.glob(src_folder + pattern)
#Move all files with a drv extension
for file in drvfiles:
    file_name = os.path.basename(file)
    shutil.move(file, sys_folder + file_name)
    print('Moved:', file)

# Search files with .icns extension in source directory
pattern = "\*.icns"
icnsfiles = glob.glob(src_folder + pattern)
#Move all files with a icns extension
for file in icnsfiles:
    file_name = os.path.basename(file)
    shutil.move(file, sys_folder + file_name)
    print('Moved:', file)

# Search files with .ini extension in source directory
pattern = "\*.ini"
inifiles = glob.glob(src_folder + pattern)
#Move all files with a ini extension
for file in inifiles:
    file_name = os.path.basename(file)
    shutil.move(file, sys_folder + file_name)
    print('Moved:', file)

# Search files with .ink extension in source directory
pattern = "\*.ink"
inkfiles = glob.glob(src_folder + pattern)
#Move all files with a ink extension
for file in inkfiles:
    file_name = os.path.basename(file)
    shutil.move(file, sys_folder + file_name)
    print('Moved:', file)

# Search files with .sys extension in source directory
pattern = "\*.sys"
sysfiles = glob.glob(src_folder + pattern)
#Move all files with a sys extension
for file in sysfiles:
    file_name = os.path.basename(file)
    shutil.move(file, sys_folder + file_name)
    print('Moved:', file)

# Search files with .tmp extension in source directory
pattern = "\*.tmp"
tmpfiles = glob.glob(src_folder + pattern)
#Move all files with a tmp extension
for file in tmpfiles:
    file_name = os.path.basename(file)
    shutil.move(file, sys_folder + file_name)
    print('Moved:', file)

#𝕧𝕚𝕕𝕖𝕠_𝕗𝕚𝕝𝕖𝕤
#*******************************************************************************

#These do not work since the extension starts with a number
"""
# Search files with .3g2 extension in source directory
pattern = "\*.3g2"
3g2files = glob.glob(src_folder + pattern)
#Move all files with a 3g2 extension
for file in 3g2files:
    file_name = os.path.basename(file)
    shutil.move(file, sys_folder + file_name)
    print('Moved:', file)


# Search files with .3gp extension in source directory
pattern = "\*.3gp"
3gpfiles = glob.glob(src_folder + pattern)
#Move all files with a 3gp extension
for file in 3gpfiles:
    file_name = os.path.basename(file)
    shutil.move(file, vid_folder + file_name)
    print('Moved:', file)
"""

# Search files with .avi extension in source directory
pattern = "\*.avi"
avifiles = glob.glob(src_folder + pattern)
#Move all files with a avi extension
for file in avifiles:
    file_name = os.path.basename(file)
    shutil.move(file, vid_folder + file_name)
    print('Moved:', file)

# Search files with .flv extension in source directory
pattern = "\*.flv"
flvfiles = glob.glob(src_folder + pattern)
#Move all files with a flv extension
for file in flvfiles:
    file_name = os.path.basename(file)
    shutil.move(file, vid_folder + file_name)
    print('Moved:', file)

# Search files with .h264 extension in source directory
pattern = "\*.h264"
h264files = glob.glob(src_folder + pattern)
#Move all files with a h264 extension
for file in h264files:
    file_name = os.path.basename(file)
    shutil.move(file, vid_folder + file_name)
    print('Moved:', file)

# Search files with .m4v extension in source directory
pattern = "\*.m4v"
m4vfiles = glob.glob(src_folder + pattern)
#Move all files with a m4v extension
for file in m4vfiles:
    file_name = os.path.basename(file)
    shutil.move(file, vid_folder + file_name)
    print('Moved:', file)

# Search files with .mkv extension in source directory
pattern = "\*.mkv"
mkvfiles = glob.glob(src_folder + pattern)
#Move all files with a mkv extension
for file in mkvfiles:
    file_name = os.path.basename(file)
    shutil.move(file, vid_folder + file_name)
    print('Moved:', file)

# Search files with .mov extension in source directory
pattern = "\*.mov"
movfiles = glob.glob(src_folder + pattern)
#Move all files with a mov extension
for file in movfiles:
    file_name = os.path.basename(file)
    shutil.move(file, vid_folder + file_name)
    print('Moved:', file)

# Search files with .mp4 extension in source directory
pattern = "\*.mp4"
mp4files = glob.glob(src_folder + pattern)
#Move all files with a mp4 extension
for file in mp4files:
    file_name = os.path.basename(file)
    shutil.move(file, vid_folder + file_name)
    print('Moved:', file)

# Search files with .mpg extension in source directory
pattern = "\*.mpg"
mpgfiles = glob.glob(src_folder + pattern)
#Move all files with a mpg extension
for file in mpgfiles:
    file_name = os.path.basename(file)
    shutil.move(file, vid_folder + file_name)
    print('Moved:', file)

# Search files with .mpeg extension in source directory
pattern = "\*.mpeg"
mpegfiles = glob.glob(src_folder + pattern)
#Move all files with a mpeg extension
for file in mpegfiles:
    file_name = os.path.basename(file)
    shutil.move(file, vid_folder + file_name)
    print('Moved:', file)

# Search files with .rm extension in source directory
pattern = "\*.rm"
rmfiles = glob.glob(src_folder + pattern)
#Move all files with a rm extension
for file in rmfiles:
    file_name = os.path.basename(file)
    shutil.move(file, vid_folder + file_name)
    print('Moved:', file)

# Search files with .swf extension in source directory
pattern = "\*.swf"
swffiles = glob.glob(src_folder + pattern)
#Move all files with a swf extension
for file in swffiles:
    file_name = os.path.basename(file)
    shutil.move(file, vid_folder + file_name)
    print('Moved:', file)

# Search files with .vob extension in source directory
pattern = "\*.vob"
vobfiles = glob.glob(src_folder + pattern)
#Move all files with a vob extension
for file in vobfiles:
    file_name = os.path.basename(file)
    shutil.move(file, vid_folder + file_name)
    print('Moved:', file)

# Search files with .wmv extension in source directory
pattern = "\*.wmv"
wmvfiles = glob.glob(src_folder + pattern)
#Move all files with a wmv extension
for file in wmvfiles:
    file_name = os.path.basename(file)
    shutil.move(file, vid_folder + file_name)
    print('Moved:', file)

#𝕗𝕠𝕟𝕥_𝕗𝕚𝕝𝕖𝕤
#*******************************************************************************

# Search files with .fnt extension in source directory
pattern = "\*.fnt"
fntfiles = glob.glob(src_folder + pattern)
#Move all files with a fnt extension
for file in fntfiles:
    file_name = os.path.basename(file)
    shutil.move(file, fnt_folder + file_name)
    print('Moved:', file)

# Search files with .fon extension in source directory
pattern = "\*.fon"
fonfiles = glob.glob(src_folder + pattern)
#Move all files with a fon extension
for file in fonfiles:
    file_name = os.path.basename(file)
    shutil.move(file, fnt_folder + file_name)
    print('Moved:', file)

# Search files with .otf extension in source directory
pattern = "\*.otf"
otffiles = glob.glob(src_folder + pattern)
#Move all files with a otf extension
for file in otffiles:
    file_name = os.path.basename(file)
    shutil.move(file, fnt_folder + file_name)
    print('Moved:', file)

# Search files with .ttf extension in source directory
pattern = "\*.ttf"
ttffiles = glob.glob(src_folder + pattern)
#Move all files with a ttf extension
for file in ttffiles:
    file_name = os.path.basename(file)
    shutil.move(file, fnt_folder + file_name)
    print('Moved:', file)

#𝕖𝕩𝕖𝕔𝕦𝕥𝕒𝕓𝕝𝕖_𝕗𝕚𝕝𝕖𝕤
#*******************************************************************************

# Search files with .apk extension in source directory
pattern = "\*.apk"
apkfiles = glob.glob(src_folder + pattern)
#Move all files with a apk extension
for file in apkfiles:
    file_name = os.path.basename(file)
    shutil.move(file, exc_folder + file_name)
    print('Moved:', file)

# Search files with .bat extension in source directory
pattern = "\*.bat"
batfiles = glob.glob(src_folder + pattern)
#Move all files with a bat extension
for file in batfiles:
    file_name = os.path.basename(file)
    shutil.move(file, exc_folder + file_name)
    print('Moved:', file)

# Search files with .bin extension in source directory
pattern = "\*.bin"
binfiles = glob.glob(src_folder + pattern)
#Move all files with a bin extension
for file in binfiles:
    file_name = os.path.basename(file)
    shutil.move(file, exc_folder + file_name)
    print('Moved:', file)

# Search files with .com extension in source directory
pattern = "\*.com"
comfiles = glob.glob(src_folder + pattern)
#Move all files with a com extension
for file in comfiles:
    file_name = os.path.basename(file)
    shutil.move(file, exc_folder + file_name)
    print('Moved:', file)

# Search files with .exe extension in source directory
pattern = "\*.exe"
exefiles = glob.glob(src_folder + pattern)
#Move all files with a exe extension
for file in exefiles:
    file_name = os.path.basename(file)
    shutil.move(file, exc_folder + file_name)
    print('Moved:', file)

# Search files with .gadget extension in source directory
pattern = "\*.gadget"
gadgetfiles = glob.glob(src_folder + pattern)
#Move all files with a gadget extension
for file in gadgetfiles:
    file_name = os.path.basename(file)
    shutil.move(file, exc_folder + file_name)
    print('Moved:', file)

# Search files with .jar extension in source directory
pattern = "\*.jar"
jarfiles = glob.glob(src_folder + pattern)
#Move all files with a jar extension
for file in jarfiles:
    file_name = os.path.basename(file)
    shutil.move(file, exc_folder + file_name)
    print('Moved:', file)

# Search files with .wsf extension in source directory
pattern = "\*.wsf"
wsffiles = glob.glob(src_folder + pattern)
#Move all files with a wsf extension
for file in wsffiles:
    file_name = os.path.basename(file)
    shutil.move(file, exc_folder + file_name)
    print('Moved:', file)

# Search files with .msi extension in source directory
pattern = "\*.msi"
msifiles = glob.glob(src_folder + pattern)
#Move all files with a msi extension
for file in msifiles:
    file_name = os.path.basename(file)
    shutil.move(file, exc_folder + file_name)
    print('Moved:', file)

#𝕕𝕒𝕥𝕒𝕓𝕒𝕤𝕖_𝕗𝕚𝕝𝕖𝕤
#*******************************************************************************

# Search files with .csv extension in source directory
pattern = "\*.csv"
csvfiles = glob.glob(src_folder + pattern)
#Move all files with a csv extension
for file in csvfiles:
    file_name = os.path.basename(file)
    shutil.move(file, dtb_folder + file_name)
    print('Moved:', file)

# Search files with .dat extension in source directory
pattern = "\*.dat"
datfiles = glob.glob(src_folder + pattern)
#Move all files with a dat extension
for file in datfiles:
    file_name = os.path.basename(file)
    shutil.move(file, dtb_folder + file_name)
    print('Moved:', file)

# Search files with .db extension in source directory
pattern = "\*.db"
dbfiles = glob.glob(src_folder + pattern)
#Move all files with a db extension
for file in dbfiles:
    file_name = os.path.basename(file)
    shutil.move(file, dtb_folder + file_name)
    print('Moved:', file)

# Search files with .dbf extension in source directory
pattern = "\*.dbf"
dbffiles = glob.glob(src_folder + pattern)
#Move all files with a dbf extension
for file in dbffiles:
    file_name = os.path.basename(file)
    shutil.move(file, dtb_folder + file_name)
    print('Moved:', file)

# Search files with .log extension in source directory
pattern = "\*.log"
logfiles = glob.glob(src_folder + pattern)
#Move all files with a log extension
for file in logfiles:
    file_name = os.path.basename(file)
    shutil.move(file, dtb_folder + file_name)
    print('Moved:', file)

# Search files with .mdb extension in source directory
pattern = "\*.mdb"
mdbfiles = glob.glob(src_folder + pattern)
#Move all files with a mdb extension
for file in mdbfiles:
    file_name = os.path.basename(file)
    shutil.move(file, dtb_folder + file_name)
    print('Moved:', file)

# Search files with .sav extension in source directory
pattern = "\*.sav"
savfiles = glob.glob(src_folder + pattern)
#Move all files with a sav extension
for file in savfiles:
    file_name = os.path.basename(file)
    shutil.move(file, dtb_folder + file_name)
    print('Moved:', file)

# Search files with .sql extension in source directory
pattern = "\*.sql"
sqlfiles = glob.glob(src_folder + pattern)
#Move all files with a sql extension
for file in sqlfiles:
    file_name = os.path.basename(file)
    shutil.move(file, dtb_folder + file_name)
    print('Moved:', file)

# Search files with .tar extension in source directory
pattern = "\*.tar"
tarfiles = glob.glob(src_folder + pattern)
#Move all files with a tar extension
for file in tarfiles:
    file_name = os.path.basename(file)
    shutil.move(file, dtb_folder + file_name)
    print('Moved:', file)

# Search files with .xml extension in source directory
pattern = "\*.xml"
xmlfiles = glob.glob(src_folder + pattern)
#Move all files with a xml extension
for file in xmlfiles:
    file_name = os.path.basename(file)
    shutil.move(file, dtb_folder + file_name)
    print('Moved:', file)

#𝕕𝕚𝕤𝕔_𝕗𝕚𝕝𝕖𝕤
#*******************************************************************************

# Search files with .bin extension in source directory
pattern = "\*.bin"
binfiles = glob.glob(src_folder + pattern)
#Move all files with a bin extension
for file in binfiles:
    file_name = os.path.basename(file)
    shutil.move(file, dsc_folder + file_name)
    print('Moved:', file)

# Search files with .dmg extension in source directory
pattern = "\*.dmg"
dmgfiles = glob.glob(src_folder + pattern)
#Move all files with a dmg extension
for file in dmgfiles:
    file_name = os.path.basename(file)
    shutil.move(file, dsc_folder + file_name)
    print('Moved:', file)

# Search files with .iso extension in source directory
pattern = "\*.iso"
isofiles = glob.glob(src_folder + pattern)
#Move all files with a iso extension
for file in isofiles:
    file_name = os.path.basename(file)
    shutil.move(file, dsc_folder + file_name)
    print('Moved:', file)

# Search files with .toast extension in source directory
pattern = "\*.toast"
toastfiles = glob.glob(src_folder + pattern)
#Move all files with a toast extension
for file in toastfiles:
    file_name = os.path.basename(file)
    shutil.move(file, dsc_folder + file_name)
    print('Moved:', file)

# Search files with .vcd extension in source directory
pattern = "\*.vcd"
vcdfiles = glob.glob(src_folder + pattern)
#Move all files with a vcd extension
for file in vcdfiles:
    file_name = os.path.basename(file)
    shutil.move(file, dsc_folder + file_name)
    print('Moved:', file)

#𝕔𝕠𝕞𝕡𝕣𝕖𝕤𝕤𝕖𝕕_𝕗𝕚𝕝𝕖𝕤
#*******************************************************************************

#This does not work since the extension starts with a number
"""
# Search files with .7z extension in source directory
pattern = "\*.7z"
7zfiles = glob.glob(src_folder + pattern)
#Move all files with a 7z extension
for file in 7zfiles:
    file_name = os.path.basename(file)
    shutil.move(file, cmp_folder + file_name)
    print('Moved:', file)
"""

# Search files with .arj extension in source directory
pattern = "\*.arj"
arjfiles = glob.glob(src_folder + pattern)
#Move all files with a arj extension
for file in arjfiles:
    file_name = os.path.basename(file)
    shutil.move(file, cmp_folder + file_name)
    print('Moved:', file)

# Search files with .deb extension in source directory
pattern = "\*.deb"
debfiles = glob.glob(src_folder + pattern)
#Move all files with a deb extension
for file in debfiles:
    file_name = os.path.basename(file)
    shutil.move(file, cmp_folder + file_name)
    print('Moved:', file)

# Search files with .pkg extension in source directory
pattern = "\*.pkg"
pkgfiles = glob.glob(src_folder + pattern)
#Move all files with a pkg extension
for file in pkgfiles:
    file_name = os.path.basename(file)
    shutil.move(file, cmp_folder + file_name)
    print('Moved:', file)

# Search files with .rar extension in source directory
pattern = "\*.rar"
rarfiles = glob.glob(src_folder + pattern)
#Move all files with a rar extension
for file in rarfiles:
    file_name = os.path.basename(file)
    shutil.move(file, cmp_folder + file_name)
    print('Moved:', file)

# Search files with .rpm extension in source directory
pattern = "\*.rpm"
rpmfiles = glob.glob(src_folder + pattern)
#Move all files with a rpm extension
for file in rpmfiles:
    file_name = os.path.basename(file)
    shutil.move(file, cmp_folder + file_name)
    print('Moved:', file)

# Search files with .tar.gz extension in source directory
pattern = "\*.tar.gz"
tar.gzfiles = glob.glob(src_folder + pattern)
#Move all files with a tar.gz extension
for file in tar.gzfiles:
    file_name = os.path.basename(file)
    shutil.move(file, cmp_folder + file_name)
    print('Moved:', file)

# Search files with .z extension in source directory
pattern = "\*.z"
zfiles = glob.glob(src_folder + pattern)
#Move all files with a z extension
for file in zfiles:
    file_name = os.path.basename(file)
    shutil.move(file, cmp_folder + file_name)
    print('Moved:', file)

# Search files with .zip extension in source directory
pattern = "\*.zip"
zipfiles = glob.glob(src_folder + pattern)
#Move all files with a zip extension
for file in zipfiles:
    file_name = os.path.basename(file)
    shutil.move(file, cmp_folder + file_name)
    print('Moved:', file)

#𝕒𝕦𝕕𝕚𝕠_𝕗𝕚𝕝𝕖𝕤
#*******************************************************************************

# Search files with .aif extension in source directory
pattern = "\*.aif"
aiffiles = glob.glob(src_folder + pattern)
#Move all files with a aif extension
for file in aiffiles:
    file_name = os.path.basename(file)
    shutil.move(file, aud_folder + file_name)
    print('Moved:', file)

# Search files with .cda extension in source directory
pattern = "\*.cda"
cdafiles = glob.glob(src_folder + pattern)
#Move all files with a cda extension
for file in cdafiles:
    file_name = os.path.basename(file)
    shutil.move(file, aud_folder + file_name)
    print('Moved:', file)

# Search files with .mid extension in source directory
pattern = "\*.mid"
midfiles = glob.glob(src_folder + pattern)
#Move all files with a mid extension
for file in midfiles:
    file_name = os.path.basename(file)
    shutil.move(file, aud_folder + file_name)
    print('Moved:', file)

# Search files with .midi extension in source directory
pattern = "\*.midi"
midifiles = glob.glob(src_folder + pattern)
#Move all files with a midi extension
for file in midifiles:
    file_name = os.path.basename(file)
    shutil.move(file, aud_folder + file_name)
    print('Moved:', file)

# Search files with .mp3 extension in source directory
pattern = "\*.mp3"
mp3files = glob.glob(src_folder + pattern)
#Move all files with a mp3 extension
for file in mp3files:
    file_name = os.path.basename(file)
    shutil.move(file, aud_folder + file_name)
    print('Moved:', file)

# Search files with .mpa extension in source directory
pattern = "\*.mpa"
mpafiles = glob.glob(src_folder + pattern)
#Move all files with a mpa extension
for file in mpafiles:
    file_name = os.path.basename(file)
    shutil.move(file, aud_folder + file_name)
    print('Moved:', file)

# Search files with .ogg extension in source directory
pattern = "\*.ogg"
oggfiles = glob.glob(src_folder + pattern)
#Move all files with a ogg extension
for file in oggfiles:
    file_name = os.path.basename(file)
    shutil.move(file, aud_folder + file_name)
    print('Moved:', file)

# Search files with .wav extension in source directory
pattern = "\*.wav"
wavfiles = glob.glob(src_folder + pattern)
#Move all files with a wav extension
for file in wavfiles:
    file_name = os.path.basename(file)
    shutil.move(file, aud_folder + file_name)
    print('Moved:', file)

# Search files with .wma extension in source directory
pattern = "\*.wma"
wmafiles = glob.glob(src_folder + pattern)
#Move all files with a wma extension
for file in wmafiles:
    file_name = os.path.basename(file)
    shutil.move(file, aud_folder + file_name)
    print('Moved:', file)

# Search files with .wpl extension in source directory
pattern = "\*.wpl"
wplfiles = glob.glob(src_folder + pattern)
#Move all files with a wpl extension
for file in wplfiles:
    file_name = os.path.basename(file)
    shutil.move(file, aud_folder + file_name)
    print('Moved:', file)
