import cv2
import pickle







class picker : 

  def tes(file,ss):
    width, height = 80,105
    try :
     with open('tempList','rb') as f:
      posList = pickle.load(f)
    except :
      posList = []
    def mouseClick(events,x,y,flags,other):
    
      if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
      if events == cv2.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(posList):
          x1,y1 = pos
          if x1<x<x1+width and y1<y<y1+height:
            posList.pop(i)
      with open('tempList','wb') as f:
        pickle.dump(posList,f)
    
    while True:
        

      img = cv2.VideoCapture(file)
      ret, frame = img.read()
      resize = cv2.resize(frame, (700, 500))
      for i in posList:
        cv2.rectangle(resize,i,(i[0]+width,i[1]+height),(10,20,255),2)
          
      # cv2.imshow("image",resize)
      # cv2.setMouseCallback("image",mouseClick)
      # cv2.waitKey(1)
      # ret, buffer = cv2.imencode('.jpg', resize)
      # resize = buffer.tobytes()
      yoy = cv2.imwrite( "static/uploads/" + ss + ".jpg",resize)
      return "static/uploads/" + ss + ".jpg"
      # cv2.setMouseCallback("image",mouseClick)
      # yield (b'--frame\r\n'
      #       b'Content-Type: image/jpeg\r\n\r\n' + resize + b'\r\n')
      


 