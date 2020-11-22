import numpy as np
from colorama import Fore
from colorama import Style
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split 

#@TODO Plotting of graphs lmaoz
#@TODO Linear Dependency

def main():
    print("--------------------------------------------------------")
    inp = input("What do you want me to do?\n")
    try:
        # Matrix Inverse
        if inp == '30' or inp == "inverse":
            print(f"{Fore.GREEN}{Style.BRIGHT}Matrix Inverse{Style.RESET_ALL}")
            inv_input = matrix_converter()
            inv_matrix = inverse(inv_input)
            print("The inverse matrix is:")
            print(inv_matrix)
            main()
        
        if inp =='31' or inp == "transpose":
            text = "Transpose of matrix"
            print(f"{Fore.GREEN}{Style.BRIGHT}{text}{Style.RESET_ALL}")
            inp = matrix_converter()
            transposed = inp.T
            print(f"Transposed matrix:\n{transposed}")
            main()
            
        # Find w given X and y
        if inp =='1':
            text = "Linear Regression"
            print(f"{Fore.GREEN}{Style.BRIGHT}{text}{Style.RESET_ALL}")    
            linear_regression("non-ridge")
            
        if inp =='2':
            text = "Linear Regression with Ridge Regression"
            print(f"{Fore.GREEN}{Style.BRIGHT}{text}{Style.RESET_ALL}")    
            linear_regression("ridge")
        
        if inp =='3':
            text = "Polynomial Regression"
            print(f"{Fore.GREEN}{Style.BRIGHT}{text}{Style.RESET_ALL}")    
            polynomial_regression("non-ridge")
            
        if inp =='4':
            text = "Polynomial Regression with Ridge Regression"
            print(f"{Fore.GREEN}{Style.BRIGHT}{text}{Style.RESET_ALL}")    
            polynomial_regression("ridge")
            
    except EOFError:
        main()
    except KeyboardInterrupt:
        main()

def polynomial_regression(status):
    try:
        det = None
        y_test = None
        mse_value = None
        print("Please input matrix X")
        X = matrix_converter()
        print("Please input matrix Y")
        y = matrix_converter()
        power = int(input("Polynomial power:\n"))
        test_status = input("Add Test cases? (y/n)\n")
        
        poly=PolynomialFeatures(power)
        X = poly.fit_transform(X)
        
        print(X)
        if status == "non-ridge":
            if len(X) > len(X[0]):
                print("\nOverdetermined Case")
                w = np.linalg.inv(X.T @ X)@X.T@y
                print(w)
                
            elif len(X) < len(X[0]):
                print("\nUnderdetermined Case")
                w = X.T @ np.linalg.inv(X @ X.T)@ y
            else:
                print("\nEven-determined case")
                det = np.linalg.det(X)
                if det <= 0.0000000001 and det >= -0.0000000001:
                    det = 0
                    exception_type = "Determinant of X is zero"
                    print(f'{Fore.RED}{Style.BRIGHT}{exception_type}{Style.RESET_ALL}')
                    main()
                w = np.linalg.inv(X) @ y
       
        elif status == "ridge":
            lam = float(input("Value for Lambda: \n"))
            if len(X) > len(X[0]):
                print("\nOverdetermined Case... Using Primal Form")
                col = X.shape[1]
                I = np.ones((col,col))
                reg = lam * I
                w = np.linalg.inv(X.T@X + reg)@X.T@y
                
            elif len(X) < len(X[0]):
                print("\nUnderdetermined Case... Using Dual Form")
                row = X.shape[0]
                I = np.ones((row,row))
                reg = lam*I
                w = X.T @ np.linalg.inv(X @ X.T + reg)@ y
                
            else:
                print("\nEven-determined case")
                det = np.linalg.det(X)
                if det <= 0.0000000001 and det >= -0.0000000001:
                    det = 0
                    exception_type = "Determinant of X is zero"
                    print(f'{Fore.RED}{Style.BRIGHT}{exception_type}{Style.RESET_ALL}')
                    main()
                w = np.linalg.inv(X) @ y
               
        if test_status == "y":
            print("Please input your test case:")
            X_test = matrix_converter()
            # Auto add bias as this is a polynomial regression
            X_test = poly.fit_transform(X_test)
            print(X_test)
            y_test = X_test @ w
            
            mse_status = input("MSE? (y/n)\n")
            if mse_status == "y":
                print("Please input y true value:")
                y_true = matrix_converter()
                mse_value = mean_squared_error(y_true, y_test)
            
        text = "\nSummary Page"
        print(f"{Fore.GREEN}{Style.BRIGHT}{text}{Style.RESET_ALL}")
        print(f"w:\n{w}\n")
        print(f"Determinant of X:\n{det}\n")
        print(f"y_test:\n{y_test}\n")
        print(f"mse:\n{mse_value}\n")
    
        main()

    except EOFError:
        main()
    except KeyboardInterrupt:
        main()

