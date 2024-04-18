import  pandas as pd

data = pd.DataFrame({ "name":['uady','san','ram','sachin'],
                      "Age":[23,24,25,26],
                      "branch":["cse","mech","ise","Ece"],
                      "place":["bang","hrr","dvg","rnr"]})
print(data)

data.to_csv('id.csv',index=False)