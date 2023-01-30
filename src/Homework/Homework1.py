# TASK 1
# Տրված է թվաբանական պրոգրեսիայի առաջին և երկրորդ անդամները։ Տրված n֊ի
# համար, վերադարձնել այդ պրոգրեսիայի n֊րդ անդամը։

def arithmetic_progression(a1, a2, n):
    arr = [a1, a2]
    d = a2 - a1
    nth_term = a1 + (n - 1) * d
    arr.append(nth_term)
    return arr


#print(arithmetic_progression(10, 12, 6))

# Task2
# CodeMaster-ը նոր է վերադարձել գնումներից։ Նա սկանավորեց իր գնած ապրանքների չեկը և ստացված շարանը տվեց Ratiorg֊ին՝ պարզելու գնված ապրանքների ընդհանուր թիվը: Քանի որ Ratiorg-ը բոտ է, նա անպայման պատրաստվում է այն ավտոմատացնել, ուստի նրան անհրաժեշտ է ծրագիր, որը կամփոփի բոլոր թվերը, որոնք հայտնվում են տվյալ մուտքագրում:
# Օգնեք Ratiorg-ին՝ գրելով ֆունկցիա, որը վերադարձնում է տվյալ inputString-ում հայտնված թվերի գումարը։

def ratiorg_help(s):
    spl = s.split(" ")
    sum_products = 0
    for i in spl:
        if i.isdigit():
            sum_products += int(i)
    return sum_products


#print(ratiorg_help("2 apples, 12 oranges"))


# TASK 3
# Մուտքագրեք երեք ամբողջ թիվ: Տպեք «Տեսակավորված» բառը, եթե թվերը նշված են ոչ աճող կամ չնվազող հերթականությամբ, իսկ «Չտեսակավորված» հակարակ դեփքում:

def define_sorted(a, b, c):
    arr = [a, b, c]
    if sorted(arr) == arr:
        print("Sorted")
    elif sorted(arr, reverse=True) == arr:
        print("Sorted")
    else:
        print("Unsorted")
    return ""


#print(define_sorted(2,1,0))

#another solution
def define_sorted1(a, b, c):
    if (a<=b and a<=c) or a>=b and a>=c:
        print("sorted")
    else:
        print("unsorted")
    return ""
# print(define_sorted1(5,0,-4))
# print(define_sorted1(1,3,2))


# TASK 4
# Գրել ֆունկցիա, որը տրված բնական թվի համար կստուգի, արդյոք այն
# կատարյալ թիվ է, թե ոչ։
# Հ․Գ Թիվը կոչվում է կատարյալ, եթե այն հավասար է իր բաժանարարների գումարին։

def is_Ideal(num):
    sum = 0
    for i in range(1, int(num / 2) + 1):
        sum += i
    if num == sum:
        return True
    else:
        return False


# print(is_Ideal(6))
# print(is_Ideal(12))


# TASK 5
# Գրել ծրագիր, որը տրված թվային արժեքներով ցուցակի համար, կհաշվի նրա էլեմենտների գումարը։

def list_sum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum


# print(list_sum([1, 2, 3, 4, 4, 32]))


# TASK 6
# Գրել ֆունկցիա, որը տրված թվային արժեքներով ցուցակի համար, կվերադարձնի այդ ցուցակի ամենամեծ էլեմենտը։

def func_max(arr):
    max_element = arr[0]
    for i in range(1,len(arr)):
        if(arr[i]>=max_element):
            max_element = arr[i]
    return max_element


# print(func_max([32, 118, 399, 23456, 988]))


# TASK 7
# Գրել ֆունկցիա, որը տրված ցուցակից կջնջի տրված արժեքին հավասար բոլոր էլեմենտները։

def func_delete(arr, n):
    for i in arr:
        if i == n:
            arr.remove(i)
    return arr


# print(func_delete([1, 34, 45, 189, 34, 2], 34))

# TASK 8
# Գրեք ֆունկցիա որը կվերադարձնի տրված թվային արժեքներով ցուցակի բոլոր էլեմենտների արտադրյալը։


def multiply(arr):
    multiple = 1
    for i in range(len(arr)):
        multiple *= arr[i]
    return multiple


# print(multiply([1, 2, 3, 38, 929]))


# TASK 9
# Գրեք  ֆունկցիա՝ տողը հակադարձելու համար, եթե դրա երկարությունը 4-ի բազմապատիկ է


