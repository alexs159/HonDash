class Bar:
    
    def __init__(self,canvas,x,y,minWidth,maxWidth,minHeight,maxHeight,minValue,maxValue,color):
        self.x=x
        self.y=y
        self.canvas = canvas
        self.minWidth = minWidth
        self.maxWidth = maxWidth
        self.minHeight = minHeight
        self.maxHeight = -maxHeight
        self.minValue = minValue
        self.maxValue = maxValue
        self.idBar = self.canvas.create_rectangle(x,y,x+self.maxWidth,y+self.maxHeight,fill=color,outline=color)

    def setHeight(self,value):
        
        if value > self.maxValue:
            value = self.maxValue
        elif value < self.minValue:
            value = self.minValue

        newHeight = (((value - self.minValue) * (self.maxHeight - self.minHeight)) / (self.maxValue - self.minValue)) + self.minHeight
        newHeight = self.y+newHeight
        actualDimension = self.canvas.coords(self.idBar)
        self.canvas.coords(self.idBar,actualDimension[0],newHeight,actualDimension[2],actualDimension[3])


        
    def setWidth(self,newWidth):
        actualDimension = self.canvas.coords(self.idBar)
        self.canvas.coords(self.idBar,actualDimension[0],actualDimension[1],newWidth,actualDimension[3])

