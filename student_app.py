from student import Student


s1=Student('Emmanuel','Muthui')
s2=Student('Kelvin','kariuki')
s3=Student('Karen','Otieno')
s4=Student('Judith','Mwendi')
s5=Student('blessing','Cheptoi')
s6=Student('derrick','kakakmt')
s7=Student('james','Ignite')
s8=Student('morean','muthama')
s9=Student('vincent','athis')
s10=Student('Ruth','mutisya')
s11=Student('Titus','kaimetu')
    
s1.attend_class(date='Thu Aug 18 22:54:52 2016')
s2.attend_class(date='Thu Aug 18 22:54:52 2016')
s3.attend_class(date='Thu Aug 18 22:54:52 2016', teacher='Mwaleh')
s4.attend_class(date='Thu Aug 18 22:54:52 2016', teacher="njira")
s5.attend_class(date='Thu Aug 18 22:54:52 2016', teacher='Nandaa')
    
print(s1.specific_day_attendees(date='Thu Aug 18 22:54:52 2016'))

   
    