def rev(s):
    if len(s) % 4 == 0:
        reverse = s[::-1]
    return reverse


# print(rev("Hello hello"))


# TASK 10
# Գրեք  ֆունկցիա՝ որը տրված բնական n թվի համար վերադարձնում է Ֆիբոնաչիի n-րդ անդամը։ Խնդիրը լուծել և ռեկուրսիվ, և իտերատիվ մեթոդներով։


def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(5))


# TASK 11
# Գրել ֆունկցիա, որը տրված 2 բնական թվերի համար կվերադարձնի նրանց ամենափոքր ընդհանուր բազմապատիկը։

def scm(num1, num2):
    if num1 > num2:
        larger = num1
        small = num2
    else:
        larger = num2
        small = num1
    smallest_common_mul = larger
    while smallest_common_mul % small != 0:
        smallest_common_mul += larger
    return smallest_common_mul


# print(scm(15, 18))

# TASK 12
# Գրեք python ծրագիր՝ նշված թվի հաջորդ ամենափոքր պալինդրոմը գտնելու համար:
# Օրինակ 119-ի համար հաջորդ պալինդրոմը 121 է


def find_palindrome(n):
    def helper(n):
        n += 1
        palindrome = [int(i) for i in str(n)]

        if palindrome == list(reversed(palindrome)):
            return n
        return helper(n)

    return helper(n)
print(find_palindrome(119))
print(find_palindrome(121))

# print(find_palindrome(119))


# TASK 13
# Ռոբոտը կանգնած է ուղղանկյուն ցանցի վրա և ներկայումս գտնվում է կետում (X0, Y0): Կոորդինատները ամբողջ թիվ են։ Այն ստանում է N հեռակառավարման հրամաններ: Յուրաքանչյուր հրաման մեկն է՝ վեր, վար, ձախ, աջ: Ճիշտ հրաման ստանալուց հետո ռոբոտը մեկ միավոր է տեղափոխում տվյալ ուղղությամբ։ Եթե ռոբոտը սխալ հրաման է ստանում, նա պարզապես անտեսում է այն: Որտե՞ղ է գտնվելու ռոբոտը բոլոր հրամաններին հետևելուց հետո:
# Ուշադրություն: աջը՝ x0+1, ձախը՝ x0-1, վերևը՝ y0+1, ներքևը՝ y0-1։

def robotics(commands):
    X0, Y0 = 0,0
    x0_pos, y0_pos = X0, Y0
    x_steps, y_steps = 0,0
    for i in commands:
        if i == "up":
            y_steps+=1
        elif i == "down":
            y_steps-=1
        elif i == "right":
            x_steps+=1
        elif i == "left":
            x_steps -=1
    x0_pos +=x_steps
    y0_pos +=y_steps
    final_position = (x0_pos, y0_pos)
    return final_position
# print(robotics(["left", "left", "up", 'up']))

# TASK 14
# Ստուգեք, արդյոք 2 ցուցակները 1-քայլ  ցիկլիկ են:

