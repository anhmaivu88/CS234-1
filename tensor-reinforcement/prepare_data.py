import episodic_data as ed
import quandl
import os

def main():
    #ed.prepare_data('../ib/csv_data/AJP.csv')
    if not os.path.exists("../ib/csv_data/GOLG.csv"):
      prices = quandl.get("LBMA/GOLD")
      prices.to_csv("../ib/csv_data/GOLG.csv")
    ed.prepare_data('../ib/csv_data/GOLG.csv')

if __name__ == '__main__':
    main()
