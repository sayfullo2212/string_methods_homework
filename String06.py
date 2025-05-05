def main(s):
    """
    A variable of type str is given. Check that it consists only of numbers.
    Args:
        s: str
    Returns:
        bool: answer
    """
    if s.isdigit() :
       return "satr faqat raqamlardan iborat"
    else :
        return "satrda raqamlardan boshqa qo'shimchalar bor" 
    return s.isdigit()
