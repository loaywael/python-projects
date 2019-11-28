from webAPI import get_movie_recom, get_movie_info


def main():
    data1 = get_movie_recom("It")
    data2 = get_movie_info("It")
    print(data1)
    print(data2)


if __name__ == "__main__":
    main()

