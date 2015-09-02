#              __  __       _     _
#             |  \/  |     (_)   | |
#  _ __  _   _| \  / | __ _ _  __| |
# | '_ \| | | | |\/| |/ _` | |/ _` |
# | |_) | |_| | |  | | (_| | | (_| |   v 0.0.1
# | .__/ \__, |_|  |_|\__,_|_|\__,_|   
# | |     __/ |
# |_|    |___/
#  


# ===================================================================================================
#                             CONFIGURE WHERE AND HOW TO CLEAN BELOW HERE                           #
# ===================================================================================================


clean = {
    "/Users/x/Desktop":{
        "gif":"/Users/x/Pictures/",
        "jpg":"/Users/x/Pictures/",
        "jpeg":"/Users/x/Pictures/",
        "png":"/Users/x/Pictures/",
    },
    #Add additional folders to clean here
    
}


# ===================================================================================================
#                  DO NOT EDIT BELOW THIS LINE UNLESS YOU KNOW WHAT YOU ARE DOING                   #
# ===================================================================================================


import sys, os, shutil

for i in clean:
    start_files = [f for f in os.listdir(i) if os.path.isfile(os.path.join(i,f))]
    for ii in clean[i]:
        for iii in start_files:
            #only work with file-types specified in clean dict
            if iii.endswith(ii):
                #make sure the directory this file will be moved into exists, if not, create it
                if not os.path.exists(clean[i][ii]):
                    os.mkdir(clean[i][ii])
                end_files = [f for f in os.listdir(clean[i][ii]) if os.path.isfile(os.path.join(clean[i][ii],f))]
                lower_end_files = [f.lower() for f in os.listdir(clean[i][ii]) if os.path.isfile(os.path.join(clean[i][ii],f))]
                #make sure the file we're moving doesn't already exist there before moving
                if iii.lower() in lower_end_files:
                    #filename exists in target location, we will rename the file with a number before moving it
                    filecount = 1
                    filename_found = False
                    while not filename_found:
                        #check to see if filename ends in a number already, if so increment that instead of adding a new number
                        if iii.split(".%s"%(ii))[0].split()[-1].isdigit():
                            current_num = iii.split(".%s"%(ii))[0].split()[-1]
                            file_name = iii.split(".%s"%(ii))[0].split()[0]
                            print "found %s %s.%s"%(file_name, current_num, ii)
                            if file_name.lower()+" "+str(filecount)+".%s"%(ii) not in lower_end_files:
                                filename_found = file_name+" "+str(filecount)+".%s"%(ii)
                                os.rename(i+"/%s"%(iii), i+"/%s"%(filename_found))
                                print "renaming %s to %s..."%(i+"/%s"%(iii), i+"/%s"%(filename_found))
                            else:
                                filecount += 1
                        elif iii.split(".%s"%(ii))[0]+" "+str(filecount).lower()+".%s"%(ii) not in lower_end_files:
                            filename_found = iii.split(".%s"%(ii))[0]+" "+str(filecount)+".%s"%(ii)
                            #rename the file before moving to filename_found
                            os.rename(i+"/%s"%(iii), i+"/%s"%(filename_found))
                            print "renaming %s to %s...."%(i+"/%s"%(iii), i+"/%s"%(filename_found))
                        else:
                            filecount+=1
                else:
                    #no duplicates found, lets move the file.
                    filename_found = iii
                #move it to clean[i][ii]
                print "moving %s to %s."%(i+"/%s"%(filename_found), clean[i][ii])
                shutil.move(i+"/%s"%(filename_found), clean[i][ii])
                