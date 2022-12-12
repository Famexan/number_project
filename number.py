class Number:
    def __init__(self, value):
        self.value = value

    def get_number(self):
        """ Returns the number. returns: int """
        number = self.value
        return number


    def is_odd(self):
        """ Returns True if the number is odd, otherwise False. returns: bool """
        number = self.value
        if number % 2 == 1:
            return True
        else:
            return False


    def is_even(self):
        """ Returns True if the number is even, otherwise False.  returns: bool """
        number = self.value
        if number % 2 == 0:
            return True
        else:
            return False

    def is_prime(self):
        """ Returns True if the number is prime, otherwise False. returns: bool """
        number = self.value
        count = 0
        for i in range(2,number):
            if number % i == 0:
                count += 1
        
        if count > 0:
            return False
        else:
            return True


    def get_divisors(self):
        """ Returns a list of all the divisors of the number. returns: list """
        number = self.value
        list_count = []

        for i in range(2,number + 1):
            if number % i == 0:
                list_count.append(i)
        return list_count


    def get_length(self):
        """ Returns the number of digits in the number. returns: int """
        number = self.value
        for i in range(1,number):
            print(i)


    def get_sum(self):
        """ Returns the sum of all the digits in the number.b returns: int """
        number = self.value
        sum = 0
        while number:
            s1 = number % 10
            sum += s1
            number //= 10
        return sum


    def get_reverse(self):
        """ Returns the number in reverse. returns: int """
        number = self.value
        rev = 0
        while number:
            rev *= 10
            s1 = number % 10
            rev += s1
            number //= 10
        return rev


    def is_palindrome(self):
        """ Returns True if the number is a palindrome, otherwise False. returns: bool """
        number = self.value
        dig = []
        while number:
            s1 = number % 10
            dig.append(s1)
            number //= 10

        count = 0
        med = len(dig) // 2

        for i in range(0,med):
            if dig[i] == dig[-(i+1)]:
                count +=1
        
        if count == med:
            return True
        else:
            return False


    def get_digits(self):
        """ Returns a list of all the digits in the number. returns: list """
        number = self.value
        dig = []
        while number:
            s1 = number % 10
            dig.append(s1)
            number //= 10
        dig.reverse()
        return dig


    def get_max(self):
        """ Returns the largest digit in the number. returns: int """
        number = self.value
        max = 0
        while number:
            s1 = number % 10
            if s1 > max:
                max = s1
            number //= 10
        return max


    def get_min(self):
        """ Returns the smallest digit in the number. returns: int """
        number = self.value
        min = number
        while number:
            s1 = number % 10
            if s1 < min:
                min = s1
            number //= 10
        return min


    def get_average(self):
        """ Returns the average of all the digits in the number. returns: float """
        number = self.value
        aver = 0
        count = 0
        while number:
            s1 = number % 10
            aver += s1
            number //= 10
            count +=1
            print(count)
        average = aver / count
        return average


    def get_median(self):
        """ Returns the median of all the digits in the number. returns: float """
        pass

    def get_range(self):
        """ Returns the range of all the digits in the number. returns: list """
        pass

    def get_frequency(self):
        """ Returns a dictionary of the frequency of each digit in the number. returns: dict """
        pass
    

# Create a new instance of Number
number = Number(1234321)
print(number.is_palindrome())