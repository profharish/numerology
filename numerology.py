##http://www.indianastrologyhoroscope.com/Numerology.html
name = input("Enter your full name:")
low = name.lower()
sum = 0
thisdict= {
  "a": 1,
  "b": 2,
  "c": 3,
  "d": 4,
  "e": 5,
  "f": 8,
  "g": 3,
  "h": 5,
  "i": 1,
  "j": 1,
  "k": 2,
  "l": 3,
  "m": 4,
  "n": 5,
  "o": 7,
  "p": 8,
  "q": 1,
  "r": 2,
  "s": 3,
  "t": 4,
  "u": 6,
  "v": 6,
  "w": 6,
  "x": 5,
  "y": 1,
  "z": 7
}
for ch in low :
    print(ch)
    x = thisdict.get(ch)
    print (x)
    sum = sum+ x
print(sum)
tot=0
while(sum>0):
    dig=sum%10
    tot=tot+dig
    sum=sum//10
print(tot)
finaldict= {
  1: "SUN",
  2: "MOON",
  3: "JUPITER",
  4: "RAHU",
  5: "MERCURY",
  6: "VENUS",
  7: "KETU",
  8: "SATURN",
  9: "MARS",}
  
x = finaldict.get(tot)
print(x)
   