def linear_regression(status):
    try:
        det = None
        y_test = None
        mse_value = None
        print("Please input matrix X")
        X = matrix_converter()
        print("Please input matrix Y")
        y = matrix_converter()
        bias_status = input("Add Bias? (y/n)\n")
        test_status = input("Add Test cases? (y/n)\n")
        
        if bias_status == "y":
            print("Bias is added")
            X = np.append(np.ones((len(X), 1)), X, axis=1)
            print(f'Your new X is:\n{X}\n')
        
        if status == "non-ridge":
            if len(X) > len(X[0]):
                print("\nOverdetermined Case")
                w = np.linalg.inv(X.T @ X)@X.T@y
                
            elif len(X) < len(X[0]):
                print("\nUnderdetermined Case")
                w = X.T @ np.linalg.inv(X @ X.T)@ y
            else:
                print("\nEven-determined case")
                det = np.linalg.det(X)
                if det <= 0.0000000001 and det >= -0.0000000001:
                    det = 0
                    exception_type = "Determinant of X is zero"
                    print(f'{Fore.RED}{Style.BRIGHT}{exception_type}{Style.RESET_ALL}')
                    main()
                w = np.linalg.inv(X) @ y
       
        elif status == "ridge":
            lam = float(input("Value for Lambda: \n"))
            if len(X) > len(X[0]):
                print("\nOverdetermined Case... Using Primal Form")
                col = X.shape[1]
                I = np.ones((col,col))
                reg = lam * I
                w = np.linalg.inv(X.T@X + reg)@X.T@y
                
            elif len(X) < len(X[0]):
                print("\nUnderdetermined Case... Using Dual Form")
                row = X.shape[0]
                I = np.ones((row,row))
                reg = lam*I
                w = X.T @ np.linalg.inv(X @ X.T + reg)@ y
                
            else:
                print("\nEven-determined case")
                det = np.linalg.det(X)
                if det <= 0.0000000001 and det >= -0.0000000001:
                    det = 0
                    exception_type = "Determinant of X is zero"
                    print(f'{Fore.RED}{Style.BRIGHT}{exception_type}{Style.RESET_ALL}')
                    main()
                w = np.linalg.inv(X) @ y
        
        if test_status == "y":
            print("Please input your test case:")
            X_test = matrix_converter()
            if bias_status == "y":
                X_test = np.append(np.ones((len(X_test), 1)), X_test, axis=1)
            y_test = X_test @ w
            
            mse_status = input("MSE? (y/n)\n")
            if mse_status == "y":
                print("Please input y true value:")
                y_true = matrix_converter()
                mse_value = mean_squared_error(y_true, y_test)
            
        text = "\nSummary Page"
        print(f"{Fore.GREEN}{Style.BRIGHT}{text}{Style.RESET_ALL}")
        print(f"w:\n{w}\n")
        print(f"Determinant of X:\n{det}\n")
        print(f"y_test:\n{y_test}\n")
        print(f"mse:\n{mse_value}\n")
    
        main()

    except EOFError:
        main()
    except KeyboardInterrupt:
        main()
    
def inverse(X):
    try:
        np.linalg.inv(X)
    except Exception as err:
        exception_type = type(err).__name__
        print(f'{Fore.RED}{Style.BRIGHT}{exception_type}{Style.RESET_ALL}') 
        main()
    return np.linalg.inv(X)

def matrix_converter():
    contents = []
    while True:
        if len(contents) == 0:
            line = input("Please enter your matrix:\n")
        else:
            line = input()
        if line == '':
            break
        line_array = list(map(lambda x: float(x), line.split()))
        contents.append(line_array)
    
    numpy_content = np.array(contents)
    return numpy_content


if __name__ == '__main__':
    main()