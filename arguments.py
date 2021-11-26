# positional arguments
def num_sum(a, b):
    return a+b


print(num_sum(4, 5))


# Default arguments
def num_sum(a, b=5):
    return a+b


print(num_sum(2, 7))

# def num_sum(a=5,b): we cannot put b after default value(a=5), it has to be b, a=5
#     return a+b
# num_sum(2,7)


def num_sum(b, a=8):
    return a+b


print(num_sum(2))


def my_greeting(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello", name + ', ' + msg)


my_greeting('Deg', 'Good Evening')
my_greeting('Anirudh')

# Arbitary arguments


def my_greeting(*names):
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)


my_greeting("Ramana", "Deg", "Anirudh", "Srini")

# calculate sum of variable length arguments(*args)


def num_sum(*nums):
    """
    This function returns the sum of numbers.
    Function accepts varible length arguments.
    """
    print(nums)
    print(type(nums))
    sum = 0
    for num in nums:  # nums are in tuple
        sum += num  # sum=sum+num
    return sum


print(num_sum(2, 4, 5))
print(num_sum(12, 13, 14, 5, 6, 7, 10))

# keywoard arguments(**kwargs)


def person_info(**person):

    for name, designation in person.items():
        print("{} designation is {}".format(name, designation))


person_info(Ramana="ML Engineer", Deg="Python Developer",
            Anirudh="Full Stack developer")
