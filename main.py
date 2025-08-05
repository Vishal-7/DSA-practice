# def decorator(func):

#     def wrapper(n):
#         print(f"Before executing the function!!")
#         func(n)
#         print(f"After executing the function!!")
#     return wrapper

# @decorator
# def greet(n):
#     print(f"Hello, {n}!!")

# if __name__ == "__main__":
#     greet("Vishal")

temp = [1,1,1,2,2,2,3,3,3,3]

test = set(temp)

print(sum(test))