def are_cyclic(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        rotated_list = list1[i:] + list1[:i]
        if rotated_list == list2:
            return True
    return False
# print(are_cyclic([1,2,3,4,5,6], [6,1,2,3,4,5]))


# TASK 15
# Գրել ծրագիր,  որը ստանւմ է թիվ, գտեք առավելագույն թիվը, որը կարող եք ստանալ՝ ջնջելով տվյալ թվի ուղիղ մեկ թվանշանը:


def delete_number(n):
    n = str(n)
    max_number = 0
    for i in range(len(n)):
        temp = int(n[:i] + n[i+1:])
        if temp > max_number:
            max_number = temp
    return max_number
# print(delete_number(152))
# print(delete_number(967))
# print(delete_number(1001))

# TASK 16
# Գրեք  ֆուկցիա որը ստանում է tuple տիպի օբյեկտ և վերադարձնում նոր tuple բաղկացած միայն առաջին tuple֊ի թվերից։
def get_tuple(obj):
    list = []
    for i in obj:
        if type(i) == int or type(i) == float:
            list.append(i)
    list = tuple(list)
    return list
print(get_tuple((1, "4", 6, 191)))


# TASK 17
# Գրեք Python ֆուկցիա որը ստանում է tuple և ցանկացաց տիպի օբյեկտ և ավելացնում է ստացած արժեքը tuple մեջ։

def adding(obj, random):
    l = list(obj)
    l.append(random)
    fin = tuple(l)
    return fin


# print(adding((2,5,8181, '5789'), 'el'))

# TASK 18
# Գրեք Python ֆուկցիա որը ստանում է tuple դարձնում է string։ Tuplex֊ի էլեմենտները ստրինգում պետք է բաժանված լինեն ‘-’ նշանով։

def tranformer(t):

    seperated = "-".join(t)
    return seperated


# print(tranformer(('abd','56',"578")))

# TASK 19
# Գրեք Python ֆուկցիա որը ստանում է list և պետքա գտնել նրա երկարությունը առանց len() ֆունկցիա֊ի օգտագորձմամբ։

def find_length(arr):
    n = 1
    i = 0
    while(arr[i] != arr[-1]):
        i+=1
        n += 1
    return n
# print(find_length([1,234,8,18,19]))

# TASK 20
# Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.            Given a ticket number n, determine if it's lucky or not. Not using: string, list, tuple, set types.

def is_lucky(n):
    arr = [int(i) for i in str(n)]
    half = len(arr)//2
    if sum(arr[:half]) == sum(arr[half:]):
        return True
    else:
        return False

# print(is_lucky(1230))
# print(is_lucky(239017))

# TASK 21
# Euler function is return a count of numbers not great than N, which are mutualy simple with N.
# Example  φ(6)=2, as only 1 and 5 from 1,2,3,4,5 are mutually simple with 6. Write a function which return count of numbers mutually simple with given N.

def euler(n):
    count = 0

    def gcd(num, n):
        for j in range(1, n):
            if num % j == 0 and n % j == 0:
                gcd = j
        return gcd

    for i in range(1,n):
        helper = gcd(i, n)
        if helper == 1:
            count+=1
    return count


# print(euler(6))

# TASK 22 *
# You are given a 0-indexed string array words, where words[i] consists of lowercase English letters. In one operation, select any index i such that 0 < i < words.length and words[i - 1] and words[i] are anagrams, and delete words[i] from words. Keep performing this operation as long as you can select an index that satisfies the conditions.
# Return words after performing all operations. It can be shown that selecting the indices for each operation in any arbitrary order will lead to the same result.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase using all the original letters exactly once. For example, "dacb" is an anagram of "abdc".

def anagram_delete(anagrams):
    i = 0
    while i < len(anagrams) - 1:
        if sorted(anagrams[i]) == sorted(anagrams[i + 1]):
            del anagrams[i + 1]
        else:
            i += 1
    return anagrams


# print(anagram_delete(['aabb', 'abab', 'bbaa', 'cd','cd']))
# print(anagram_delete(["a","b","c","d","e"]))

# TASK 23 **[&quot;ABC&quot;,&quot;ACB&quot;,&quot;ABC&quot;,&quot;ACB&quot;,&quot;ACB&quot;]
# You are given an array of strings names, and an array heights that consists of distinct positive integers.
# Both arrays are of length n. For each index i, names[i] and heights[i] denote the name and height of the ith person.
# Return names sorted in descending order by the people's heights.

def sortByHeight(names, heights):
    for i in range(len(heights)):
        for j in range(i+1, len(heights)):
            if heights[i] < heights[j]:
                heights[i], heights[j] = heights[j], heights[i]
                names[i], names[j] = names[j], names[i]
    return names
# print(sortByHeight(["Mary","John","Emma"],[180,165,170]))

# Task 24
# In a special ranking system, each voter gives a rank from highest to lowest to all
# teams participating in the competition.
# The ordering of teams is decided by who received the most position-one votes. If two
# or more teams tie in the first position, we consider the second position to resolve the
# conflict, if they tie again, we continue this process until the ties are resolved. If two or
# more teams are still tied after considering all positions, we rank them alphabetically
# based on their team letter.
#
# You are given an array of strings votes which is the votes of all voters in the ranking
# systems. Sort all teams according to the ranking system described above.
# Return a string of all teams sorted by the ranking system.

def ranking(votes):
    vote_counts = {}

    for vote in votes:
        for i, team in enumerate(vote):
            if team not in vote_counts:
                vote_counts[team] = [0] * len(votes[0])
            vote_counts[team][i] += 1

    return vote_counts

# print(ranking(["ABC", "ACB", "ABC", "ACB", "ACB"]))