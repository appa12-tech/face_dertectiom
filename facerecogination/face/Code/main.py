#main python code section
#def Main():
 #   while True:
  #      function()

def Main():

    print("*****Main Menu*****")
    print("Press 1. to determine the total face in the picture: ")
    print("Press 2. to determine whether the two face matches or not: ")
    print("Press 3. for face detection and face recogniton:")
    a=int(input("Enter the above mentioned option:"))


    while a!=4:
        if a==1:
            import face_recog
        elif a==2:
            import img_match
        elif a==3:
            import web_record
    

if __name__=="__main__":
    Main()



