def interests():
  print("Enter your interestes, one after the other, and enter\"stop\"when finished")
  set1 = set()
  #activity = ""
  while True:
    activity = input()
    if activity == "stop" :
      break
    set1.add(activity)
  return set1

def tinderTheSecond ():
  print ("First person:")
  p1set = interests()
  print("Second person:")
  p2set = interests()
  common = p1set.intersection(p2set)
  if len (common) > 4:
    print(f"yay - you are a match! you have {len(common)}inetersts in common")
  else:
      print(f"well, i don't think it will work out :( you have only {len(common)} interests in common")

tinderTheSecond()