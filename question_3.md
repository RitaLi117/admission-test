# 1. What is Git and why is it used?

**Git 是一種分散式版本控制系統**，主要用於追蹤和管理程式的更動。
基本概念：
- 記錄檔案 snapshot ，而不是差異
- 大部分操作都可以在本地完成
- Git 能檢查完整性
- Git 通常只增加資料
- 有三種狀態：已提交（committed）、已修改（modified）和已預存（staged）
- 三個主要區域：Git 資料夾、工作目錄（working directory）和預存區（staging area）

### 基本 Git 工作流程：
1. 在自己工作目錄修改檔案。 
2. 預存檔案，將檔案的快照新增到預存區。 
3. 做提交的動作，這會讓存在預存區的檔案快照永久地儲存在 Git 目錄中。

---

### 以下是 Git 的優點，讓大多數人都選擇它

- 免費且開源
- 速度快且檔案體積小
- 分散式系統：在沒有伺服器或沒有網路的環境下，仍可以使用 Git 來進行版本控制
- 協作：不同的開發人員可以共享同一個代碼庫，在不同的分支上獨立進行開發工作後，並將修改項目合併到主分支上。
- 版本控制：追蹤程式碼的修改和歷史記錄，當出現問題時可以找回以前的版本。
- 分支管理：支持多個分支，開發人員可以在不同的分支上進行獨立的工作和測試新功能，然後合併到主分支上。

---

# 2. What is the difference between List, Dictionary, Tuple and Set in Python?

## List and Tuple:
- 都是**有序**列表
- List: 資料是可以更動的
- Tuple: 資料是不可以更動的

## Set and Dictionary:
- 裡面的資料都是**無順序性**的
- Set: 集合，裡面的資料不能重複（會自動刪除重複的資料）
- Dictionary: 字典，一個 Key 對應一個 Value

---

### List:
利用索引**取得**資料
```
print(List[0]) # List 的名字[索引位置]，索引位置是從 0 開始算的
```
利用索引**更新**資料
```
List[0] = 30 # 將 30 放到列表中的第一個位置
print(List[0]) # 輸出會是 30
```
**取得特定範圍**的資料
```
print(List[1:4]) # 取位置是 1, 2, 3 的資料，且不包含位置是 4 的資料
```
**刪除特定範圍**的資料
```
List[1:4] = [] # 刪除位置是 1, 2, 3 的資料，且不包含位置是 4 的資料
print(List) # 輸出時會看到原位置是 1, 2, 3 的資料已被刪除
```
**串接列表**
```
List = List + [40, 50]
print(List) # 40, 50 會在列表的最後面
```
取得列表長度
```
print(len(List))
```
**巢狀列表**（列表內可再放列表）
```
List = [[1, 2, 3], [4, 5, 6]]
print(List[0][1]) # 輸出 2

List[0][0:2] = [7, 7, 7]
print(List[0]) # 輸出 [7, 7, 7, 3]
print(List) # 輸出 [[7, 7, 7, 3], [4, 5, 6]]
```

### Tuple: 
- 操作跟 List 一樣，**但資料不能更動**
```
Tuple = (1, 2, 3)
print(Tuple[2]) # 輸出 3

print(Tuple[0:2]) # 輸出 (1, 2)
```
```
Tuple[0] = 4 # 錯誤： Tuple 的資料不可以變動
```

---

### Set:
用 in/not in 判斷該值有沒有在集合內
```
Set = {1, 2, 3}
print(3 in Set) # True
print(10 in Set) # False
```
交集（取兩個集合中相同的資料）<br>
聯集（取兩個集合中的所有資料，但不重複取）<br>
差集<br>
反交集（取兩個集合中不重疊的部分）
```
Set1 = {1, 2, 3, 4}
Set2 = {2, 3, 4, 5}
Set3 = Set1&Set2 # 交集
print(Set3) # {3, 4, 5}

Set4 = Set1|Set2 # 聯集
print(Set4) # {1, 2, 3, 4, 5}

Set5 = Set1-Set2 # 差集：從 Set1 中減去跟 Set2 重疊的部分
print(Set5) # {1}

Set6 = Set1^Set2 # 反交集
print(Set6) # {1, 5}
```
將字串拆解成集合
```
Set_from_String = set("Hello")
print(Set_from_String) # {'l', 'H', 'e', 'o'} ，無順序性的且去除重複的
```

### Dictionary: 
取值<br>
更新值
```
Dic1 = {"A": "apple", "B": "banana"}
print(Dic1["A"]) # apple

Dic1["A"] = "APPLE"
print(Dic1["A"]) # APPLE
```
用 in/not in 判斷有沒有在字典的 **Key** 內
```
Dic1 = {"A": "apple", "B": "banana"}
print("A" in Dic1) # True
print("B" not in Dic1) # False
```
刪除某個鍵值對
```
Dic1 = {"A": "apple", "B": "banana"}
del Dic1["A"]
print(Dic1) # {"B": "banana"}
```
以列表為基礎產生字典
```
Dic2 = {x: X*2 for x in [1, 2, 3]} # for 跟 in 是固定寫法， in 後面接列表
print(Dic2) # {1: 2, 2: 4, 3: 6}
```