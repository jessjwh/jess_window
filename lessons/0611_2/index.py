import data
def main():
    youbike:list[dict] = data.load_data()
    print(youbike)

if __name__ =='__main__':
    main()