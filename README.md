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

# Reference -- 補充

* [機器學習：建立線性迴歸資料與預測！](https://ithelp.ithome.com.tw/articles/10197248)
    > `regressionmlflow.ipynb`
