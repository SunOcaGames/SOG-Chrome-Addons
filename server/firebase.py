# 引用必要套件
import firebase_admin
import time as t
from firebase_admin import credentials
from firebase_admin import firestore

print("hi! I'm firebase.py")

# 引用私密金鑰
# path/to/serviceAccount.json 請用自己存放的路徑
cred = credentials.Certificate('sunocagames.json')

# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred)

# 初始化firestore
db = firestore.client()


# 建立文件 必須給定 集合名稱 文件id
# 即使 集合一開始不存在 都可以直接使用


'''儲存訊息'''
def save(name):   
  doc = {
    'online_name':name,
    'online_time':t.time()
  }
  doc_ref = db.collection("Scratch_Online").document("SOG")
  doc_ref.set(doc)

  # 語法
  # doc_ref = db.collection("集合名稱").document("文件id")
  # doc_ref提供一個set的方法，input必須是dictionary

'''自由的上傳資料'''
def update(doc,collection,document):
  doc_ref = db.collection(collection).document(document)
  doc_ref.set(doc)

'''自由的下載資料'''
def dowmdate(path):
  print('read from firebase!(dowmdate)')
  doc_ref = db.document(path)
  try:
      doc = doc_ref.get()
      # 透過 to_dict()將文件轉為dictionary
      #print("{}".format(doc.to_dict()))
      return doc.to_dict()
  except:
      print("指定文件的路徑{}不存在，請檢查路徑是否正確".format(path))
      return False
