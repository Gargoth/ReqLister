from datetime import date


class Req:
    ReqList = {}

    def __init__(self, category, name, ddate, due= None):
        self.category = category.lower()
        self.name = name
        self.ddate = ddate
        self.dbgDisplay = f"{self.category}|{self.name}|{self.ddate}"

        if self.category in list(Req.ReqList.keys()):
            Req.ReqList[self.category].append(self)
        else:
            Req.ReqList.update({self.category: [self]})
        
        Req.ReqList[self.category] = sorted(Req.ReqList[self.category], key= lambda a: a.ddate)

    def fDate(self):
        dday = date(int(self.ddate[:self.ddate.index("/")]), int(self.ddate[self.ddate.index(
            "/")+1: self.ddate.rindex("/")]), int(self.ddate[self.ddate.rindex("/")+1:]))
        daysLeft = dday - date.today()

        if daysLeft.days == 0:
            return "Today"
        elif daysLeft.days == 1:
            return "Tomorrow"
        elif 1 < daysLeft.days <= 7:
            return dday.strftime("%A")
        elif 7 < daysLeft.days < 365:
            return dday.strftime("%B %d")
        elif daysLeft.days >= 365:
            return "In years"
        else:
            return daysLeft.days

    def fLine(self):
        if self.ddate.startswith("#"):
            return f"\n - {self.name}  ({self.ddate[1:]})"
        elif self.ddate != "":
            return f"\n - {self.name}  ({self.fDate()})"
        else:
            return f"\n - {self.name}"

    @classmethod
    def fCat(cls, cat):
        output = cat.upper()
        for i in range(len(cls.ReqList[cat])):
            output += cls.ReqList[cat][i].fLine()
        return output

    @classmethod
    def fAll(cls):
        output = ""
        for i in cls.ReqList.keys():
            output += cls.fCat(i) + "\n\n"
        return output