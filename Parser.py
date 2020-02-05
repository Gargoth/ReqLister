from Req import Req

def parse(txtList):
    for i in range(len(txtList)):
        try:
            category = txtList[i][:txtList[i].index("|")]

            if txtList[i].count("|") == 2:
                name = txtList[i][txtList[i].index("|")+1 : txtList[i].rindex("|")]
                if txtList[i][txtList[i].rindex("|")+1:].startswith("#"):
                    ddate = txtList[i][txtList[i].rindex("#"):]
                else:
                    ddate = txtList[i][txtList[i].rindex("|")+1:]
            elif txtList[i].count("|") == 1:
                name = txtList[i][txtList[i].index("|")+1 :]
                ddate = ""

            Req(category, name, ddate)
        except(ValueError):
            if txtList[i] == "":
                print(f"Value Error at line {i} due to Empty Line")
            else:
                print(f"Value Error at line {i} due to \"{txtList[i]}\"")