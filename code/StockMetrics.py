
import statistics as stats

from code.StockData import StockData


class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

    def average01(self):
        """pt1
        """
        averages = []
        for row in self.data:
            print(row)
            new_list = []
            print(new_list)
            for value in row[1:]:
                if value == '' or value == " ":
                    print('--emptyRow--')
                    continue
                else:
                    new_list.append(float(value))
                    print(new_list, ' <--row value added to list')
                averages.append(round(sum(new_list)/len(new_list),3))
        return averages

    def median02(self):
        median = []
        for row in self.data:
            print(row)
            new_list = []
            print(new_list)
            for value in row[1:]:
                if value == '' or value == " ":
                    print('--emptyRow--')
                    continue
                else:
                    new_list.append(float(value))
                    print(new_list, ' <--row value added to list')
                median.append(round((new_list + 1)/2),3)
        return median

    

    def stddev03(self):
        stdev = []
        for row in self.data:
            print(row)
            new_list = []
            print(new_list)
            for value in row[1:]:
                if value == '' or value == " ":
                    print('--emptyRow--')
                    continue
                else:
                    new_list.append(float(value))
                    print(new_list, ' <--row value added to list')
                stdev.append(round((new_list + 1)/2),3)
        return stdev
        
