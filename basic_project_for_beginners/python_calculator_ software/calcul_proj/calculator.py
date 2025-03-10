from add import addition
from multi import multi
from div import division
import matplotlib.pyplot as plt

def main():
    a = int(input("enter any 1st number :"))
    b = int(input("enter any 2nd number :"))
    add_res = addition (a,b)
    multi_res = multi(a,b)
    division_res = division(a,b)

    print("addition :\n",add_res)
    print("multiplication :\n",multi_res)
    print("division:\n",division_res)
    plt.plot([1,2,3],[add_res,multi_res,division_res])
    plt.show()

    
if __name__=="__main__":
    main()
