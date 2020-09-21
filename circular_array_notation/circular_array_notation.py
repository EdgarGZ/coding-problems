def circularArrayRotation(a, k, queries):
    """
    Input
        - a -> List
        - k -> Int: number of rotations
        - m -> List: indices to check
    """

    for i in range(k):
        last_element = a.pop()
        a.insert(0, last_element)

    result = []
    for i in range(len(queries)):
        result.append(a[queries[i]])

    return result

# if __name__ == '__main__':
def main(a, k, queries):
    # nkq = input().split()

    # n = int(nkq[0])

    # k = int(nkq[1])

    # q = int(nkq[2])

    # a = list(map(int, input().rstrip().split()))

    # queries = []

    # for _ in range(q):
    #     queries_item = int(input())
    #     queries.append(queries_item)

    return circularArrayRotation(a, k, queries)
