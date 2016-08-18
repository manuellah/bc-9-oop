class student(object):#inheritance
    def __init__(self,id,fName,lName,county="KE"):
    	self.__id=id
    	self.fname=fName
    	self.lName=lName

    def attend_class(self, **kwargs):