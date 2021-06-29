class Time:
    def __init__(self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second
    def __add__(self,other):
        second=self.second+other.second
        minute=self.minute+other.minute+(second/60)
        hour=self.hour+other.hour+(minute/60)
        minute=minute%60
        second=second%60
        return "%d: %d: %d"%(hour,minute,second)
    def __str__(self):
        return "%d: %d: %d"%(self.hour,self.minute,self.second)

t1=Time(5,20,30)
print("First time is:\t",t1)     
t2=Time(4,15,30)
print("Second time is:\t",t2)
t3=t1+t2
print("Total time is:\t",t3)
    
