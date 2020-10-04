import math

class MathBook:

    def __init__(self, problems_per_page, chapters, problems):
        self.problems_per_page = problems_per_page
        self.chapters = chapters
        self.problems = problems

    def get_mathbook(self):
        book, book_chapter = [], {}
        last_problem = 0

        for chapter in self.chapters:
            book_chapter['chapter'] = chapter
            book_chapter['total problems'] = self.problems[chapter - 1]
            book_chapter['total pages'] = self.problems[chapter - 1] // self.problems_per_page if self.problems[chapter - 1] % self.problems_per_page == 0 else math.floor(self.problems[chapter - 1] / self.problems_per_page) + 1

            book_chapter['problems per chapter'] = []
            problems_sequence = [i for i in range(1, self.problems[chapter - 1] + 1)]
            for i in range(book_chapter['total pages']):
                book_chapter['problems per chapter'].append(problems_sequence[last_problem:last_problem + self.problems_per_page])
                last_problem += self.problems_per_page

            book.append(book_chapter)
            last_problem = 0
            problems_sequence = ''
            book_chapter = {}

        return book

    def get_pages_with_problems(self):
        total_pages, special_problems = 0, 0
        problems = []
        book = self.get_mathbook()
        for page in book:
            for key, value in page.items():
                if key == 'total pages':
                    total_pages += value

        for page in book:
            for key, value in page.items():
                if key == 'problems per chapter':
                    for arr in value:
                        problems.append(arr)

        for i in range(1, total_pages + 1):
            if i in problems[i - 1]:
                special_problems += 1

        return special_problems


def workbook(n, k, arr):
    return MathBook(k, [i + 1 for i in range(n)], arr).get_pages_with_problems()

# if __name__ == '__main__':
def main(n, k, arr):
    # nk = input().split()

    # n = int(nk[0])

    # k = int(nk[1])

    # arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)
    return result
