class Student(object):#inheritance
    def __init__(self,id,fName,lName,county="KE"):
    	self.__id=id
    	self.fname=fName
    	self.lName=lName

    def attend_class(self, **kwargs):
    	'''
    	default values:
    	 loc = 'Hogwarts'
    	 date= current_date
    	 teacher='alex'
    	'''
    	pass

s1 = Student(1,'manuh','muthui')
s1 = Student(1,'allan','m','ug')