# Downloads-folder-sorting-script
A simple script that sorts your download folder based on the extensions of the files that are inside the downloads folder


┏━━┓╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏┳━┓┏━┓╋╋╋╋┏┓╋╋╋╋┏━┓╋╋╋┏┓┏┓
┗┓┓┣━┳┳┳┳━┳┳┓┏━┳━┓┏┛┃━┫┃━╋━┳┓┏┛┣━┳┳┓┃━╋━┳┳┫┗╋╋━┳┳━┓
┏┻┛┃╋┃┃┃┃┃┃┃┗┫╋┃╋┗┫╋┣━┃┃┏┫╋┃┗┫╋┃┻┫┏┛┣━┃╋┃┏┫┏┫┃┃┃┃╋┃
┗━━┻━┻━━┻┻━┻━┻━┻━━┻━┻━┛┗┛┗━┻━┻━┻━┻┛╋┗━┻━┻┛┗━┻┻┻━╋┓┃
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗━┛

This script allows you to simply sort your downloads folder by running this script. All the steps you need to take in order to be able to run this correctly and have it functioning are:
1) Make folders of these exact names (or if you are lazy and use windows, you can use the script I provided to make these folders for you):
   compressed_files
   disc_files
   executable_files
   font_files
   image_files
   presentation_files
   programming_files
   spreadsheet_files
   system_files
   video_files
   word_processor_and_text_files
   
   If you will be using the script: Just go to the directory where you want to make these folders, paste the script (cmd file) and double click on it

2) For the next step, you just have to go to the 'moving_files.py' file and change the locations for the src_folder, that is supposed to be the Downloads folder and the location of the other folders that we created in step 1
3) You are done! Now all you have to do is, run the 'moving_files.py' file whenever you want to sort your downloads folder and all your files will be moved to the folders you created in step 1, all sorted according to the file types


Notice ⚠ : The file types ".3g2", ".3gp", and ".7z" will not be able to be sorted because they all start with a number and are not detected for some reason. I am not quite sure on how to fix it, but I will try to do so in the future
