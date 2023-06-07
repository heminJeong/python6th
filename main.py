def disp():
    def show():
        return "Show Function"
    return show

r_sh = disp()
print(r_sh(), type(r_sh))