import cv2
import pytesseract
import glob
import pandas as pd
from itertools import chain,islice

location = "images/*"

list_of_list = []
for file in glob.glob(location):
	img = cv2.imread(file)
	custom_config = r'--oem 3 --psm 6'
	# doing ocr using pytesseract
	list_of_list.append((pytesseract.image_to_string(img, config=custom_config).split('\n')[:-1]))

# unpacking all list in as single list
chained_list = list(chain(*list_of_list))
chained_list= [i for i in chained_list if ("ID:" in i) or ("Name:" in i)]

# making sublist , where each list contains 2 items(id and names)
chunks = [chained_list[x:x+2] for x in range(0, len(chained_list), 2)]

# making a dataframe corresponding name vs id number
df = pd.DataFrame(chunks, columns=['id', 'name'])
df['id'] = df['id'].apply(lambda x:int(x.split(':')[1].strip()))
df['name'] = df['name'].apply(lambda x:x.split(':')[1].strip())
df = df[["name","id"]]

print(df)

# saving the generated dataframe as csv file
df.to_csv("id_VS_name.csv", index=False)
