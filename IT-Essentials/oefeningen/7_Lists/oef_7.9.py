def main():
    kleuren = ["rood", "wit", "blauw", "oranje", "zwart"]
    maten = ["Small", "Medium", "Large", "extra large"]
    aantal_shirts = [[45, 102, 19, 55, 0], [79, 47, 58, 22, 46], [109, 33, 112, 0, 0], [109, 33, 112, 10, 10]]

    print("Bijbestellen")
    for i in range(len(maten)):
        som = 0
        for j in range(len(kleuren)):
            som += aantal_shirts[i][j]
        ondergrens = som / 3

        ## test voor werking arry
        ## som2 = 0
        ## for j in range(len(kleuren)):
        ##    som2 += aantal_shirts[i][j]
        ## bovengrens = som2 * 3

        print("Bijbestellen " + maten[i] + " als voorraad < " + str(ondergrens))
        for j in range(len(kleuren)):
            if aantal_shirts[i][j] < ondergrens:
                print(maten[i], " " + kleuren[j])


if __name__ == '__main__':
    main()

