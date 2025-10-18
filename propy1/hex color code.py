if __name__ == '__main__':
    n = int(input())
    cssCode = ""
    for _ in range(n):
        cssCode += input()
    #print(cssCode)

    clrList = []
    validClr = ['1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','a','b','c','d','e','f']

    for i in range(len(cssCode)):
        chck = 0
        if cssCode[i] == '#':
            try:
                clr6 = cssCode[i] + cssCode[i+1] + cssCode[i+2] + cssCode[i+3] + cssCode[i+4] + cssCode[i+5] + cssCode[i+6]
                #print(clr6)
                for j in range(6):
                    if clr6[j+1] in validClr:
                        chck += 1
                #print("chck1 =" + str(chck))
                if chck == 6 and (cssCode[i+7] != '{') and not (cssCode[i+7].isalnum()):# for #bonkers
                        print(clr6)
            except IndexError:
                #print("IE1")
                pass

            if chck != 6:
                chck = 0
                try:
                    clr3 = cssCode[i] + cssCode[i+1] + cssCode[i+2] + cssCode[i+3]
                    #print(clr3)
                    for j in range(3):
                        if clr3[j+1] in validClr:
                            chck += 1
                    #print("chck2="+str(chck))
                    if chck==3 and (cssCode[i+4] != '{') and not (cssCode[i+4].isalnum()):#for #bonks
                        print(clr3)
                except:
                    #print("IE2")
                    pass



# 1 test case out of 6 is still failing and i have spotted 3(kinda) loopholes in my code
# first- if selector == #bonkers i.e. next char is not {. as i am picking up only 6 chars. SOL- i should only pick up string's part that or consider only that part that is between {} [and string b/w }{ should be rejected]
#second- if color code == #bonkers: i can eliminate some of cases by checking chck value and reject chck = 4,5 etc but wut abt when chck = 7,8 or more. shld i check that adjacent values are not validclr?
#i unlocked that test case using hackos and just fex taped that error but problem 1 requires complete rebuild, so will do that later using list prolly

#unlocked test case
# 35
# .arrow-up {
# 	width: 0;
# 	height: 0;
# 	border-left: 5px solid transparent;
# 	border-right: 5px solid transparent;
#
# 	border-bottom: 5px solid black;
# }
#
# .arrow-down {
# 	width: 0;
# 	height: 0;
# 	border-left: 20px solid transparent;
# 	border-right: 20px solid transparent;
#
# 	border-top: 20px solid #f00;
# }
#
# .arrow-right {
# 	width: 0;
# 	height: 0;
# 	border-top: 60px solid transparent;
# 	border-bottom: 60px solid transparent;
#
# 	border-left: 60px solid green;
# }
#
# #f0f {
# 	width: 0;
# 	height: 0;
# 	border-top: 10px solid transparent;
# 	border-bottom: 10px solid transparent;
#
# 	border-right:10px solid blue;
# }