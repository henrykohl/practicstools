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
        mlflow.log_params("a",a)
        mlflow.log_params("b",b)
        mlflow.log_params("opt",opt)
        print(f"my result is {result}")
        print(f"my result regrading {opt} is {result}")
        mlflow.log_params("result", result)