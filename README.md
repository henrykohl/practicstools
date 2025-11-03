# practicstools -- MLflow Demo

* A portion of [Lecture 13 -- MLFlow & DVC integration - Part 3](https://www.youtube.com/watch?v=aS466KYOxB4)

* (18:05) 啟用新個 Conda Lab -- practicstools
    > 等同建立新的 GitHub

* 建立 `requirements.txt`
    ```txt
    pandas
    mlflow==2.2.2
    ```

* [mlflow 2.9.2](https://mlflow.org/releases/2.9.2)

* [mlflow pypi 2.9.2](https://pypi.org/project/mlflow/2.9.2/)

* (22:50) 執行 `conda create -p env python=3.8 -y` and `source activate ./env`

* (23:55) 執行 `pip install -r requirements.txt`

* (26:00) 執行(測試 mlflow 是否安裝成功)
    ```python
    python
    import mlflow
    import pandas
    exit()
    ```

* [MLflow Tracking Quickstart](https://mlflow.org/docs/latest/ml/tracking/quickstart/)

* [Core Components of MLflow](https://mlflow.org/docs/3.0.1/introduction/)

* (43:03) 建立 `experiments.py`
    ```python
    import mlflow

    def calculator(a,b):
        return (a*b)


    if __name__ == '__main__':
        a,b=1084,3470
        result=calculator(a,b)
        print(f"my result is {result}")
    ```
    > 執行 `python experiments.py`

* (48:00) 修改 `experiments.py`
    ```python
    import mlflow

    def calculator(a,b,operation=None):
        if operation == "add":
        return (a+b)
        if operation == "sub":
        return (a-b)
        if operation == "mul":
        return (a*b)
        if operation == "div":
        return (a/b)
        


    if __name__ == '__main__':
        a,b=10454,314046
        result=calculator(a,b,"add")
        print(f"my result is {result}")
    ```
    > 執行 `python experiments.py`

* (50:24) 修改 `experiments.py`
    ```python
    import mlflow
    
    def calculator(a,b,operation=None):
        if operation == "add":
        return (a+b)
        if operation == "sub":
        return (a-b)
        if operation == "mul":
        return (a*b)
        if operation == "div":
        return (a/b)


    if __name__ == '__main__':
        a,b,opt=10454,314046,"add" ## a,b,opt=104,314,"sub" (再次測試)
        with mlflow.start_run():  ## 意味著 MLflow server will start
        result=calculator(a,b,opt)
        mlflow.log_param("a",a)
        mlflow.log_param("b",b)
        mlflow.log_param("opt",opt)
        print(f"my result is {result}")
        mlflow.log_param("result", result)

    ```
    > 執行 `python experiments.py` \
    > 根目錄下會建立 /mlflow 資料夾

* (57:51) 修改 `experiments.py`
    ```python
    a,b,opt=109,3142,"div" ## a,b,opt=10903406,31424565,"mul" (再次測試)
    with mlflow.start_run():
        ...
        print(f"my result regrading {opt} is {result}")
        ...
    ```
    > 執行 `python experiments.py`

* (1:04:48) 執行 `mlflow ui`

* (1:07:30) Demo run `mlflow ui` locally (1:16:24 done)

## Reference -- 補充

* [機器學習：建立線性迴歸資料與預測！](https://ithelp.ithome.com.tw/articles/10197248)
    > `regressionmlflow.ipynb`

# DVC Demo

+ The Note of [Lecture 14 -- DVC & Airflow in End-to-End Project](https://www.youtube.com/watch?v=WwwvtPgjpQw)

+ Resource: [DVC-Demo Github](https://github.com/sunnysavita10/DVC-Demo)

* (15:05) 開啟 [practicaltools](https://github.com/henrykohl/practicstools) Github
  > 清空(移除所有檔案)

* (17:17) 執行 
  ```bash
  ls -a
  rm -rf .git
  ls -a
  ```

* [DVC Documentation](https://dvc.org/doc)

* (22:30) 執行 `git remote -v`
  > haven't initialized the git. So it shows "fatal: not a git repository"

* 執行 
  ```bash
  git init
  ls -a
  git status
  touch README.md
  git status
  #git commit -m "first commit"
  git add README.md
  git config --global user.email "you@example.com"
  git config --global user.name "Your name"
  git commit -m "first commit"
  git status
  ```

* (28:27) without 'git', we cannot use DVC.

* (38:43) `touch test.py`
  ```python
  import pandas as pd
  Data=[
    {"name":"sunny","age":28,"city":"bhopal"},
    {"name":"sudhanshu","age":33,"city":"Delhi"},
    {"name":"krish","age":35,"city":"bengalore"},
    {"name":"vikas","age":29,"city":"pune"}
  ]

  Data = pd.DataFrame(Data)

  Data.to_csv("data/data.csv",index=False)
  ```
* 建立 `/data` 資料夾

* (33:20) 執行
  ```bash
  git status
  git add test.py
  git commit -m "second commit"
  git log

  git checkout 編號 # 編號是 commit id (讓檔案回到對應此 commit id 當時的狀態)
  ```

* (37:20) 執行
  ```bash
  python test.py
  pip list # pandas 還未安裝
  conda create -p venv python=3.8 -y
  ```

* (38:24) 執行 
  ```bash
  touch requirements.txt
  conda activate ./venv
  pip install -r requirements.txt
  ````
  > 建立 `requirements.txt` 
  > > ```python
  > > pandas
  > > ```

* (40:20) 執行 `python test.py`

* (44:29) 修改 `requirements.txt`
  ```txt
  pandas
  dvc
  ```
* [Get Started with DVC](https://dvc.org/doc/start)

* (45:55) 再次執行 `pip install -r requirements.txt`

* 執行 
  ```bash
  python
  import dvc
  exit()

  git status ## 顯示 untracked files
  ```

* (48:45) 執行 `touch .gitignore`
  ```txt
  /venv
  ```
  
* (51:12) 執行 `dvc init`
  > 自動建立 `.dvcignore` 與 `/.dvc` 資料夾

* (53:08) 查看 `.dvc` 資料夾
  > 內含 `config` 與 `.gitignore` 檔案，以及 `/tmp` 資料夾

* (56:35) 執行 `git status` 顯示
  ```txt
  .dvc/.gitignore
  .dvc/config
  .dvcignore
  ```
  > Changes to be committed (自動產生)

* (58:10) 執行 
  ```bash
  git commit -m "third commit"
  git status
  ```

* (1:00:07) 執行 `dvc add data/data.csv` 後，在`/data` 資料夾之下，
  > 產生 `data.csv.dvc` 檔案 \
  > 產生 `.gitignore` 檔案

* (1:04:31) 
  <pre>
  We never use git/github for data management/versioning

    git/github
      |
      |------> Source Code Management[SCM] (O) / Data Tracking (X)
      1. Storage size (<25MB)
      2. Conflict resolution (SCM:version)
      3. Performance (pushing data causes degradation performance)
  </pre>

* (1:13:40) 執行 `git status`

* (1:14:45) 執行 `git commit -m "fourth commit"`
  > "nothing added to commit..." (fourth commit 應該是不需要，因為沒有任何檔案狀態有所改變)

* (1:15:59) 新增一行資料 `data/data.csv`
  ```csv
  ...
  dipesh,31,agra 
  ```

* 在 `data.csv.dvc` 查看 md5 的 id

* (1:16:21) 執行 `dvc add data/data.csv`
  > 在 `data.csv.dvc` 中 md5 的 id 發生改變

* (1:17:00) 執行 `git status`，沒有新的改變 

* `.dvc` 資料夾中產生 `/cache` 資料夾，裡面有兩個資料夾，名稱其實就是 md5 的 id 開頭的字串前兩碼

* (1:18:40) 再新增一行資料 `data/data.csv`
  ```csv
  ...
  rahul,30,goa 
  ```

* (1:18:52) 執行 `dvc add data/data.csv`
  > `.dvc/cache` 中 又會新增一個資料夾 \
  > 在 `data.csv.dvc` 中 md5 的 id 又再次發生改變

* 這裡要在 `data/data.csv` 中刪除後三行，但 lecture demo出現一些問題，所以就跳過

* (1:20:56) 再新增一行資料 `data/data.csv`
  ```csv
  ...
  paul,28,mumbai
  ```

* (1:21:05) 執行 `dvc add data/data.csv`
  > `.dvc/cache` 中 又會新增一個資料夾 \
  > 在 `data.csv.dvc` 中 md5 的 id 又再次發生改變

* (1:27:45) 刪除 在 `.dvc/cache` 下所有資料夾

* (1:28:15) 在 `data/data.csv` 中刪除最後三筆資料，保留前五筆資料

* (1:28:17) `dvc add data/data.csv`
  > `.dvc/cache` 中 新增一個資料夾 \
  > 在 `data.csv.dvc` 中 md5 的 id 發生改變

* (1:29:55) 執行 
  ```bash
  git add data/data.csv.dvc
  git commit -m "first version"
  ```

* (1:30:25) 新增一行資料 `data/data.csv`
  ```csv
  ...
  dipesh,31,agra 
  ```

* (1:30:40) 執行 `dvc add data/data.csv`
  > 在 `data.csv.dvc` 中 md5 的 id 發生改變 \
  > `.dvc/cache` 中 新增一個資料夾 

* (1:31:11) 執行 
  ```bash
  git add data/data.csv.dvc
  git commit -m "second version"
  ```

* (1:30:25) 新增一兩行資料 `data/data.csv`
  ```csv
  ...
  rahul,30,goa 
  paul,28,mumbai
  ```

* (1:31:52) 執行 
  ```bash
  dvc add data/data.csv ## md5 的 id 改變
  git add data/data.csv.dvc 
  git commit -m "third version"
  ```

* (1:32:33) 在 `data/data.csv` 中刪除最後四筆資料，保留前四筆資料

* (1:32:40) 執行 
  ```bash
  dvc add data/data.csv ## md5 的 id 改變
  git add data/data.csv.dvc 
  git commit -m "fourth version"
  ```

* (1:33:55) 執行 `git log`
  > 複製一個 commit 的 **id** (lecture demo 複製 second version)

* (1:34:31) 執行 
  ```bash
  git checkout 剛複製的id
  dvc checkout
  ```

* (1:35:29) 再次執行 `git log`
  > 複製 first version 的 commit 的 **id**

* (1:35:42) 執行 
  ```bash
  git checkout 剛複製的id
  dvc checkout
  ```
  > `data/data.csv` 改變成對應的版本 (first version)

* (1:36:10) 複製 third version 的 commit 的 **id**
  ```bash
  git checkout 剛複製的id
  dvc checkout
  ```
  > `data/data.csv` 改變成對應的版本 (third version)

---

* (1:43:23) `dvc remote add -d remote_storage local_path` 
  > remote_storage 與 local_workspace_path 依據實際的環境輸入

* (1:45:53) 執行 `dvc push`
  > 產生 `/files` 資料夾，Lecture Demo 隨後把此資料夾刪除

* 建立 `myremotestorage` 資料夾
  
* (1:48:46) 執行 
  ```bash
  dvc remote add -d remote_storage2 /workspaces/practicstools/myremotestorage ## 用 codeanywhere 實作的路徑
  dvc push
  ```

* (1:49:35) 在 `/myremotestorage` 中的檔案，對其新增兩筆資料
  ```txt
  ...
  aditya,31,pune
  dibyanshu,32,noida
  ```

* (1:49:48) 執行 
  ```bash
  dvc add data/data.csv
  git add data/data.csv.dvc
  git commit -m "latest version" ## 發生 conflict ??
  ```

* () Lecture 這裡有點亂（發生問題，解決時，commands 被擋住）
  ```bash
  #git commit .dvc/config ## demo 打錯
  git add .dvc/config
  git commit -m "config added"
  dvc push
  ```

* (1:55:11) 秀出 commands

* (1:57:27~2:01:12) 建立 `dvc.yaml` 檔案
  > Review 今天 DVC，且 Overview 下一個課程 Airflow  

# DVC Demo 2

+ The Note of [Lecture 15 -- Airflow in End-to-End Project ](https://www.youtube.com/watch?v=JrON6Np32TM)

+ Resource: [DVC-Demo Github](https://github.com/sunnysavita10/DVC-Demo)

* 開啟 [practicaltools](https://github.com/henrykohl/practicstools) Github

* (11:35) 建立 `stage_01.py` 與 `stage_02.py`
  ```python
  # stage_01.py
  with open("artifact.txt","w") as f:
    f.write("my name is sunny and here u am executing stage one")
  ```
  ```python
  # stage_02.py
  with open("artifact.txt","r") as f:
    text=f.read()
  print(text)
  ```

* () 建立/編輯 `dvc.yaml`
  ```yaml
  stages:
    stage_01:
      cmd: python stage_01.py
      deps:
        - stage_01.py
      outs:
        - artifact.txt


    stage_02:
      cmd: python stage_02.py
      deps:
        - artifact.txt
        - stage_02.py
  ```

* (20:43) 執行 
  ```bash
  source activate ./venv

  python
  import dvc
  exit()

  dvc repo ## 產生 dvc.lock
  ```

* (22:40) Overview -- `dvc.lock`

* (24:07) Review `/data/data.csv.dvc`

* (27:07)
  <pre>
                          Data (versioning): do by DVC
                      
                                    
                        Pipeline (versioning): do by DVC also - <font color=pink>DVC.yaml</font>
                     
                    
                   stage-01        stage-02        stage-03        stage-04
  <font color="green">Components        | DI |          | DV |          | DT |          | MT |</font>
                     ^  v            ^  v            ^  v            ^  v  
                        |____________|  |____________|  |____________|

  </pre>

  > - Wrtie down the simple configuration inside the YAML file. In the configuration, need to mention the dependencies, need to mention the stagies, need to the outputs. 
  > - Doing some sort of changes, we can easily track it. Those all the changes basically we can keep somewhere. That is called *pipeline versioning*, *pipeline reproducibility*,*project reproducibility*.

* (32:25) Back to `dvc.lock`
  > 執行 `dvc repo` -- Stage 'stage_01' / 'stage_02' didn't change, skipping

* 看 `/.dvc/cache/runs` 資料夾下(是否)變化

* (34:04) 在 `stage_02.py` 新增一行
  ```python
  ...
  print("i am teaching dvc")
  ```

* (34:18) 接著執行 `dvc repo`
  > 顯示 
  ```txt
  ...
  Updating lock file 'dvc.lock'
  ```

* (35:16) 再看 `/.dvc/cache/runs` 資料夾下(是否)變化

* (36:17) 執行 `dvc dag` (give you the dependencies)

* (38:10) 在 `stage_01.py` 新增內容
  ```python
  ...
  with open("artifact2.txt","w") as f:
    f.write("this is my second file")
  ```

* (39:05) 在 `stage_02.py` 新增內容
  ```python
  ...
  print("this is the second example")
  ```

* (39:16) 建立 `stage_03.py`
  ```python
  with open("artifact2.txt","r") as f:
    text=f.read()  
  print(text)
  ```

* (40:00) 修改 `dvc.yaml` (新增內容)
  ```yaml
  ...
    stage_03:
    cmd: python stage_03.py
    deps:
      - artifact2.txt
      - stage_03.py
  ```
  

* (40:59) Check `dvc.lock` (記下'artifact.txt'個' md5 編碼)

* (41:55) 執行 `dvc repo`

* (42:09) 再 Check `dvc.lock` 
  > 'artifact.txt' 的 md5 編碼 沒變 \
  > 'stage_01' 的 md5 編碼改變了 \
  > 'stage_02' 的 md5 編碼改變了 \
  
* `/.dvc/cache/runs` 中會產生新的資料夾

* (44:42) 執行 `dvc dag`

* (Lecture) 建立 Github repository -- 'DVC-mlflow'，將本堂 code 儲放於此。但 demo 有些問題。 