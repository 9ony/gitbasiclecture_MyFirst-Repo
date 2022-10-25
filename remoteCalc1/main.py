#import
from add import add_func
from sub import sub_func

#변수선언
num1 = 50;
num2 = 100;
result = 0;

#메인코드부
result = add_func(num1,num2)
print(num1, "+" , num2 , "=" ,result)
result = sub_func(num1,num2)
print(num1, "-" , num2 , "=" ,result)
